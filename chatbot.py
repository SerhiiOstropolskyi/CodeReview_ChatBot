import argparse

from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Simple command line chatbot with GPT-4"
    )

    parser.add_argument(
        "--personality",
        type=str,
        help="A brief summary of the chatbot's personality",
        default="friendly and helpful",
    )

    args = parser.parse_args()

    initial_prompt = (
        f"You are a conversational chatbot. Your personality is: {args.personality}"
    )
    messages = [{"role": "system", "content": initial_prompt}]

    while True:
        try:
            user_input = input("You: ")
            messages.append({"role": "user", "content": user_input})

            res = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=messages
            )

            messages.append(
                {"role": "assistant", "content": res.choices[0].message.content}
            )

            print(("Assistant: "), res.choices[0].message.content)

        except KeyboardInterrupt:
            print("Exiting...")
            break

    print(res)


if __name__ == "__main__":
    main()

import os
from openai import OpenAI

def main():
    try:
        # Get API key from environment variable
        api_key = os.environ['ZHIPU_AI_API_KEY']

        # Initialize OpenAI client with BigModel base URL
        client = OpenAI(
            api_key=api_key,
            base_url="https://open.bigmodel.cn/api/paas/v4"
        )

        # Make chat completion request
        response = client.chat.completions.create(
            model="glm-4.6",
            messages=[
                {"role": "user", "content": "Hello, what is your name and who created you?"}
            ]
        )

        # Print the assistant's response
        print(response.choices[0].message.content)

    except KeyError:
        print("Error: ZHIPU_AI_API_KEY environment variable not set.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
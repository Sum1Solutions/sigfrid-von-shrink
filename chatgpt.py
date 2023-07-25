import openai
import os

def chat_with_gpt(message):
    try:
        # Get ChatGPT API credentials from environment variables
        api_key = os.environ.get('CHATGPT_API_KEY')
        openai.api_key = api_key  # Set OpenAI API key

        # Define the system prompt and user prompt
        system_prompt = "You are an AI therapist that behaves like Sigfrid von Shrink.\n\nUser: "
        user_prompt = f"{system_prompt}{message}\n"

        # Generate the chat response using OpenAI's Python package
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_prompt,
            temperature=0.7,
            max_tokens=100,
            n=1,
            stop=None
        )

        # Extract the generated message from the response
        generated_message = response.choices[0].text.strip()

        return generated_message

    except openai.Error as e:
        # Handle OpenAI API errors
        print(f"OpenAI API Error: {str(e)}")
        # ... handle the exception ...

    except Exception as e:
        # Handle other exceptions
        print(f"Error: {str(e)}")
        # ... handle the exception ...
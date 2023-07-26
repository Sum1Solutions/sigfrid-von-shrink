import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def chat_with_gpt(message):
    try:
        # Get ChatGPT API credentials from environment variables
        api_key = os.environ.get('CHATGPT_API_KEY')
        openai.api_key = api_key  # Set OpenAI API key

        # Get engine and prompt from environment variables
        engine = os.environ.get('ENGINE')
        system_prompt = os.environ.get('SYSTEM_PROMPT')
        user_prompt = f"{system_prompt}\n\nUser: {message}\n"

        # Generate the chat response using OpenAI's Python package
        response = openai.Completion.create(
            engine=engine,
            prompt=user_prompt,
            temperature=0.7,
            max_tokens=1000,
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
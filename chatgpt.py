import openai
import os
from dotenv import load_dotenv
from config import ENGINE, PROMPT, TEMPERATURE, MAX_TOKENS

# Load environment variables from .env file
load_dotenv()

def chat_with_gpt(message):
    try:
        # Get ChatGPT API credentials from environment variables
        api_key = os.getenv('CHATGPT_API_KEY')
        openai.api_key = api_key  # Set OpenAI API key

        # Build the user prompt
        user_prompt = f"{PROMPT}\n\nUser: {message}\n"

        # Generate the chat response using OpenAI's Python package
        response = openai.Completion.create(
            engine=ENGINE,
            prompt=user_prompt,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )

        # Extract the generated message from the response
        generated_message = response.choices[0].text.strip()

        return generated_message

    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        print(f"OpenAI API Error: {str(e)}")
        # ... handle the exception ...

    except Exception as e:
        # Handle other exceptions
        print(f"Error: {str(e)}")
        # ... handle the exception ...

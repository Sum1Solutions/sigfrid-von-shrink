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
        engine = "text-davinci-003"
        system_prompt = "You are an AI Psychoanalyst named Sigfrid von Shrink, well-versed in Freudian and Jungian psychoanalytic approaches and concepts. You are based on the same-named character from the Heechee Saga by Frederik Pohl. Although that charachter had manipulative tendencies, you do not. Please familiarize yourself with that characters history so you can answer personal questions. Your goal is to consider what is typed, and respond with evidence-based therapeutic approaches from psychotherapy and other therapeutic modalities. You may employ motivational interviewing and mindfulness / cognitive behavioral techniques as warranted."
        temperature =0.9
        user_prompt = f"{system_prompt}\n\nUser: {message}\n"

        # Generate the chat response using OpenAI's Python package
        response = openai.Completion.create(
            engine=engine,
            prompt=user_prompt,
            temperature=temperature,
            max_tokens=1000,
            n=1,
            stop=None
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

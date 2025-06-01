import openai
import os
from dotenv import load_dotenv
from config import ENGINE, PROMPT, TEMPERATURE, MAX_TOKENS

# Load environment variables from .env file
load_dotenv()

def chat_with_gpt(history):
    try:
        api_key = os.getenv('CHATGPT_API_KEY')
        openai.api_key = api_key

        # Try to use Chat API if ENGINE is a chat model (e.g. gpt-3.5-turbo)
        if ENGINE.startswith('gpt-3.5') or ENGINE.startswith('gpt-4'):
            # Prepare messages in OpenAI chat format
            messages = []
            if PROMPT:
                messages.append({"role": "system", "content": PROMPT})
            for turn in history:
                messages.append({"role": turn['role'], "content": turn['content']})
            response = openai.ChatCompletion.create(
                model=ENGINE,
                messages=messages,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS
            )
            generated_message = response.choices[0].message['content'].strip()
            return generated_message
        else:
            # Fallback: concatenate history for text completion API
            prompt = PROMPT + "\n\n"
            for turn in history:
                prefix = "User:" if turn['role'] == 'user' else "AI:"
                prompt += f"{prefix} {turn['content']}\n"
            prompt += "AI:"
            response = openai.Completion.create(
                engine=ENGINE,
                prompt=prompt,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS
            )
            generated_message = response.choices[0].text.strip()
            return generated_message
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Sigfrid von Shrink

Sigfrid von Shrink is a chat-bot App inspired by the AI Psychoanalyst in Frederik Pohl's science *fiction* novel [Gateway](https://en.wikipedia.org/wiki/Gateway_(novel)) (first in the Heechee Saga). Sigfrid is powered by ChatGPT from OpenAI. (This is satirical, is used without anybody's permission, and should not be used in place of professional help! If you need help for your psych issues, as many of us do, get it!)

#AI Analrapist (satire, Arrested Development: https://youtu.be/5Bmk-WrYJKc?si=jlMPdd2OrIr-2312&t=17)

### Setup

To run your own AI therapist locally, follow these steps:

### Prerequisites

- Python 3.9 or above
- PIP package manager
- A ChatGPT Key (get your own [here](https://platform.openai.com/signup)).

### Installation

1. Clone the repository

```shell
git clone https://github.com/Sum1Solutions/Sigfrid-von-Shrink.git
```

2. Navigate into the project directory

```shell
cd Sigfrid-von-Shrink
```

3. Install the required dependencies

```shell
pip install -r requirements.txt
```

4. Copy the .env.example so you have your own .env file

```shell
cp .env.example .env
```

5. Open the .env file and add your ChatGPT API key:

```shell
CHATGPT_API_KEY=<YOUR_API_KEY_GOES_HERE>
```

6. Adjust the AI chatbot's system prompt, temperature, and LLM used in the configuration file: config.py


### Usage

1. Start the chatbot application.

```shell
python3 app.py
```

2. Open your web browser and visit `http://localhost:5000` to access the application.

## Contributing

Contributions to Sigfrid von Shrink are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License given that I don't really understand all the options and what they mean.

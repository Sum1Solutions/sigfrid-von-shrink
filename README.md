# Sigfrid von Shrink

Sigfrid von Shrink is a chat application  powered by ChatGPT from OpenAI and inspired by Frederik Pohls charachter from the science *fiction* series [Gateway](https://en.wikipedia.org/wiki/Gateway_(novel)) (aka the Heechee Saga).

### Setup

To run your own AI therapist follow these steps:

### Prerequisites

- Python 3.7 or above
- pip package manager
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
CHATGPT_API_KEY=PUT_YOUR_API_KEY_HERE
```

### Usage

1. Start the LLM *therapist*

```shell
python3 app.py
```
2. Open your web browser and visit `http://localhost:5000` to access the application.

## Contributing

Contributions to Sigfrid von Shrink are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License given that I don't really understand all the options and what they mean.
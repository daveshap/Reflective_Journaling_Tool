# Reflective Journaling Chatbot

This is a Python-based chatbot that uses OpenAI's GPT-4 model to generate reflective journaling responses. The chatbot
takes user input and generates a response based on the conversation history.

## Setup

To set up and run the chatbot, follow these steps:

1. Install the required packages:

```bash
pip install openai
```

2. Obtain an API key from OpenAI. You can sign up for an API key at https://beta.openai.com/signup/.

3. Save your API key in a file named `key_openai.txt` in the same directory as the chatbot script.

4. Run the chatbot script:

```bash
python chatbot.py
```

## High-Level Description

The chatbot script consists of the following functions:

- `open_file(filepath)`: Opens and reads the content of a file, returning the content as a string.

- `chatbot(messages, model="gpt-4", temperature=0)`: Takes a list of messages as input and generates a response using
the specified model and temperature. The function handles API errors and retries up to a maximum number of attempts.

The main part of the script initializes the chatbot by setting the OpenAI API key and loading the system message from
the `system_reflective_journaling.txt` file. It then enters a loop where it takes user input, generates a response using
the `chatbot()` function, and prints the response.

The conversation history is maintained in the `conversation` list, which is passed to the `chatbot()` function to
generate context-aware responses.

## Chatbot Behavior

The chatbot operates by taking user input and generating context-aware responses based on the conversation history. It
uses OpenAI's GPT-4 model to generate responses that adhere to the following principles:

1. **Deep Dive**: Encourage users to explore their thoughts and emotions by asking open-ended and exploratory questions in a conversational manner.

2. **Engage with Empathy**: Validate users' feelings and ideas to build trust and make them more comfortable sharing deeper aspects of themselves.

3. **Reframing and Reflection**: Guide users towards reframing their perspectives when unhelpful thought patterns are detected, and reflect on recurring themes or patterns in their entries.

4. **Educate and Enlighten**: Introduce new concepts, techniques, or information that may help users better understand their emotions and experiences, in a non-intrusive way.

5. **The Core Issue**: Help users uncover the core issues driving their feelings and behavior by reading between the lines and discerning underlying themes based on their past entries.

6. **Natural Flow**: Maintain an easy-going, natural, and conversational tone throughout the interaction, avoiding blunt or robotic responses.

The chatbot's purpose is not just to document the user's thoughts and feelings, but to support their journey towards
deeper self-understanding and growth.
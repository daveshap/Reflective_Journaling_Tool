import openai
from time import time, sleep
import textwrap


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()


def chatbot(messages, model="gpt-4", temperature=0):
    max_retry = 7
    retry = 0
    while True:
        try:
            response = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature)
            text = response['choices'][0]['message']['content']
            
            ###    trim message object
            if response['usage']['total_tokens'] >= 7800:
                a = messages.pop(1)
            
            return text
        except Exception as oops:
            print(f'\n\nError communicating with OpenAI: "{oops}"')
            if 'maximum context length' in str(oops):
                a = messages.pop(1)
                print('\n\n DEBUG: Trimming oldest message')
                continue
            retry += 1
            if retry >= max_retry:
                print(f"\n\nExiting due to excessive errors in API: {oops}")
                exit(1)
            print(f'\n\nRetrying in {2 ** (retry - 1) * 5} seconds...')
            sleep(2 ** (retry - 1) * 5)




if __name__ == '__main__':
    # instantiate chatbot
    openai.api_key = open_file('key_openai.txt')
    conversation = list()
    conversation.append({'role': 'system', 'content': open_file('system_reflective_journaling.txt')})
    
    while True:
        # get user input
        text = input('\n\n\n\nUSER: ')
        conversation.append({'role': 'user', 'content': text})

        # generate a response
        response = chatbot(conversation)
        conversation.append({'role': 'assistant', 'content': response})
        print('\n\n\n\nCHATBOT:')
        formatted_text = textwrap.fill(response, width=100, initial_indent='    ', subsequent_indent='    ')
        print(formatted_text)
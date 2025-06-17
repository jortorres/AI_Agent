import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def get_prompt_from_arg():  # funciton to get request from console
    arg_num = len(sys.argv)
    if arg_num < 2:
        print("Usage: python3 main.py '<prompt>'")
        sys.exit(1)
    elif arg_num < 3:
        return sys.argv[1]
    if arg_num == 3 and sys.argv[2] == "--verbose":
        return sys.argv[1] 
    else:
        sys.exit(1)

def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY") # get API
    client = genai.Client(api_key=api_key) # create an instance

    arg_prompt = get_prompt_from_arg()

    messages = [types.Content(role="user", parts=[types.Part(text=arg_prompt)]),] # put messages from prompt into a list
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)  # added message and send to gemini

    if len(sys.argv)== 3 and sys.argv[2] == "--verbose":
        print(f"User prompt: {arg_prompt}") # print response
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}") # print prmpt tokens
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n") # print response tokens
        print(response.text)
    else:
        print(response.text) # print response        


if __name__ == "__main__":
     main()
     
import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, function_name_to_callable
import json

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

def call_function(function_call_part, verbose=False):  #fucntions to call the acutal function available
    function_name = function_call_part.name
    function_args = function_call_part.args.copy()
    function_args["working_directory"] = "./calculator"

    if verbose: 
        print(f"Calling function: {function_name}({function_args})")
    print(f" - Calling function: {function_name}")

    if function_name not in function_name_to_callable:
        return types.Content(
            role="tool",
            parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
            )],
        )
    
    results = function_name_to_callable[function_name](**function_args)


    return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": results},
                )
            ],
        )


    

def main():
    MAX_LOOP = 20

    verbose = (len(sys.argv)==3 and sys.argv[2] == "--verbose")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    arg_prompt = get_prompt_from_arg()
    messages = [types.Content(role="user", parts=[types.Part(text=arg_prompt)])]

    for i in range(MAX_LOOP):
        print("\n" + "="*10 + f" AGENT STEP {i+1} " + "="*10)
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt),
        )

        # Print and append candidates
        for candidate in response.candidates:
            print("\n=== Model Step ===")
            if candidate.content.parts and hasattr(candidate.content.parts[0], "text"):
                print(candidate.content.parts[0].text)
            else:
                print(candidate.content)
            messages.append(candidate.content)

        # Handle tool calls
        if response.function_calls:
            for func_call in response.function_calls:
                print(f"\n=== Tool Call: {func_call.name} ===")
                function_results = call_function(func_call, verbose=verbose)
                response_parts = function_results.parts
                result = response_parts[0].function_response.response
                print(json.dumps(result, indent=2))
                messages.append(function_results)
        else:
            print("\n=== Final Model Response ===")
            print(response.text)
            break

if __name__ == "__main__":
     main()
     
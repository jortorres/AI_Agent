AI Agent for Personal Learning

This project builds an AI agent for personal learning using Google's Gemini API. The agent is designed to run arbitrary Python code for educational purposes.

SECURITY RISK: This code is for learning purposes only and does not include security or safety features required for production use. DO NOT USE THIS CODE ON YOUR COMPUTER due to potential risks associated with executing arbitrary code.

Conversation Flow

Below is an example of how the agent interacts in a conversation to perform tasks, such as fixing a bug in a calculator:

User: "Please fix the bug in the calculator"

Model: "I want to call get_files_info..."

Tool: "Here's the result of get_files_info..."

Model: "I want to call get_file_content..."

Tool: "Here's the result of get_file_content..."

Model: "I want to call run_python_file..."

Tool: "Here's the result of run_python_file..."

Model: "I want to call write_file..."

Tool: "Here's the result of write_file..."

Model: "I want to call run_python_file..."

Tool: "Here's the result of run_python_file..."

Model: "I fixed the bug and then ran the calculator to ensure it's working."

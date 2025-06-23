Building AI agent for personal learning, using Google's Gemani API. Build functionality for an Agent to run arbitrary Python code. SECURITY RISK, DON'T USE THIS CODE ON YOUR COMPUTER, It does not have all the security and safety features that a production AI agent would have. It is for learning purposes only.

A list of messages in the "conversation". It will look something like this:
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



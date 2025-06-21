import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    
    try:
        current_file = file_path
        
        if not os.path.isabs(current_file): # check is absolute path
            current_file = os.path.join(working_directory, current_file)
            
        current_file = os.path.abspath(current_file)
        work_dir = os.path.abspath(working_directory)
        
        if not current_file.startswith(work_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(current_file):
            return f'Error: File "{file_path}" not found.'
        if not current_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        results = subprocess.run(["python3", current_file], timeout=30,capture_output=True,text=True, cwd=work_dir)

        if results.returncode != 0:
            return f"STDOUT: {results.stdout}\nSTDERR: {results.stderr}\nProcess exited with code {results.returncode}"

        if results.returncode == 0:
            if not results.stdout and not results.stderr:
                return f"No output produced."
        return f"STDOUT: {results.stdout}\nSTDERR: {results.stderr}"
               
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Executes the specified Python file, constrained to the working directory. Optional arguments can be provided.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="relative file path giving in the prompt.",
                ),
            },
        ),
    )
    


    
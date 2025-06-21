import os
from google.genai import types

def write_file(working_directory, file_path, content):

    try:
        current_file = file_path  
        if not os.path.isabs(current_file): # check is absolute path
            current_file = os.path.join(working_directory, current_file)
        
        current_file = os.path.abspath(current_file) # make absolut path
        work_dir = os.path.abspath(working_directory)
     
        if not current_file.startswith(work_dir): # check if file path is in working path
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        current_dir = os.path.dirname(current_file)  # check for directory name
        
        os.makedirs(current_dir, exist_ok=True) # make directory if needed
        
        with open(current_file, "w") as f:  # write to file from contents sent in
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:  # any errors sent a string response
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes or overwrites the content of the specified file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the file to write to, relative to the working directory.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to write to the file.",
                ),
            },
        ),
    )



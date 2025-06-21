import os
from google.genai import types

def get_file_content(working_directory, file_path):
    
    try:
        current_file = file_path
        MAX_CHARS = 10000
        if not os.path.isabs(current_file): # check is absolute path
            current_file = os.path.join(working_directory, current_file)

        work_dir = os.path.abspath(working_directory)
        current_file = os.path.abspath(current_file)

        if not current_file.startswith(work_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(current_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(current_file, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            # Check if there's more content by trying to read one more character
            if f.read(1):  # If this returns something, the file was longer
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string

    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads the content of the specified file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="the filepath relative form the command prompt.",
                ),
            },
        ),
    )
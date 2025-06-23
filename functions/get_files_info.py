import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    try:

        if not directory or directory in [".", ""]:
            directory = working_directory
        else:
            abs_work_dir = os.path.abspath(working_directory)
            abs_dir = os.path.abspath(os.path.join(working_directory, directory))
            # If the resolved abs_dir is just the working directory, use working directory
            if abs_dir == abs_work_dir:
                directory = working_directory
            else:
                directory = abs_dir
        
                
        work_dir = os.path.abspath(working_directory) 
        arg_dir = os.path.abspath(directory)
        dir_list = os.listdir(directory) # new list with directory contents
        lines = [] 

        if not arg_dir.startswith(work_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(arg_dir):
            return f'Error: "{directory}" is not a directory'
      
        for dir in dir_list: # loop thru contents of directory
            current_path = os.path.join(arg_dir,dir) # creat path
            lines.append(f"- {dir}: file_size={os.path.getsize(current_path)} bytes, is_dir={os.path.isdir(current_path)}") # append to lines
        return "\n".join(lines) # return list seperated by return
    except Exception as e:
        return f"Error: {e}" 
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )
    



    

    
    

    
    



    

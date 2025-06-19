import os

def get_files_info(working_directory, directory=None):
    try:
        if not os.path.isabs(directory): # check is absolute path
            directory = os.path.join(working_directory, directory) # create it
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
    
def get_file_content(working_directory, file_path):
    
    try:
        MAX_CHARS = 10000
        if not os.path.isabs(file_path): # check is absolute path
            file_path = os.path.join(working_directory, file_path)

        work_dir = os.path.abspath(working_directory)
        current_file = os.path.abspath(file_path)
        print(work_dir)
        print(current_file)
        if not current_file.startswith(work_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(file_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) <  MAX_CHARS:
            return file_content_string
        return file_content_string + f' [...File "{file_path}" truncated at 10000 characters]'

    except Exception as e:
        return f"Error: {e}"


    

    
    

    
    



    

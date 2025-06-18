import os

def get_files_info(working_directory, directory=None):


    try:
        if not os.path.isabs(directory):
            directory = os.path.join(working_directory, directory)
        work_dir = os.path.abspath(working_directory)
        arg_dir = os.path.abspath(directory)
        dir_list = os.listdir(directory)


        dir_info = ''
        lines = []

        if not arg_dir.startswith(work_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(arg_dir):
            return f'Error: "{directory}" is not a directory'
    
    
  
        for dir in dir_list:
            current_path = os.path.join(arg_dir,dir)
            lines.append(f"- {dir}: file_size={os.path.getsize(current_path)} bytes, is_dir={os.path.isdir(current_path)}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"

    
    

    
    



    

import os
from functions.working_dir_decorator import is_working_dir


@is_working_dir
def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        is_a_dir = os.path.isdir(target_path_abs)

        if is_a_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(working_dir_abs, exist_ok=True)

        with open(target_path_abs, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: {e}"

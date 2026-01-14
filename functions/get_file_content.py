import os
from config import MAX_CHARS
from functions.working_dir_decorator import is_working_dir


@is_working_dir
def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        is_valid_file = os.path.isfile(target_file_abs)

        if not is_valid_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        content = ""
        is_truncated = False
        with open(target_file_abs, "r") as f:
            content = f.read(MAX_CHARS)
            is_truncated = False if f.read(1) is None else True

        if is_truncated:
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {e}"

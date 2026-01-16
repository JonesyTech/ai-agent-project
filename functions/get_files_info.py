from genericpath import isdir
import os
from functions.working_dir_decorator import is_working_dir
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)


@is_working_dir
def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_dir = os.path.isdir(target_dir)

        if not valid_dir:
            return f'Error: "{directory}" is not a directory'

        # - README.md: file_size=1032 bytes, is_dir=False
        # - {file_name}: file_size={file_size} bytes, is_dir={is_a_dir}

        files_meta_data = []
        for file_name in os.listdir(target_dir):
            file_path_abs = os.path.join(target_dir, file_name)
            is_dir = os.path.isdir(file_path_abs)
            is_file = os.path.isfile(file_path_abs)
            file_size = os.path.getsize(file_path_abs)

            if not is_dir and not is_file:
                continue

            files_meta_data.append(
                f"- {file_name}: file_size: {file_size} bytes, is_dir={is_dir}"
            )

        results = "\n".join(files_meta_data)

        return results
    except Exception as e:
        return f"Error: {e}"

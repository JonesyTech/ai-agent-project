import os


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        is_valid_target = (
            os.path.commonpath([working_dir_abs, target_path_abs]) == working_dir_abs
        )
        is_a_dir = os.path.isdir(target_path_abs)

        if not is_valid_target:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

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

from genericpath import isdir
import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )
        valid_dir = os.path.isdir(target_dir)

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

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

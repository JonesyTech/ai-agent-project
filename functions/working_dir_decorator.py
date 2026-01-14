import os


def is_working_dir(func):
    def wrapper(*args):
        working_directory = args[0]
        relative_path = args[1]

        working_abs = os.path.abspath(working_directory)
        target_abs = os.path.normpath(os.path.join(working_abs, relative_path))

        valid_target_path = os.path.commonpath([working_abs, target_abs]) == working_abs

        if not valid_target_path:
            return f'Error: Cannot execute "{relative_path}" as it is outside the permitted working directory'

        return func(*args)

    return wrapper

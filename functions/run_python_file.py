import os
import subprocess
from functions.working_dir_decorator import is_working_dir


@is_working_dir
def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if not os.path.isfile(target_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_abs]
        if args:
            command.extend(args)

        sp = subprocess.run(
            command,
            cwd=working_directory,
            text=True,
            timeout=30,
            capture_output=True,
        )

        output = ""

        if sp.returncode != 0:
            output += f"Process exited with code {sp.returncode}\n"

        stdout = sp.stdout or ""
        stderr = sp.stderr or ""

        if not stdout and not stderr:
            output += "No output produced"
        else:
            if stdout:
                output += f"STDOUT: {stdout}\n"
            if stderr:
                output += f"STDERR: {stderr}"

        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"

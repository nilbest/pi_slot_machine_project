import os
import platform
import subprocess
import sys

def activate_and_run():
    """Activate the virtual environment and run the main script."""
    env_dir = ".env"  # Change to your virtual environment directory
    activate_script = None
    python_executable = sys.executable

    # Determine platform and appropriate activation script
    if platform.system() == "Windows":
        activate_script = os.path.join(env_dir, "Scripts", "activate.bat")
        command = f'{activate_script} && {python_executable} main.py'
    else:
        activate_script = os.path.join(env_dir, "bin", "activate")
        command = f'source {activate_script} && {python_executable} main.py'

    # Check if the virtual environment exists
    if not os.path.exists(activate_script):
        print("Virtual environment not found. Please run 'python setup.py' to set it up.")
        sys.exit(1)

    # Run the command
    try:
        subprocess.call(command, shell=True)
    except Exception as e:
        print(f"Failed to run the application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    activate_and_run()

import os
import platform
import subprocess
import sys

def run_command(command, shell=False):
    """Helper to run a system command."""
    try:
        subprocess.check_call(command, shell=shell)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

def install_requirements(pip_path=None):
    """Install dependencies from requirements.txt."""
    print("Installing dependencies...")
    pip_command = [pip_path] if pip_path else [sys.executable, "-m", "pip"]
    run_command(pip_command + ["install", "-r", "requirements.txt"])

def create_virtual_env():
    """Create and activate a virtual environment."""
    print("Setting up a virtual environment...")
    env_name = ".env"
    run_command([sys.executable, "-m", "venv", env_name])

    # Get pip path for the created virtual environment
    pip_path = os.path.join(env_name, "Scripts", "pip") if platform.system() == "Windows" else os.path.join(env_name, "bin", "pip")
    return pip_path

def check_platform_dependencies():
    """Check and handle platform-specific dependencies."""
    current_os = platform.system()
    if current_os == "Linux":
        # Detect if running on a Raspberry Pi
        try:
            with open("/sys/firmware/devicetree/base/model", "r") as f:
                model = f.read().lower()
                if "raspberry pi" in model:
                    print("Raspberry Pi detected. Installing RPi.GPIO...")
                    install_requirements()
                else:
                    print("Non-Raspberry Pi Linux system detected. Skipping GPIO installation.")
        except FileNotFoundError:
            print("Not a Raspberry Pi device.")
    elif current_os == "Windows":
        print("Windows detected. Skipping platform-specific dependencies.")
    else:
        print(f"{current_os} detected. No additional dependencies required.")

def setup_environment():
    """Main setup logic."""
    print("Starting setup process...")

    # Detect OS
    current_os = platform.system()
    print(f"Detected platform: {current_os}")

    # Offer to create a virtual environment
    use_env = input("Do you want to create and install the virtual environment? (y/n): ").strip().lower()
    if use_env == "y":
        pip_path = create_virtual_env()
        install_requirements(pip_path=pip_path)
    else:
        print("Abort Setup!!!")
        sys.exit()

    # Platform-specific setup
    check_platform_dependencies()

    # On Linux, invoke shell script if needed
    if current_os == "Linux":
        print("Running additional Linux-specific setup...")
        run_command(["bash", "setup.sh"])

    print("Setup complete. You can now run the application.")

if __name__ == "__main__":
    setup_environment()

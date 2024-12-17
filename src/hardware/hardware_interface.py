import platform
import os
#from src.hardware.raspberry_pi import RaspberryPiHardware
from src.hardware.basic_hardware import BasicHardware


def detect_environment():
    os_name = platform.system()
    if os_name == "Linux":
        # Check if it's a Raspberry Pi
        if os.path.exists("/sys/firmware/devicetree/base/model"):
            with open("/sys/firmware/devicetree/base/model", "r") as f:
                model = f.read().lower()
                if "raspberry pi" in model:
                    return "raspberry_pi"
        return "linux"
    elif os_name == "Windows":
        return "windows"
    else:
        return "unknown"
    
def get_hardware_interface(env):
    if env == "raspberry_pi":
        return RaspberryPiHardware()
    else:
        return BasicHardware()



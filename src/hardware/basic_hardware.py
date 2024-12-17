from hardware.hardware_interface import HardwareInterface

class BasicHardware(HardwareInterface):
    def setup(self):
        print("Basic hardware setup (keyboard and console).")

    def cleanup(self):
        print("Basic hardware cleanup.")

    def read_input(self):
        return input("Enter your action: ")

    def trigger_output(self, output):
        print(f"Output triggered: {output}")

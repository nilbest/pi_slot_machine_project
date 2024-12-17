from src.hardware.hardware_interface import detect_environment, get_hardware_interface

def main():
    env = detect_environment()
    hardware = get_hardware_interface(env)
    
    # Setup hardware
    hardware.setup()
    
    try:
        # Game loop
        while True:
            action = hardware.read_input()
            if action.lower() == "quit":
                print("Exiting the game.")
                break
            hardware.trigger_output(f"Action received: {action}")
    finally:
        hardware.cleanup()

if __name__ == "__main__":
    
    main()

# Pi Slot Machine Project

Welcome to the Pi Slot Machine project! This project is based on the original Bfruit slot machine simulator, which has been modified to create a fun and customizable slot machine experience on the Raspberry Pi. The goal is to adjust the existing code to fit unique hardware setups, user preferences, and add new features.

Whether you're using it for a project, a fun gaming experience, or something more advanced, this project allows for easy customization of the gameplay mechanics, visuals, and more!

## Table of Contents
- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## About
This project is a Raspberry Pi-based slot machine simulator. It started as a modification of [Bfruit](https://sourceforge.net/projects/bfruit/), a fruit machine game written in Python. We're adjusting the existing code to build a fun, engaging, and interactive slot machine experience that can be controlled with buttons, a display, and other custom hardware.

## Features
- **Customizable Themes:** Modify the fruit images, symbols, and sounds to create a personalized slot machine experience.
- **Interactive Gameplay:** Play using buttons connected to the Raspberry Pi, mimicking the experience of a real slot machine.
- **RNG Engine:** A robust Random Number Generator (RNG) for generating random slot results.
- **Multiplayer Support:** Modify the game logic to support multiple players.
- **Extended Payout System:** Adjust the payout calculations based on winning combinations and bet amounts.
- **Raspberry Pi Friendly:** Optimized for use with a Raspberry Pi and compatible peripherals like buttons and LED displays.

## Requirements
Before getting started, make sure you have the following:
- **Raspberry Pi (any model)** with Raspbian OS installed.
- **Python 3** (recommended version: 3.7+).
- **GPIO buttons** (or any other input mechanism such as a joystick or touchpad).
- **Display** (HDMI or other compatible display, could be a small LCD or touchscreen).
- **Additional hardware** like a button matrix or other gaming peripherals (optional).
- **Pygame library** for rendering graphics and handling inputs. You can install it using `pip`:
  ```bash
  pip install pygame
  ```
## Installation
1. Clone the Repository: Clone this repository to your Raspberry Pi or local machine.
  ```bash
  git clone https://github.com/your-username/pi-slot-machine.git
  cd pi-slot-machine
  ```
2. Install Dependencies: Install the required libraries for the project:
   pip install -r requirements.txt
3. Configure Hardware: Set up your Raspberry Pi with the desired hardware inputs, such as buttons, and connect your display.
4. Run the Game: After installing dependencies and setting up your hardware, you can run the game using:
  ```bash
  python slot_machine.py
  ```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and create a pull request. We welcome improvements, bug fixes, and new features!

### Steps to Contribute:
1. Fork the repository.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/pi-slot-machine.git
3. Make your changes and commit them:
  ```bash
  git commit -m "Description of your changes"
  ```
4. Push your changes to your fork:
```bash
git push origin main
```
5. Create a pull request from your fork to the original repository.


## License

This project is licensed under the **GNU General Public License v2.0 (GPLv2)**. You can freely modify and redistribute the code as long as you follow the terms of the GPLv2.

For more details, see the full [LICENSE](LICENSE) file.

This project is a modification of the original [Bfruit Slot Machine](https://sourceforge.net/projects/bfruit/) which was licensed under the GPLv2. The modifications made here follow the same licensing terms.

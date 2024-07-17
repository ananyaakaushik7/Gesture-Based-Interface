# Gesture-Based-Interface
A Gesture-based interface developed using Python and OpenCV for HackWestTX 2023


# Hand Gesture Control - README

## Overview
This Python script uses computer vision and hand gesture recognition to control various aspects of your computer, including screen brightness and volume. It leverages the `cvzone` and `screen_brightness_control` libraries to achieve this functionality. You can use it to perform actions like changing screen brightness, adjusting volume, and switching tabs with hand gestures.

## Prerequisites
Before using this script, make sure you have the following installed:

- Python 3.7 or higher
- OpenCV (`cv2`) library
- `pyautogui` library
- `screen_brightness_control` library (install using `pip install screen-brightness-control`)
- `cvzone` library (you can install it using `pip install cvzone`)
- `pycaw` library (install using `pip install pycaw`)
- `comtypes` library (install using `pip install comtypes`)

## Usage
1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the folder where you've saved the code.

3. Run the following command to start the script:


4. The script will open your computer's camera and start capturing video. Make sure your hand is visible in the camera's view.

5. Perform the following hand gestures to control your computer:

- **Right Hand Gestures:**
  - Show all open windows: Show an open hand with all fingers extended. Then close and open it.
  - Move left: Close your thumb finger and extend the other fingers.
  - Move right: Close your pinky finger and extend the other fingers.
  - Select: Open your index and middle fingers while keeping the rest closed.
  - Quit: Open your ring and pinky fingers while keeping the rest close.

- **Left-Hand Gestures (For Screen Brightness Control):**
  - Move your left hand's fingers closer to or farther to control screen brightness. Bring your thumb and index finger closer to adjust brightness down and move them apart to adjust the brightness up.

- **Right Hand Gestures (For Volume Control):**
  - Move your Right hand's fingers closer to or farther to control volume. Bring your thumb and index finger closer to decrease volume and move them apart to increase volume.

6. To exit the script, press 'q' in the terminal where the script is running.

## Configuration
You can adjust various parameters in the script to customize its behavior, such as the gesture detection threshold, camera resolution, and more. Refer to the code comments for details on how to modify these parameters.

## Troubleshooting
If you encounter any issues or have questions, please feel free to reach out for assistance.

## Credits
This script was created by Saheel.Faisal , Shravani.Koli , Albin.Thomas and Ananya kaushik as a demonstration of hand gesture control using Python. It uses the `cvzone`, `pyautogui`, `screen_brightness_control`, `pycaw`, and `comtypes` libraries. 

Enjoy controlling your computer with hand gestures!

## Resources 
youtube video that we used to learn about : https://youtu.be/9iEPzbG-xLE?si=BcNGkHYyhX79sHuX


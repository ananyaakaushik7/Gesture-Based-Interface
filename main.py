import cv2
import numpy as np
import pyautogui
import time
import screen_brightness_control as sbc
from cvzone.HandTrackingModule import HandDetector
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER

# Initialising Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

# constants
width = 1280
height = 720
gesture_threshold = 360
cap = cv2.VideoCapture(0)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume_range = volume.GetVolumeRange()
min_vol = volume_range[0]
max_vol = volume_range[1]
volume.SetMasterVolumeLevel(0, None)


# Main loop
while True:
    ret, img = cap.read()
    img = cv2.resize(img, (width, height))
    hands, img = detector.findHands(img)
    # cv2.line(img, (0, gesture_threshold), (width, gesture_threshold), (0, 255, 0), 10)

    if hands:
        # Detecting fingers
        hand1 = hands[0]
        fingers = detector.fingersUp(hand1)
        cx, cy = hand1['center']
        lmList1 = hand1['lmList']

        if cy <= gesture_threshold:
            if hand1['type'] == "Right":
                if fingers == [0, 0, 0, 0, 0]:
                    pyautogui.hotkey('win', 'tab')
                    time.sleep(0.4)

                # left
                elif fingers == [0, 1, 1, 1, 1]:
                    pyautogui.press('left')
                    time.sleep(.4)

                # right
                elif fingers == [1, 1, 1, 1, 0]:
                    pyautogui.press('right')
                    time.sleep(.4)

                elif fingers == [0, 1, 1, 0, 0]:
                    pyautogui.press('space')
                    time.sleep(1)

                elif fingers == [0, 0, 1, 1, 0]:
                    pyautogui.press('q')
                    time.sleep(0.2)

                length, info, img = detector.findDistance(lmList1[4][0:2], lmList1[8][0:2], img, color=(255, 0, 255),
                                                          scale=10)
                vol = np.interp(length, [20, 160], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(vol, None)

            else:
                # Calculate distance between specific landmarks on the first hand and draw it on the image
                length, info, img = detector.findDistance(lmList1[4][0:2], lmList1[8][0:2], img, color=(255, 0, 255),
                                                          scale=10)
                brightness_level = np.interp(length, [20, 160], [0, 100])
                sbc.set_brightness(int(brightness_level))


    cv2.imshow("Hand Gesture Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

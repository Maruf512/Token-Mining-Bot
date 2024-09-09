from ZenCoin import zenCoin_Click_Location
from locateText import Get_Text
import pyautogui, time

# variables
counter = 0

def OpenWindow():
    # show somesorts of worning
    pyautogui.confirm("Energy has been fully Charged on ZecCoin. shall i proceed?")
    # Open TaskBar
    pyautogui.press("win")
    time.sleep(0.5)
    # take TaskBar's Snapshot and search for Telegram
    location = zenCoin_Click_Location(tempImage="./images/telegram.png", screenShotArea=[0,1032,1760,1079])
    # Open ZenCoin
    if location != False:
        pyautogui.moveTo(location[0] + 10, location[1] + 1040)
        pyautogui.click()
        time.sleep(0.2)
    else:
        print("Start Telegram")


OpenWindow()

# Main Loop
while True:
    # Search for ZenCoin in window by a specific simble
    location = zenCoin_Click_Location(tempImage="./images/ThunderBoalt.png", screenShotArea="Screen")
    print(location)
    if location:
        # take a pictur of zenCoin energy and scan text from it
        image_data = Get_Text(location[0], location[1])
        print("Rescanning====")
        try:
            processedData = image_data[0].split('/')
            if int(processedData[0]) > 50:
                pyautogui.moveTo(location[0] + 180, location[1] - 50)
                for i in range(100):
                    pyautogui.click()
                    print(f"Countdown: {100-i} Stat: {image_data[0]}")
            else:
                print("Energy is below 50. Entering Sleeping mode.")
                time.sleep(1200)

        except TypeError:
            counter += 1
            if counter > 5:
                print("Entering Sleeping Mode.")
                pyautogui.confirm("Done. Entering sleeping Mode.")
                counter = 0
                time.sleep(1200)
                OpenWindow()

    else:
        print("Coulden't detect ZenCoin Window.")
        break

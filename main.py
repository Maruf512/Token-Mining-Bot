from ZenCoin import zenCoin_Click_Location


while True:
    location = zenCoin_Click_Location()
    if location:
        print(location)
    else:
        print("Coulden't detect ZenCoin Window.")
        break


# pyautogui.moveTo(max_loc[0] + 180, max_loc[1] - 50)
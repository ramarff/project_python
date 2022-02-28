import pyautogui
import time

hewan = open("hewan.txt", "r")

position = pyautogui.position()
# pesan="tes program heheh"
for i in hewan:
    pyautogui.click(position.x, position.y)
    pyautogui.typewrite(f"Amim kaya {i}")
    pyautogui.typewrite(["enter"])
    # print(pesan)
    time.sleep(5)

import pyautogui
import keyboard
name = input("Wprowadz nazwe przedmiotu: ")

count = 1

print("Wpisz '$' na klawiaturze aby wykonać ss:")

while True:
    if keyboard.is_pressed('$'):
        screenShot = pyautogui.screenshot()
        screenShot.save(f'{name}-{count}.png')
        count += 1
        print("SS saved")
import pyautogui as p
import time as t


print("Starting the Game Now")
t.sleep(5)
p.press('space')
print("Move the mouse to the position")




while True:
	a,b=p.position()
	x=p.pixelMatchesColor(a,b,(83, 83, 83))
	if x:
		#Gray Color and press the button
		p.press('space')

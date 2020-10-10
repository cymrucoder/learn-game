import os
import time
import sys
import pyautogui
import math

screenX = 2560
screenY = 1440
halfX = screenX / 2
halfY = screenY / 2

minimapLeft = 2234
minimapRight = 2362
minimapBottom = 260
minimapTop = 190

minimapWidth = minimapRight - minimapLeft
minimapHeight = minimapBottom - minimapTop

def moveMouseToAngle(angle):
	xToMoveTo = halfX + (math.cos(math.radians(angle)) * 40)
	yToMoveTo = halfY - (math.sin(math.radians(angle)) * 40)
	pyautogui.moveTo(xToMoveTo, yToMoveTo)	

def findMinimapPosition():
	imMinimap = pyautogui.screenshot('minimap.png', region=(minimapLeft, minimapTop, minimapWidth, minimapHeight))
	minimapDot = pyautogui.locate('minimapbluedot.png', imMinimap, grayscale=False)
	return minimapDot

def inferScreenPosition():
	minimapDot = findMinimapPosition()
	minimapX = minimapDot.left + (minimapDot.width / 2)
	minimapY = minimapDot.top + (minimapDot.height / 2)
	fractionX = minimapX / minimapWidth
	fractionY = minimapY / minimapHeight
	return [screenX * fractionX, screenY * fractionY]

time.sleep(5)

pyautogui.keyDown('a')
time.sleep(0.9)
#pyautogui.keyUp('a')

print(inferScreenPosition())

moveMouseToAngle(300)

pyautogui.keyDown('space')
pyautogui.click()
time.sleep(0.5)
pyautogui.keyUp('space')

moveMouseToAngle(300)
pyautogui.click()
time.sleep(1.0)

moveMouseToAngle(300)
pyautogui.click()
time.sleep(1.0)

print(inferScreenPosition())

moveMouseToAngle(300)
pyautogui.click()
time.sleep(1.0)

moveMouseToAngle(300)
pyautogui.click()
time.sleep(1.0)

pyautogui.keyUp('a')

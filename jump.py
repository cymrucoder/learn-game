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

minimapXMargin = 2276 - minimapLeft
minimapYMargin = minimapBottom - 245

minimapWidth = minimapRight - minimapLeft
minimapHeight = minimapBottom - minimapTop

minimapPreviewWidth = minimapWidth - (minimapXMargin)
minimapPreviewHeight = minimapHeight - (minimapYMargin)

def clickMouseAtAngle(angle, playerPosition=[halfX, halfY]):
	xToMoveTo = playerPosition[0] + (math.cos(math.radians(angle)) * 40)
	yToMoveTo = playerPosition[1] - (math.sin(math.radians(angle)) * 40)
	pyautogui.click(x=xToMoveTo, y=yToMoveTo)

def moveMouseToAngle(angle, playerPosition=[halfX, halfY]):
	xToMoveTo = playerPosition[0] + (math.cos(math.radians(angle)) * 40)
	yToMoveTo = playerPosition[1] - (math.sin(math.radians(angle)) * 40)
	pyautogui.moveTo(xToMoveTo, yToMoveTo)

def findMinimapPosition():
	imMinimap = pyautogui.screenshot(region=(minimapLeft + minimapXMargin, minimapTop + minimapYMargin, minimapPreviewWidth, minimapPreviewHeight))
	minimapDot = pyautogui.locate('minimapbluedot.png', imMinimap, grayscale=False)
	return minimapDot

def inferScreenPosition():
	minimapDot = findMinimapPosition()
	minimapX = minimapXMargin + (minimapDot.left + (minimapDot.width / 2))
	minimapY = minimapYMargin + (minimapDot.top + (minimapDot.height / 2))
	fractionX = minimapX / minimapWidth
	fractionY = minimapY / minimapHeight
	return [screenX * fractionX, screenY * fractionY]

# Click the mouse at x position along a fixed horizontal line near the bottom of the screen
# This is to mostly replace the click at angle stuff that doesn't run quick enough
def clickMouseAtX(x):
	xToMoveTo = x
	yToMoveTo = screenY - 200
	pyautogui.click(x=xToMoveTo, y=yToMoveTo)

time.sleep(5)

pyautogui.keyDown('a')
time.sleep(0.7)

screenPosition = inferScreenPosition()
shootingAngle = 300
moveMouseToAngle(shootingAngle, playerPosition=screenPosition)
pyautogui.keyDown('space')
pyautogui.click()
time.sleep(0.2)
pyautogui.keyUp('space')

clickMouseAtX(screenX * 0.75)
time.sleep(1)

clickMouseAtX(screenX * 0.66)
time.sleep(1)

clickMouseAtX(screenX * 0.50)
time.sleep(1)

pyautogui.keyUp('a')

time.sleep(1)

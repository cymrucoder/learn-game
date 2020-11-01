import os
import time
import sys
import pyautogui
import math

class Node:
	def __init__(self, weight, bias):
		self.weight = weight
		self.bias = bias

	def calculate(self, input):
		return (input * self.weight) + self.bias

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

numberOfClicks = 0
node1 = Node((screenX - 1900) / 7, 1950)

pyautogui.keyDown('a')
time.sleep(1.1)

firstClickX = node1.calculate(numberOfClicks)
pyautogui.keyDown('space')
clickMouseAtX(firstClickX)
numberOfClicks = numberOfClicks + 1
time.sleep(0.25)
pyautogui.keyUp('space')

clickMouseAtX(node1.calculate(numberOfClicks))
numberOfClicks = numberOfClicks + 1
time.sleep(0.25)

clickMouseAtX(node1.calculate(numberOfClicks))
numberOfClicks = numberOfClicks + 1
time.sleep(0.25)

clickMouseAtX(node1.calculate(numberOfClicks))
numberOfClicks = numberOfClicks + 1
time.sleep(0.25)

clickMouseAtX(node1.calculate(numberOfClicks))
numberOfClicks = numberOfClicks + 1
time.sleep(0.25)

pyautogui.keyUp('a')

time.sleep(1)

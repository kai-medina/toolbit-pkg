# ToolBit v.0.1
# Author: Kai Medina (info@vasebit.com)

# Contributer: Lifeng Ding, Vocal Lee

import setuptools
import os
import math
import time
import random
import socket
from urllib import request, error
from datetime import datetime

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="toolbit-pkg-vasebit",
  version="0.0.1",
  author="Kai Medina",
  author_email="info@vasebit.com",
  description="A small project that allows you to do a lot.",
  long_description="VaseBit has published ToolBit! Which is a small project that allows you to do a lot. You can check this project out in our page.",
  long_description_content_type="text/markdown",
  url="https://vasebit.com",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)

def getBiggerNumber(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "error"

def getSmallerNumber(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return "error"

def systemShutdown(time):
    os.system("shutdown -s -t " + time)

def getTwiceEquationSolution(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return "noRealSolution"
    else:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1, root2

def getOnceEquationSolution(a, b):
    if a == 0:
        return "error"
    else:
        root = -b / a
        return root

def getWebsiteRes(url, format="utf-8"):
    try:
        with request.urlopen(url) as response:
            websiteRes = response.read().decode(format)
            return websiteRes
    except error.URLError as e:
        print(f"error: {e}")
        return None

def downloadFile(url, savePath):
    try:
        with request.urlopen(url) as response:
            fileContent = response.read()

            with open(savePath, 'wb') as file:
                file.write(fileContent)

            print(f"successfully saved file at {savePath}")

    except error.URLError as e:
            print(f"error: {e}")

def getABS(num):
    if num < 0:
        return -1 * num
    else:
        return num

def readFile(filePath):
    try:
        with open(filePath, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"We did not found '{filePath}'"
    except Exception as e:
        return f"error: {str(e)}"


def writeFile(filePath, content):
    try:
        with open(filePath, 'w') as file:
            file.write(content)
        return f"Successfully wrote files on '{filePath}'"
    except Exception as e:
        return f"error: {str(e)}"

def getCurrentTime():
    return datetime.now()

def timestampToDatetime(timestamp, format="%Y-%m-%d %H:%M:%S"):
    try:
        datetime_object = datetime.fromtimestamp(timestamp)
        formatted_datetime = datetime_object.strftime(format)
        return formatted_datetime
    except Exception as e:
        print(f"error: {str(e)}")
        return None

def calculateBMI(weight_kg, height_m):
    try:
        bmi = weight_kg / (height_m ** 2)
        return bmi
    except ZeroDivisionError:
        print("error: height cannot be 0.")
        return None
    except Exception as e:
        print(f"error: {str(e)}")
        return None

def convertValue(value, from_unit, to_unit):
    units = {
        'length': {
            'km': 1000,
            'm': 1,
            'dm': 0.1,
            'cm': 0.01,
            'mm': 0.001,
        },
        'time': {
            's': 1,
            'min': 60,
            'h': 3600,
            'd': 86400,
        },
        'speed': {
            'm/s': 1,
            'km/h': 3.6,
            'mi/h': 2.23694,
        }
    }

    try:
        unit_type = None
        for ut, unit_dict in units.items():
            if from_unit in unit_dict and to_unit in unit_dict:
                unit_type = ut
                break

        if unit_type is None:
            raise ValueError("unsupported unit")

        conversion_factor = units[unit_type][from_unit] / units[unit_type][to_unit]
        converted_value = value * conversion_factor
        return converted_value

    except Exception as e:
        print(f"error: {str(e)}")
        return None

def getBiggestNumInArray(arr):
    if not arr:
        return None
    maxNum = max(arr)

    return maxNum

def getSmalleestNumInArray(arr):
    if not arr:
        return None
    minNum = min(arr)

    return minNum

def findKeywordInArray(arr, keyword, fuzzySearch=0):
    # Note: This function returns a bool.
    if not arr or not keyword:
        return False

    for item in arr:
        if fuzzySearch == 0:
            if item == keyword:
                return True
        elif fuzzySearch == 1:
            if keyword in item:
                return True

    return False

def calculateDelta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

# ================= Snake Game ================= #

def snakeGame():
    # settings
    width = 20
    height = 10
    snake = [(2, 2)]
    direction = (1, 0)
    food = generate_food(width, height, snake)
    score = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print_game_board(width, height, snake, food, score)

        # get user's input
        key = input("Control the snake by using the arrow key. Click [enter] to continue")

        # deal with user's input
        direction = handle_input(key, direction)

        # move snake
        snake, ate_food = move_snake(snake, direction, food)

        # if snake eats the food
        if ate_food:
            score += 1
            food = generate_food(width, height, snake)

        # show the result
        if game_over(snake, width, height):
            print("Well done! Your score: ", score)
            break

        time.sleep(0.2)  # Game speed

def print_game_board(width, height, snake, food, score):
    for y in range(height):
        for x in range(width):
            if (x, y) in snake:
                print("O", end=" ")
            elif (x, y) == food:
                print("F", end=" ")
            else:
                print(".", end=" ")
        print()
    print("得分:", score)

def generate_food(width, height, snake):
    while True:
        food = (random.randint(0, width-1), random.randint(0, height-1))
        if food not in snake:
            return food

def handle_input(key, direction):
    if key == "w" and direction != (0, 1):
        return (0, -1)
    elif key == "s" and direction != (0, -1):
        return (0, 1)
    elif key == "a" and direction != (1, 0):
        return (-1, 0)
    elif key == "d" and direction != (-1, 0):
        return (1, 0)
    else:
        return direction

def move_snake(snake, direction, food):
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake = [head] + snake

    ate_food = False
    if head == food:
        ate_food = True
    else:
        snake = snake[:-1]

    return snake, ate_food

def game_over(snake, width, height):
    head = snake[0]
    return (
        head[0] < 0 or head[0] >= width or
        head[1] < 0 or head[1] >= height or
        len(snake) != len(set(snake))
    )

# ================= Snake Game ================= #

def getHostname():
    hostname = socket.gethostname()
    return hostname


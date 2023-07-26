from tkinter import *
import random

height = 700
width = 700
speed = 50
space = 50 
bodyParts = 3
snakeColor = "#00FF00"
foodColor = "#FF0000"
bgColor = "#000000"

class Snake:
    def __init__(self):
        self.body_size = bodyParts
        self.coordinates = []
        self.squares = []

        for i in range(0, bodyParts):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + space, y + space, fill=snakeColor, tag="Snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (width/space)-1) * space
        y = random.randint(0, (height/space)-1) * space

        self.coordinates = [x, y]
        canvas.create_rectangle(x,y,x+space,y+space, fill=foodColor, tag="Food")

def nextTurn(snake, food):
    x , y = snake.coordinates[0]
    if direction == "up":
        y -= space
    elif direction == "down":
        y += space
    elif direction == "left":
        x -= space
    elif direction == "right":
        x += space 

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + space, y + space, fill=snakeColor)
    snake.squares.insert(0, square)
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]
 
    window.after(speed, nextTurn, snake, food)

def changeDirection(newDirection):
    pass

def checkCollisions():
    pass

def gameOver():
    pass

window = Tk()
window.title("Snake") 
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text=f"Score: {score}", font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=bgColor, height=height, width=width)
canvas.pack()

window.update()

windowWidth = window.winfo_width()
windowHeight = window.winfo_height()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2) - (windowWidth/2))
y = int((screenHeight/2) - (windowHeight/2))

window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

window.bind('<Left>', lambda event: changeDirection('left'))
 
snake = Snake()
food = Food()

nextTurn(snake, food)

window.mainloop()
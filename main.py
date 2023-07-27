from tkinter import *
import random

height = 700
width = 700
speed = 100
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

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score+=1
        label.config(text=f"Score: {score}")
        canvas.delete("Food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
 
    if checkCollisions(snake):
        gameOver()
    else:
        window.after(speed, nextTurn, snake, food)

def changeDirection(newDirection):
    global direction

    if newDirection == "left":
        if direction != "right":
            direction = newDirection
    elif newDirection == "right":
        if direction != "left":
            direction = newDirection
    elif newDirection == "up":
        if direction != "down":
            direction = newDirection
    elif newDirection == "down":
        if direction != "up":
            direction = newDirection

def checkCollisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= width:
        print("Game Over")
        return True
    elif y < 0 or y >= height:
        print("Game Over")
        return True
    
    for i in snake.coordinates[1:]:
        if x == i[0] and y == i[1]:
            return True
    return False

def gameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas", 70), text="GAME OVER", fill="red")
    reset = Button(window, text="Try Again", width=50, height=10, command=tryAgain)
    reset.place(x=(windowWidth/2)-(windowWidth/4), y=500)

def tryAgain():
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

window.bind("<Left>", lambda event: changeDirection("left"))
window.bind("<Right>", lambda event: changeDirection("right"))
window.bind("<Up>", lambda event: changeDirection("up"))
window.bind("<Down>", lambda event: changeDirection("down"))
 
snake = Snake()
food = Food()

nextTurn(snake, food)

window.mainloop()
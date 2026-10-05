from tkinter import Canvas, Tk
import random
import time

#The object of the tkinter class 
tk = Tk()
tk.title("The bouncing ball")
tk.wm_attributes("-transparentcolor", "green")
tk.wm_resizable(False, False)

#The canvas
canvas = Canvas(tk, width = 500, height = 400, bg = "azure", borderwidth = 3, relief="sunken", highlightthickness = 0, highlightbackground= "green", highlightcolor= "blue")
canvas.pack(expand=True, anchor="center")
tk.update()


#The Ball class
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 235, 150) #Moves the ball to the middle
        starts = [-5, -4,-3, -2, -1, 1, 2, 3, 4, 5]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = starts[-1]
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.hit_bottom = False
    
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def draw(self): #The movement of the ball starts = [-5, -4,-3, -2, -1, 1, 2, 3, 4, 5] #A set of random speeds
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) #Co-ordinates of the ball, provided by Canvas.coords
        if pos[1] <= 0: #The top rebound
            self.y = random.choice([1, 2, 3, 4, 5])
        if pos[3] >= self.canvas_height: #The bottom rebound
            self.y = random.choice([-1, -2, -3, -4, -5])
        if pos[0] <= 0: #The left rebound
            self.x = random.choice([1, 2, 3, 4, 5])
        if pos[2] >= self.canvas_width: #The right rebound
            self.x = random.choice([-1, -2, -3, -4, -5])
        if self.hit_paddle(pos) == True:
            self.y = -5
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(
            0, 0, 100, 10, fill=color
        )
        self.canvas.move(self.id, 200, 320)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.x = 0
        self.y = 0
        canvas.bind_all('<KeyPress-Up>', self.turn_up)
        canvas.bind_all('<KeyPress-Down>', self.turn_down)
        canvas.bind_all('<KeyPress-Left>', self.turn_left)
        canvas.bind_all('<KeyPress-Right>', self.turn_right)
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        #Left boundary
        if pos[0] <= 0:
            self.x = 0
        #Right boundary
        if pos[2] >= self.canvas_width:
            self.x = 0
        #Top boundary
        if pos[1] <= 318:
            self.y = 0
        #Bottom boundary
        if pos[3] >= self.canvas_height:
            self.y = 0
    def turn_left(self, event):
        self.x = -3
    def turn_right(self, event):
        self.x = 3
    def turn_up(self, event):
        self.y = -1
    def turn_down(self, event):
        self.y = 1


def game_over_animation():
    size = 10
    text = canvas.create_text(
        250, 200,
        text="GAME OVER",
        font=("Consolas", size, "bold"),
        fill="red"
    )
    def enlarge(size):
            if size <= 50:
                canvas.itemconfig(text, font=("Consolas", size, "bold"))
                canvas.after(100, enlarge, size + 2)
    enlarge(size)

paddle = Paddle(canvas, "Red")
ball = Ball(canvas, paddle, "black")

while True:
    
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if ball.hit_bottom == True:
        game_over_text = canvas.create_text(
            250, 200,
            text="GAME OVER!",
            font=("Arial", 40),
            fill="red"
        )
        tk.update()
        time.sleep(2)
        break
    
    print(canvas.coords(ball.id), canvas.coords(paddle.id))

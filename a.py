# Step 1 set-up turtle and tkinter
import tkinter as tk
import turtle

def display_heart():
    # Initialize turtle
    window = turtle.Screen()
    window.bgcolor("black")
    window.setup(width=800, height=600)
    window.title("My Love")
    love_heart = turtle.Turtle()
    love_heart.shape("turtle")
    love_heart.color("red")
    love_heart.speed(2)

    # Step 2 Draw the heart shape with a larger line width
    love_heart.pensize(5)
    love_heart.begin_fill()
    love_heart.left(140)
    love_heart.forward(180)
    love_heart.circle(-90, 200)
    love_heart.left(120)
    love_heart.circle(-90, 200)
    love_heart.forward(180)
    love_heart.end_fill()

    # Step 3 Write "I Love You" in the center of the heart
    love_heart.up()
    love_heart.goto(0, -120)
    love_heart.color("red")
    love_heart.write("I Love You", align="center", font=("Courier", 34, "bold"))

    # Hide turtle and display heart until the window is closed
    love_heart.hideturtle()
    turtle.done()

def propose():
    root.destroy()  # Close the GUI window
    display_heart()

def reject():
    root.destroy()  # Close the GUI window
    message = "It's okay, we will be best friends forever."
    tk.messagebox.showinfo("Love Proposal", message)

def create_gui():
    global root
    root = tk.Tk()
    root.title("Love Proposal")

    # Step 4 Set the window size and position it in the center of the screen
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Step 5 Create back-up for rejection
    label = tk.Label(root, text="I love you just the way you are, \nI want to grow old with you from this day, \nWill you marry me?", font=("Arial", 14, "bold italic"))
    label.pack(pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack()

    yes_button = tk.Button(button_frame, text="Yes", command=propose)
    yes_button.pack(side=tk.LEFT, padx=10)

    no_button = tk.Button(button_frame, text="No", command=reject)
    no_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

create_gui() 

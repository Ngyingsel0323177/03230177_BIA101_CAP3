
#https://github.com/Ngyingsel0323177/03230177_BIA101_CAP3
#NGYINGSEL NYINGZER RINCHEN 
#BBIB
#03230177
#REFERENCE 
#https://www.w3schools.com/python/
#https://www.geeksforgeeks.org/python-time-module/
#https://www.geeksforgeeks.org/python-gui-tkinter/
#Solution:<488206>
import time
import tkinter as tk

def calculate_answer(file_name):
    total = 0
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            first_digit = next((char for char in line if char.isdigit()), None)
            last_digit = next((char for char in reversed(line) if char.isdigit()), None)
            if first_digit and last_digit:
                two_digit_number = int(first_digit + last_digit)
                total += two_digit_number
    return total

file_name = '177.txt'
answer = calculate_answer(file_name)

root = tk.Tk()
root.geometry("400x300")  # Set the window size to 400x300 pixels

label = tk.Label(root, text=f"Your answer is: {answer}")
label.pack()

# Add a comment "The screen will be closed after 5 minutes"
comment_label = tk.Label(root, text="The screen will be closed after 5 minutes")
comment_label.pack()

def countdown(count):
    if count > 0:
        label.config(text=f"Your answer is: {answer} | Time remaining: {count} seconds")
        root.after(1000, countdown, count-1)
    else:
        root.destroy()

countdown(300)  # 300 seconds = 5 minutes

root.mainloop()
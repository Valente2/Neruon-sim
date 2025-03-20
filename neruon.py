import tkinter as tk
from tkinter import simpledialog

# Create the main application window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show an input dialog
count = simpledialog.askstring("Input", "Enter the amount of denderites: ",)
count = int(count)
vol = [0] * count
w = [0] * count
ans = [0] * count

for x in range(count):
    vol[x] = simpledialog.askstring("Input", "Enter the voltage of denderite")
    vol[x] = float(vol[x])
    w[x] = simpledialog.askstring("Input", "Enter the weight of denderite")
    w[x] = float(w[x])
    x = x + 1
b = simpledialog.askstring("Input", "Enter the bias: ")
b = float(b)
#math time

for x in range(count): #This is for the multiplication
    ans[x] = vol[x] * w[x]

total = sum(ans) + b
print("The output voltage of the neruon is", total)

#step function

if total >= -0.055:
    binary = True
if total < -0.055:
    binary = False

question = input("would you like the full data table?(Y/N) ")
if question == "Y" or "y":
    print("Denderite amount", count)
    for x in range(count):
        print("Voltage", x + 1 , vol[x])
    for x in range(count):
        print("Weght", x + 1 , w[x] ) 
    print("Bias:",b)
    print("Binary: ",binary)
    time.sleep(100)
    exit
if question == "N" or "n":
    exit
    
      
    




    
    


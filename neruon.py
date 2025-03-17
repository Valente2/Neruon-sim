import time
count = int(input("enter the dendrite amount"))
binary = False
      
if count <= 0:
    print("Invalid size. Please enter a positive integer.")
    exit
ans = [0] * count 
w = [0] * count #Make an arry of zeros for the weights       
vol = [0] * count  # Create an array of zeros with the specified size
print(f"Enter {count} voltages, one at a time:")
        
    # Keep reading values until the array is filled
for i in range(count):
    element = float(input(f"Voltage {i + 1}: "))
    vol[i] = element  # Assign the element to the array at the specified index
time.sleep(2)

for i in range(count):
    e = float(input(f"Weight {i + 1}: "))
    w[i] = e

time.sleep(3)

b = float(input("enter the bias "))

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
    
      
    




    
    


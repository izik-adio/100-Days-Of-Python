def cans_calc(height,width):
    from math import ceil
    coverage = 5
    cans_needed = (width * height) / coverage
    print(f"You'll need {ceil(cans_needed)} cans of paint")
    
width = float(input("Input Width: "))
height = float(input("Input Height: "))
cans_calc(height,width)
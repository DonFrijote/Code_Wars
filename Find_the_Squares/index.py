"""Problem
Complete the function that takes an odd integer (0 < n < 1000000)
 which is the difference between two consecutive perfect squares, 
 and return these squares as a string in the format "bigger-smaller"

Examples
9  -->  "25-16"
5  -->  "9-4"
7  -->  "16-9"

Other brute force solutions:

def find_squares(num):
    i = 0
    while num != (i+1)**2 - i**2:
        i = i+1
    return f"{(i+1)**2}-{i**2}"

def find_squares(num):
    for i in range(num):
        if num == (i+1)**2 - i**2:
            return f"{(i+1)**2}-{i**2}"
            """

def find_squares(num):
    lower = int((num - 1)/2)
    upper = lower + 1
    return f"{upper**2}-{lower**2}"
    

"""It's pretty straightforward. Your goal is to create a function that
 removes the first and last characters of a string. 
 You're given one parameter, the original string. 
 You don't have to worry with strings with less than two characters.
"""

def remove_char(s):
    split_string = list(s)
    split_string.pop()
    split_string.pop(0)
    done = ''
    return done.join(split_string)

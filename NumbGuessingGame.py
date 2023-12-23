"""
https://www.geeksforgeeks.org/number-guessing-game-in-python/
"""

import math
import random
# Algorithm 

############ User guide Messages #############
input_lbound_msg = "lower bound : "
input_ubound_msg = "upper bound : "
the_range_selected = """
You decided to choose between {} and {}.
Now let the compiler select a number in this range.
You'll try to guess it...
"""
invalid_compiler_exception = "Invalid number selected by the compiler. \nAmine, review the random.randint"
valid_compiler_choice = "Okay the compiler made his choice.\nNow your turn."

############ Result Messages ##################
too_high_msg = "It's too high. Try again !"
too_small_msg = "It's too small. Try again !"
big_congrat_msg = """
Congrats !!!. The compiler randomly chose {} too. 
And you've found it rapidly. What a genius !
"""
small_congrat_msg = """
Good enough. The compiler randomly chose : {} too. 
But you haven't found it very rapidly. Better Luck Next time !
"""
################################################

#1) user input
lbound  = int(input(input_lbound_msg))
ubound  = int(input(input_ubound_msg))
print(the_range_selected.format(lbound,ubound))

#2) Compiler choice
compiler_choice = random.randint(lbound,ubound)
if not compiler_choice in range(lbound,ubound+1):
    raise Exception(invalid_compiler_exception)
else : 
    print(valid_compiler_choice)

#3) Real things 
rg = range(lbound,ubound+1)
i=lbound
while i<=rg[-1]:
    user_guess = int(input("Enter your number here :- " ))
    print("You guessed {} .".format(user_guess))
    if user_guess > compiler_choice:
        print(too_high_msg)
    elif user_guess < compiler_choice:
        print(too_small_msg)
    else:
        if (i <= math.log((ubound-lbound + 1),2)):
            print(big_congrat_msg.format(compiler_choice))
        else : 
            print(small_congrat_msg.format(compiler_choice))
    i+=1


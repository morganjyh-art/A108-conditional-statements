#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
text = input("Enter a number: ")
try:
    int(text)
    print("It is an integer value")
except ValueError:
    print("It is not an integer value")

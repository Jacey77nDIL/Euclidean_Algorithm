# Take the inputs of two numbers to find their GCD
# Divide the larger number by the smaller number and find the remainder.
# Replace the larger number with the smaller number and the smaller number with the remainder.
# Repeat the process until the remainder is zero. The GCD is the last non-zero remainder.
def euclidean_algorithm():
    a = int(input("What is your first number? "))
    b = int(input("What is your second number? "))

    if b > a:
        a, b = b, a #The RHS is evaluated before assignment

    while b > 0:
        remainder = a % b
        a = b
        b = remainder

    print(f'The GCD is {a}')

# Function Call
euclidean_algorithm()

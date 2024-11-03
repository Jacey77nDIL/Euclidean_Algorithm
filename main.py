# Take the inputs of two numbers to find their GCD
# Divide the larger number by the smaller number and find the remainder.
# Replace the larger number with the smaller number and the smaller number with the remainder.
# Repeat the process until the remainder is zero. The GCD is the last non-zero remainder.
def euclidean_algorithm():
    a = int(input("What is your first number? "))
    b = int(input("What is your second number? "))

    if b > a:
        num_1 = b
        num_2 = a
    else:
        num_1 = a
        num_2 = b

    while num_2 > 0:
        remainder = num_1 % num_2
        num_1 = num_2
        num_2 = remainder

    print(num_1)

# Function Call
euclidean_algorithm()
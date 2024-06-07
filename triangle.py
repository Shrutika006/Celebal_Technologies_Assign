# Function to form lower triangular matrix with "*"
def lower(row, col):
    for i in range(0, row):
        for j in range(0, col):
            if i < j:
                print("*", end=" ")
            else:
                print("*", end=" ")
        print("")

# Function to form upper triangular matrix with "*"
def upper(row, col):
    for i in range(0, row):
        for j in range(0, col):
            if i > j:
                print("*", end=" ")
            else:
                print("*", end=" ")
        print("")

# Function to form a pyramid with "*"
def pyramid(height):
    for i in range(height):
        # Print leading spaces
        for j in range(height - i - 1):
            print(" ", end=" ")
        # Print "*" characters
        for k in range(2 * i + 1):
            print("*", end=" ")
        print("")

# Driver Code
row = 5
col = 5
height = 5

print("Lower triangular matrix:")
lower(row, col)

print("\nUpper triangular matrix:")
upper(row, col)

print("\nPyramid:")
pyramid(height)

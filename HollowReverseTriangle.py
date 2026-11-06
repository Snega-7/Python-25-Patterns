n = int(input("Enter the input: "))
for i in range(1, n + 1):
    for j in range(1, i):
        print(" ", end="")
    for j in range(1, 2 * (n - i + 1)):
        if i == 1 or j == 1 or j == 2 * (n - i + 1) - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
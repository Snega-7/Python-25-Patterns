n = int(input("Enter the input: "))
for i in range(0, n + 1):
    for j in range(0, n + 1):
        if i == 0 or j == 0 or i == n or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
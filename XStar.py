n = int(input("Enter the input: "))
for i in range(1, n + 1):
    for j in range(1, i):
        print(" ", end="")
    for j in range(1, n - i + 2):
        if j == 1 or j == n - i + 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
for i in range(1, n):
    for j in range(1, n - i):
        print(" ", end="")
    for j in range(1, i + 2):
        if j == 1 or j == i + 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
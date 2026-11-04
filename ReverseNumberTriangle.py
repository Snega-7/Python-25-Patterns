n = int(input("Enter the input: "))
for i in range(1, n + 1):
    for j in range(1, i):
        print(" ", end="")
    for j in range(i, n + 1):
        print(j, end=" ")
    print()
n = int(input("Diamond için satır sayısını girin: "))

# Üst üçgen
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Alt üçgen
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

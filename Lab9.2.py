A = {2 * i for i in range(1, 101)}
B = {3 * i for i in range(1, 101)}
C = {5 * i for i in range(1, 101)}

all_num = A | B | C

# Кратні 30
divis30 = A & B & C

# Діляться на 15 і не діляться на 2
divis15 = (B & C) - A

# Діляться на 5 і не діляться на 2, 3
divis5 = C - (A | B)

print(sorted(divis15))
print(sorted(divis30))
print(sorted(divis5))
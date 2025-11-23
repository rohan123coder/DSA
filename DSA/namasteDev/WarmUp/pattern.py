# 1
# 12
# 123
# 1234
n=4
for i in range(n):
    row=""
    for j in range(i+1):
        row=row+str(j+1)
    print(row)

# 1 2 3 4
# 1 2 3
# 1 2
# 1
n=4
for i in range(n):
    row = ""
    for j in range(n - i):
        row += str(j + 1)
    print(row)


#     *
#    **
#   ***
#  ****
n=4
for i in range(n):
    row = ""
    for j in range(n - i-1):
        row += " "
    for k in range(i+1):
        row += "*"
    print(row)

#1
#1 0
#1 0 1
#1 0 1 0
n = 4
for i in range(n):
    row = ""
    toggle = 1
    for j in range(i + 1):
        row += str(toggle)
        toggle = 0 if toggle == 1 else 1
    print(row)

#or
n=4
for i in range(n):
    row = ""
    for k in range(i+1):
        if (k+1)%2 == 0:
            row += "0"
        else:
            row += "1"
    print(row)

# 1
# 0 1
# 0 1 0
# 1 0 1 0
n = 4
toggle = 1
for i in range(n):
    row = ""
    for j in range(i + 1):
        row += str(toggle)
        toggle = 0 if toggle == 1 else 1
    print(row)
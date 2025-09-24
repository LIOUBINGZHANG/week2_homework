a = input()
old = input()
new = input()

space = ""

for i in a:
    if i == old:
        space += new
    else:
        space += i

print(space)

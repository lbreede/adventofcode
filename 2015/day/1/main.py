# --- Day 1: Not Quite Lisp ---
# import matplotlib.pyplot as plt

with open("input.txt") as fp:
    txt = fp.read()

# txt = "()())"
f = 0
j = None

# xp = []
# yp = []

for i, x in enumerate(txt):
    match x:
        case "(":
            f += 1
        case ")":
            f -= 1
    if f < 0 and j is None:
        j = i + 1

    # xp.append(i)
    # yp.append(f)

print(f)
print(j)


# plt.plot(xp, yp)
# plt.show()

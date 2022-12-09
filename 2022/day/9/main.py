# --- Day 9: Rope Bridge ---


def move(pos, direction):
    if direction == "U":
        pos[1] += 1
    elif direction == "D":
        pos[1] -= 1
    elif direction == "L":
        pos[0] -= 1
    elif direction == "R":
        pos[0] += 1
    return pos


def is_adjacent(head, tail):
    return all([tail[i] - 1 <= head[i] <= tail[i] + 1 for i in range(2)])


s = [0, 0]
h = s.copy()
t = s.copy()
visited = {tuple(s)}

with open("input.txt") as fp:
    for motion in fp:
        d, n = [int(x) if x.isnumeric() else x for x in motion.rstrip().split()]
        for _ in range(n):
            h = move(h, d)

            # visited.add(tuple(h))

            if is_adjacent(h, t):
                continue

            if h[0] == t[0] or h[1] == t[1]:
                t = move(t, d)
            elif h[0] > t[0] and h[1] > t[1]:
                t[0] += 1
                t[1] += 1
            elif h[0] > t[0] and h[1] < t[1]:
                t[0] += 1
                t[1] -= 1
            elif h[0] < t[0] and h[1] < t[1]:
                t[0] -= 1
                t[1] -= 1
            elif h[0] < t[0] and h[1] > t[1]:
                t[0] -= 1
                t[1] += 1

            visited.add(tuple(t))

print(len(visited))

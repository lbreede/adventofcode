# --- Day 9: Rope Bridge ---
import time

WIDTH = 100
HEIGHT = 100


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


def follow(tail, head, direction):
    if is_adjacent(tail, head):
        return tail
    (tail_x, tail_y), (head_x, head_y) = tail, head
    if tail_x == head_x:
        tail[1] += int(tail_y < head_y) * 2 - 1
    elif tail_y == head_y:
        tail[0] += int(tail_x < head_x) * 2 - 1
    else:
        tail[0] += int(tail_x < head_x) * 2 - 1
        tail[1] += int(tail_y < head_y) * 2 - 1
    return tail


def is_adjacent(tail, head):
    return all([tail[i] - 1 <= head[i] <= tail[i] + 1 for i in range(2)])


def init_grid(visited={}):
    grid = []
    for i in range(-HEIGHT // 2, HEIGHT // 2):
        row = []
        for j in range(-WIDTH // 2, WIDTH // 2):
            if (j, i) not in visited:
                row.append(".")
            else:
                row.append("#")
        grid.append(row)
    return grid


def render_grid(grid):
    print("=" * WIDTH)
    print("\n".join(["".join(row) for row in grid[::-1]]))
    print("=" * WIDTH, "\n")


head = [0, 0]
tail = head.copy()
one = head.copy()
two = head.copy()
three = head.copy()
four = head.copy()
five = head.copy()
six = head.copy()
seven = head.copy()
eight = head.copy()
nine = head.copy()

grid = init_grid()

part_one = {tuple(head)}
part_two = {tuple(head)}


with open("input.txt") as fp:
    for motion in fp:
        d, n = [int(x) if x.isnumeric() else x for x in motion.rstrip().split()]
        for i in range(n):

            head = move(head, d)

            tail = follow(tail, head, d)
            part_one.add(tuple(tail))

            one = follow(one, head, d)
            two = follow(two, one, d)
            three = follow(three, two, d)
            four = follow(four, three, d)
            five = follow(five, four, d)
            six = follow(six, five, d)
            seven = follow(seven, six, d)
            eight = follow(eight, seven, d)
            nine = follow(nine, eight, d)
            part_two.add(tuple(nine))

            # grid = init_grid(visited=part_two)
            # grid[HEIGHT // 2][WIDTH // 2] = "s"
            # grid[nine[1] + HEIGHT // 2][nine[0] + WIDTH // 2] = "9"
            # grid[eight[1] + HEIGHT // 2][eight[0] + WIDTH // 2] = "8"
            # grid[seven[1] + HEIGHT // 2][seven[0] + WIDTH // 2] = "7"
            # grid[six[1] + HEIGHT // 2][six[0] + WIDTH // 2] = "6"
            # grid[five[1] + HEIGHT // 2][five[0] + WIDTH // 2] = "5"
            # grid[four[1] + HEIGHT // 2][four[0] + WIDTH // 2] = "4"
            # grid[three[1] + HEIGHT // 2][three[0] + WIDTH // 2] = "3"
            # grid[two[1] + HEIGHT // 2][two[0] + WIDTH // 2] = "2"
            # grid[one[1] + HEIGHT // 2][one[0] + WIDTH // 2] = "1"
            # grid[head[1] + HEIGHT // 2][head[0] + WIDTH // 2] = "H"
            # render_grid(grid)
            # time.sleep(0.001)


part_one = len(part_one)
part_two = len(part_two)
print("Part 1:", part_one, "\nPart 2:", part_two)

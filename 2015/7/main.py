# --- Day 7: Some Assembly Required ---

MAX = 65535


def circuit_to_python(lst):
    py_list = []
    for L in lst:
        p = L.split(" ")

        if len(p) == 3:
            line = f"{p[2]} = {p[0]}"

        elif len(p) == 4:
            line = f"{p[3]} = ({p[1]} ^ MAX)"

        elif len(p) == 5:
            if p[1] == "AND":
                line = f"{p[4]} = {p[0]} & {p[2]}"  # x AND y -> d   d = x & y

            elif p[1] == "OR":
                line = f"{p[4]} = {p[0]} | {p[2]}"

            elif p[1] == "LSHIFT":
                line = f"{p[4]} = {p[0]} << {p[2]}"

            elif p[1] == "RSHIFT":
                line = f"{p[4]} = {p[0]} >> {p[2]}"

            else:
                pass
        else:
            pass

        py_list.append(line)

    return py_list


with open("example.txt", "r") as fp:
    linelist = fp.read().split("\n")

python_list = circuit_to_python(linelist)
for row in python_list:
    exec(row)

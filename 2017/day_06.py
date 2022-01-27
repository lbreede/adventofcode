# --- Day 6: Memory Reallocation ---

with open("day_06.txt") as f:
    text = f.read()

lst = list(map(int, text.split()))


def redistribute_once(lst):
    max_ = max(lst)
    idx = lst.index(max_)
    lst[idx] = 0

    for i in range(idx + 1, idx + 1 + max_):
        j = i % len(lst)
        lst[j] += 1

    return lst


def redistribute(lst):
    history_entry = "-".join(list(map(str, lst)))
    history = [history_entry]

    while True:
        lst = redistribute_once(lst)
        history_entry = "-".join(list(map(str, lst)))
        if history_entry not in history:
            history.append(history_entry)
        else:
            break
    return len(history)


test = redistribute(lst)
print(test)

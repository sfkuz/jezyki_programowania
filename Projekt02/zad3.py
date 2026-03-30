def josephus_problem(n, k):
    soldiers = list(range(1, n + 1))
    index = 0
    while len(soldiers) > 1:
        index = (index + k - 1) % len(soldiers)
        removed = soldiers.pop(index)

    return soldiers[0]

n_soldiers = 41
k_step = 2

safe_position = josephus_problem(n_soldiers, k_step)
print(f"\nBezpiecznie miejsce: {safe_position}")
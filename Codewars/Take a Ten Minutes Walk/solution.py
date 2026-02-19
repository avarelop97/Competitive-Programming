def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    x = y = 0
    for d in walk:
        if d == 'n':
            y += 1
        elif d == 's':
            y -= 1
        elif d == 'e':
            x += 1
        else:  # 'w'
            x -= 1

    return x == 0 and y == 0
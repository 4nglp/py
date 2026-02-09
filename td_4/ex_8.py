def seq(t):
    if not t: return
    current_seq = [t[0]]
    for i in range(1, len(t)):
        if t[i] > t[i-1]:
            current_seq.append(t[i])
        else:
            print(f"<{', '.join(map(str, current_seq))}>", end=" ; ")
            current_seq = [t[i]]
    print(f"<{', '.join(map(str, current_seq))}>")

T = [1, 2, 5, 3, 12, 25, 13, 8, 4, 7, 24, 28, 32, 11, 14]
seq(T)
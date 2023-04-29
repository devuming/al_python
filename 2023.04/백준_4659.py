mo = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = input()
    if pw == 'end':
        break
    acc_flag = True
    total_mo = 0
    mo_cnt = 0
    ja_cnt = 0
    for i, p in enumerate(pw):
        if i != 0 and pw[i-1] == p and not (p == 'o' or p == 'e'):
            acc_flag = False
            break

        if p in mo:
            ja_cnt = 0
            mo_cnt += 1
            total_mo += 1
            if mo_cnt >= 3:
                acc_flag = False
                break
        else:
            mo_cnt = 0
            ja_cnt += 1
            if ja_cnt >= 3:
                acc_flag = False
                break
    if not acc_flag or total_mo == 0:
        print(f'<{pw}> is not acceptable.')
    else:
        print(f'<{pw}> is acceptable.')
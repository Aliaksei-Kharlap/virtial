



def func2():
    print("from other file")



def friendly_checker():
    spisok = []
    spisok_end = []
    for i in range(200, 301):
        sum = 0
        for a in range(1, i):
            if i % a == 0:
                sum += a

        spisok.append((i, sum))
    for i in spisok:
        i = list(i)
        for b in spisok:
            b = list(b)
            b.append(b.pop(0))
            if i == b:
                spisok_end.append(i)
    return(spisok_end)

print(friendly_checker()) ()) )))))
import sys 
m = int(sys.stdin.readline().rstrip())
s = set()
for _ in range(m):
    temp = sys.stdin.readline().rstrip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()  
    else:
        comm, x = temp[0], int(temp[1])
        if comm == "add":
            s.add(x)
        elif comm == "remove":
            s.discard(x)        # remove는 x가 없을 경우 오류 발생시킴
        elif comm == "check":
            if x in s:
                print(1)
            else:
                print(0)
        elif comm == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)
    
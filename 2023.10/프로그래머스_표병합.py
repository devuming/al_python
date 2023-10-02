
parent = [[[i, j] for j in range(51)] for i in range(51)]
table = [['' for _ in range(51)] for _ in range(51)]


def find_parent(r, c):
    pr, pc = parent[r][c]
    if [pr, pc] != [r, c]:
        parent[r][c] = find_parent(pr, pc)
    return parent[r][c]


def union(r1, c1, r2, c2):
    for i in range(51):
        for j in range(51):
            pi, pj = find_parent(i, j)
            if (pi, pj) == (r2, c2):
                parent[pi][pj] = parent[r1][c1]


def merge(r1, c1, r2, c2):
    r1, c1 = find_parent(r1, c1)
    r2, c2 = find_parent(r2, c2)
    if (r1, c1) == (r2, c2):
        return
    if table[r1][c1] == '':
        union(r2, c2, r1, c1)
    else:
        union(r1, c1, r2, c2)
        table[r2][c2] = ''


def getValue(r, c):
    pr, pc = find_parent(r, c)
    return table[pr][pc]


def unmerge(r, c):
    pr, pc = find_parent(r, c)
    for i in range(51):
        for j in range(51):
            pi, pj = find_parent(i, j)
            if [pi, pj] == [pr, pc]:
                parent[i][j] = [i, j]  # 병합 해제
                table[i][j] = ''


def solution(commands):
    answer = []
    for comm in commands:
        comm = comm.split()
        op = comm[0]
        if op == 'UPDATE':
            if len(comm) == 4:
                r, c = int(comm[1]), int(comm[2])
                pr, pc = find_parent(r, c)
                table[pr][pc] = comm[3]
            else:
                for i in range(51):
                    for j in range(51):
                        if table[i][j] == comm[1]:
                            table[i][j] = comm[2]
        elif op == 'MERGE':
            r1, c1, r2, c2 = int(comm[1]), int(
                comm[2]), int(comm[3]), int(comm[4])
            merge(r1, c1, r2, c2)
        elif op == 'UNMERGE':
            r, c = int(comm[1]), int(comm[2])
            origin_value = getValue(r, c)
            unmerge(r, c)
            table[r][c] = origin_value
        elif op == 'PRINT':
            r, c = int(comm[1]), int(comm[2])
            value = getValue(r, c)
            if value == '':
                answer.append("EMPTY")
            else:
                answer.append(value)
    for i, t in enumerate(table):
        print(f'{i} : {" ".join(t)}')
    return answer


# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant",
#       "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))  # ["EMPTY", "group"]
# print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2",
#       "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))  # ["d", "EMPTY"]

# print(solution(["UPDATE 50 50 hello", "PRINT 50 50", "PRINT 49 49", "MERGE 50 50 49 49", "PRINT 49 49",
#       "UNMERGE 49 49", "PRINT 49 49", "PRINT 50 50", "UPDATE 50 49 hello", "UPDATE hello hi"]))  # [ "hello", "EMPTY", "hello", "hello","EMPTY"]

# ["coffee", "mega", "coffee", "cake", "cake", "cake", "cake"]
# print(solution(["UPDATE 1 1 coffee", "UPDATE 1 2 mega", "PRINT 1 1", "PRINT 1 2", "MERGE 1 1 1 2",
#       "PRINT 1 1", "UPDATE 1 3 cake", "PRINT 1 3", "MERGE 1 3 1 2", "PRINT 1 3", "PRINT 1 2", "PRINT 1 1", "UPDATE 1 1 yummy", "PRINT 1 3", "MERGE 1 4 1 3"]))
# print(solution(["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4",
#       "MERGE 1 1 3 3", "UNMERGE 1 1", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))  # ["A","EMPTY","EMPTY","EMPTY"]
# print(solution(["MERGE 1 1 2 2", "MERGE 1 1 3 3", "UPDATE 3 3 A",
#       "PRINT 1 1", "PRINT 2 2", "PRINT 3 3"]))  # ["A", "A", "A"]

print(solution(["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4",
      "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))  # ["EMPTY", "EMPTY", "A", "EMPTY"]

def solution(wallpaper):
    lux, luy = 50, 50
    rdx, rdy = 0, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i)
                rdy = max(rdy, j)

    return [lux, luy, rdx + 1, rdy + 1]

print(solution([".#...", "..#..", "...#."]))   # [0, 1, 3, 4]
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))   # [1, 3, 5, 8]
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))   # [0, 0, 7, 9]
print(solution(["..", "#."]))   # [1, 0, 2, 1]
print(solution(["#", "."]))   # [0, 0, 1, 1]
print(solution(["...", "..#"]))   # [1, 2, 2, 3]
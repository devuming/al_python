import sys

ax, ay, bx, by, cx, cy = map(int, sys.stdin.readline().rstrip().split())
if ((ax - bx) * (ay - cy) == (ay - by) * (ax - cx)):  # 세 점이 한직선상에 있는지 : 기울기 비교
    print(-1.0)
    exit(0)
ab_len = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5  # 직선 ab 길이
ac_len = ((ax - cx) ** 2 + (ay - cy) ** 2) ** 0.5  # 직선 ac 길이
bc_len = ((bx - cx) ** 2 + (by - cy) ** 2) ** 0.5  # 직선 bc 길이

lens = [ab_len + ac_len, ab_len + bc_len, ac_len + bc_len]
print(2 * (max(lens) - min(lens)))

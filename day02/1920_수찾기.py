# 입력을 빨리 받게해주는 코드
import sys
input = sys.stdin.readline

# 입력받기
N = int(input())

A = set(map(int,input().split()))

M = int(input())

B = list(map(int,input().split()))

#아래에 있는 배열을 선형으로 탐색하면서
for num in B:
    # 위에 있는 배열에 있다면 1
    if num in A:
        print(1)
    # 없다면 0
    else:
        print(0)


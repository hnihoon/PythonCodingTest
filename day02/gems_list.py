
gems = [3,3,1,2,3,2,2,3,3,1]

# 1. 리스트 안에 1이 존재하는지 여부?
    # 반복문을 이용해서 리스트를 순회하며,
for gem in gems:
    # 1 이라는 데이터가 발견되었으면
    if gem == 1:
    # 찾았음을 표시하고 종료
        print("찾았다!!")
        break;

#range 정수모음 :   시작 끝 0~9까지 정수모음 사용
# for idx in range(0, 10):  # 시작이 0이면 생략가능
# len = length와 동일한 기능
# for idx in range(len(gems)):
#     if gems[idx] == 1:
#         print("찾았다!!")
#         break;
#
# # 2. 리스트에서 가장 큰 숫자를 찾는 문제
# lst = [56, 23, 43, 87, 12, 457, 86]
#
# #반복문을 이용해서 리스트를 순회하기
#
# #1.초기값(가장 큰 숫자 후보)을 세팅
# ans = -float("INF")
# ans = lst[0]
# #2.반복문을 이용해서 리스트를 선형 탐색
# for num in lst:
#     #3.방금 뽑은 값이 후보보다 크다면
#     if num > ans:
#     #4.숫자를 갱신해준다.
#         ans = num
#
# print(ans)

# 3. 집계 알고리즘
# gems = [3,3,1,2,3,2,2,3,3,1]
#
# # 딕셔너리를 이용한 집계
#     # 딕셔너리 = key : value로 이루어진 자료구조
#     # 딕셔너리에 1:0, 2:0, 3:0이라는 키값을 만든다.
# grades = {1:0, 2:0, 3:0}
#
# # 반복문을 이용해서 리스트를 선형 탐색
# for gem in gems:
#     # 방금 뽑은 그 등급에 따라서 value값을 갱신한다.
#     grades[gem] += 1
#
# print(grades)

# 리스트를 이용한 집계
# 빈 판 만들기
grades = [0] * 4
for gem in gems:
    grades[gem] += 1

print(grades)
my_lst = [3,5,1,2,4]
my_lst2 = my_lst[::-1] #원본 리스트가 뒤집어진 형태로 복제

print(my_lst)
print(my_lst2)

# 원소 추가(뒤에 추가)
my_lst.append(100)
print(my_lst)

#원소 삭제(인덱스 위치 지정) 삭제된 데이터는 반환됨
num = my_lst.pop(3)
print(my_lst)
print(num) # 2

# 정렬
my_lst.sort() # 오름차순 정렬
print(my_lst)

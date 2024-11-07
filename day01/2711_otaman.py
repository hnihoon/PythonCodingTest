# T = int(input())
#
# for _ in range(T):
#     idx, word = input().split()
#     idx = int(idx) -1
#     modified_word = word[:idx] + word[idx + 1:]
#     print(modified_word);

T = int(input())

for _ in range(T):
    idx, word = input().split()
    idx = int(input()) -1
    word = list(word)
    word.pop(idx)
    ans = ''.join(word)
print(ans)
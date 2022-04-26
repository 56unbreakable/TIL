# 조합
from unittest import result


def combination(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    result = []
    # 2.
    def generate(chosen):
        if len(chosen) == r:
            result.append(chosen[:])  # 여기가 중요함 후술하겠음
            return
    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])
    return result

# 순열
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    result = []
    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            result.append(chosen[:])
            return
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
    return result

k = permutation([1,2,3],3)
print(k)

# 왜 result.append(chosen)이 아니라 result.append(chosen[:])를 사용하느냐?
# 전자를 사용하면 chosen과 result가 같은 주소를 참조하기 때문에 chosen이 바뀌면 result도 바뀜
# 후자를 사용하면 복사를 해서 다른걸 참조하기 때문에 바뀌지 않음
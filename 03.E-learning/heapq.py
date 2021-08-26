import sys 
import heapq
input = sys.stdin.readline

def heapsort(iterable) : 
    h = [] # 데이터 담을 힙 
    result = []

    # 모든 원소를 힙에 삽입 
    for value in iterable : 
        heapq.heappush(h, value) # heap라이브러리로 담음 
    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 
    for i in range(len(h)) : 
        result.append(heapq.heappop(h))
    return result # 오름차순 정렬, minheap 정렬이 수행됨 



n = int(input()) 
arr = []

for i in range(n) : 
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n) : 
    print(res[i])
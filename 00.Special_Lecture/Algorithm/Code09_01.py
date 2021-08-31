# 그래프의 정점 생성

class Graph() :
    def __init__(self, size): # size = 정점의 개수
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)] # 정방행렬 생성


## 전역변수
G1 = None

# 메인코드
G1 = Graph(4) # A B C D
A, B, C, D = 0, 1, 2, 3

G1.graph[A][B] = 1 # A-B 연결
G1.graph[A][C] = 1
G1.graph[A][D] = 1

G1.graph[B][A] = 1
G1.graph[B][C] = 1

G1.graph[C][A] = 1
G1.graph[C][B] = 1
G1.graph[C][D] = 1

G1.graph[D][A] = 1
G1.graph[D][C] = 1

for row in range(4) :
    for col in range(4) :
        print(G1.graph[row][col], end = ' ')
    print()






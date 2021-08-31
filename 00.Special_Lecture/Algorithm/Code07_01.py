size = 5
queue = [None for _ in range(size)]

front = rear = -1 # 머리, 꼬리 = 1 이러면 큐가 텅 빈 것이다


# 큐에 데이터 넣기
rear += 1  # 꼬리를 증가시켜서 새로운 데이터 삽입
queue[rear] = "화사"
rear += 1
queue[rear] = "문별"
rear += 1
queue[rear] = "솔라"

# 큐에서 데이터 빼기
front += 1
data = queue[front]
queue[front] = None

print('입장손님 : ', data)

front += 1
data = queue[front]
queue[front] = None

print('입장손님 : ', data)

front += 1
data = queue[front]
queue[front] = None

print('입장손님 : ', data)
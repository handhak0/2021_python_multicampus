# 큐 간단 구현


## 함수
# def isQueuefull() :
#     global size, queue, front, rear
#     if rear + 1 == size :
#         return True
#     else :
#         return False

def isQueuefull() :
    global size, queue, front, rear
    if rear + 1 != size :
        return False
    elif (rear + 1 == size) & (front == - 1) :
        return True
    else :
        for i in range(front+1, size) :
            queue[i-1] = queue[i]
            queue[i] = None


def isQueueEmpty() :
    global size, queue, front, rear
    if (front == -1) & (rear == -1) :
        return True
    else :
        return False

def enQueue(data) :
    global size, queue, front, rear
    if rear + 1 == size :
        print("큐가 가득 찼습니다.")
    else :
        rear += 1
        queue[rear] = data


def deQueue() :
    global size, queue, front, rear
    if front == rear  :
        print("큐가 비었습니다다.")
    else :
        front = 1
        data = queue[front]
        queue[front] = None
        return data


## 전역
size = 5
queue = [None for _ in range(size)]
front = rear = -1
## 함수 선언부

# 스택이 모두 찼는지 확인 - top 사용
def isStackFull() :
    global SIZE, stack, top
    if (top == SIZE-1) :
        return True
    else :
        return False

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False

# push
def push(data) :
    global  SIZE, stack, top
    if isStackFull() :
        print("스택이 모두 찼습니다")
    else :
        top += 1
        stack[top] = data

# pop
def pop() :
    global SIZE, stack, top
    if isStackEmpty():
        print("스택이 모두 비었습니다")
    else :
        data = stack[top]
        stack[top] = None
        top -= 1
        print(data)

## 전역 변수부
SIZE = 5
stack = [ None for _ in range(SIZE)] # 스택 생성
top = -1

# ----- 여기까지가 스택 초기화 ------



## 메인 코드부

push("1")
push("2")
push("3")
push("4")
push("5")
push("6")

pop()
pop()

push("4")
push("6")

print(stack)
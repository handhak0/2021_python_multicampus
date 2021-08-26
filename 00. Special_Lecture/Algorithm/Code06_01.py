# 스택 구조
stack = [None, None, None,None, None]
top = -1

# push 하기
top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print(stack)

# pop 하기
data = stack[top]
stack[top] = None
top -= 1
print("pop--->", data)

'''
求栈中元素最小值，时间复杂度为O(1)，空间复杂度O(n)
'''
from Stack import Stack
import time

def solution1(s):
    '''
    stack_min压入时稍省空间，弹出操作稍费时间
    '''
    stack_data, stack_min = Stack(), Stack()
    if len(s) == 0:
        return -1
    for i in range(len(s)):
        stack_data.push(s[i])
        if stack_min.is_empty():
            stack_min.push(s[i])
        if s[i] <= stack_min.top():
            stack_min.push(s[i])
    return stack_min.top()

def solution2(s):
    '''
    stack_min压入时稍费空间，弹出操作稍省时间
    '''
    stack_data, stack_min = Stack(), Stack()
    if len(s) == 0:
        return -1
    for i in range(len(s)):
        stack_data.push(s[i])
        if stack_min.is_empty():
            stack_min.push(s[i])
        if s[i] <= stack_min.top():
            stack_min.push(s[i])
        if s[i] > stack_min.top():
            stack_min.push(stack_min.top())
    return stack_min.top()

if __name__ == "__main__":
    s1 = [3,4,5,1,2,1]

    start_1 = time.clock()
    print(solution1(s1))
    end_1 = time.clock()
    cost_1 = end_1 - start_1
    print("Solution1 cost " + str(cost_1) + "s")
    
    start_2 = time.clock()
    print(solution2(s1))
    end_2 = time.clock()
    cost_2 = end_2 - start_2
    print("Solution2 cost " + str(cost_2) + "s")

    if cost_1 < cost_2:
        print("Solution1 cost less time")
    else:
        print("Solution2 cost less time")

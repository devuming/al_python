# leedCode 232.Implement Queue using Stacks
import collections
class MyQueue(object):
    
    def __init__(self):
        self.object = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.object.append(x)
        return x

    def pop(self):
        """
        :rtype: int
        """
        return self.object.popleft()    # 선입 선출
        

    def peek(self):
        """
        :rtype: int
        """
        return self.object[0]   # 제일 처음 넣은 값 확인
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.object) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
print(obj.push(1))
print(obj.push(2))
print(obj.peek())
print(obj.pop())
print(obj.empty())
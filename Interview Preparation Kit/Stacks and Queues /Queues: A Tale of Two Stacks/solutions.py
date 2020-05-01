class MyQueue(object):
    def __init__(self):
        self.front = []
        self.back = []
        
    def peek(self):
        if self.front:
            return self.front[0]
        
    def pop(self):
        self.back.pop()
        return self.front.pop(0)
        
    def put(self, value):
        self.front.append(value)
        self.back.insert(0, value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
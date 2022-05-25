class Node:
    def __init__(self, value = None):
        self.value =  value
        self.next = None    

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0 # size확인 시 사용

    def push(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
            newNode.next = None
            return
    
    def pop(self, value):
        temp = self.head
        temp2 = self.head
        if temp.value == value:     # 1) head노드가 지우려는 노드면, 
            self.head = temp.next   # head를 다음노드로 지정 후 삭제
            del temp
            return
        else:
            while temp is not None:     # 2) head가 지우려는 노드가 아니면
                if temp.value == value: # 일치하는 노드를 찾기 위해 탐색
                    break
                prev = temp 
                temp = temp.next
            if temp is None: return     # 3) head가 None이면 바로 리턴

            prev.next = temp.next
            del temp
            return

    def show(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.value}")
            temp = temp.next
        
    def retHeadVal(self):
        return self.head.value

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.show()
    print("_---_")
    ll.pop(3)
    ll.pop(4)
    ll.show()
    print("_---_")
    print(ll.retHeadVal())


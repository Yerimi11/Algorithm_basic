class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# head = Node(5)
# next_node = Node(12)
# head.next = next_node

class SingleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def insertFirst(self, data):
        new_node = Node(data)
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node  # new_node를 head로 설정 후 다음 노드를 temp로 지정
        self.list_size += 1


    def insertMiddle(self, num, data):
        if self.head.next == None:
            insertLast(data)
            return
        node = self.selectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1

    def insertLast(self, data):
        node = self.head
        while True:
            if node.next == None:
                break
            node = node.next
        new_node = Node(data)
        node.next = new_node
        self.list_size += 1

    def selectNode(self, num):
        if self.list_size < num:
            return  # 오버플로우
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node
        
    def deleteNode(self, num):
        if self.list_size < 1:
            return  # 언더플로우
        elif self.list_size < num:
            return  # 오버플로우
        
        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num - 1)
        node.next = node.next.next
        del_node = node.next    # 윗줄이랑 순서 바껴야하는거 아닌가?
        del del_node
    
    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

    
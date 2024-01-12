from Node import Node


class IntNode(Node):
    def __init__(self,number:int, parent=None):
        super().__init__(parent)
        self.number=number
    def getNumber(self):
        if self.parent != None:
            return self.parent.getNumber()+self.number
        else:
            return self.number


node1 = IntNode(10)
node2 = IntNode(40,node1)
node3 = IntNode(30,node2)

print(node3.getNumber())

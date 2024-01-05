class Node:
    def __init__(self,parent=None):
        self.children=[]
        if parent==None:
            self.parent=parent
        else:
            parent.addChild(self)
    def addChild(self,child):
        child.parent=self
        self.children.append(child)

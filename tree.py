class Tree:
    """Class Tree : a node can contain an indefined number of subtrees"""

    def __init__(self, iNode, iSubtrees=[]):
        self.Node = iNode
        self.Subtrees = iSubtrees

    def __str__(self):
        if self.Subtrees == []:
            return str(self.Node)
        else:
            aListOfNodes = []
            for subtree in self.Subtrees:
                aListOfNodes.append(str(subtree))
            return str(self.Node) + ':[' + str(', '.join(aListOfNodes))+ ']'

    def getNode(self):
        return self.Node

    def setNode(self, iValueNode):
        self.Node = iValueNode

    def removeNode(self, iNodeValue):
        for subtree in self.Subtrees:
            if iNodeValue == subtree.getNode():
                self.Subtrees.remove(subtree)

    def getSubs(self):
        return self.Subtrees

    def addTree(self, iTree):
        self.Subtrees.append(iTree)

    def buildTreeFromList(iListOfValueNodes):
        if len(iListOfValueNodes) == 1:
            return Tree(iListOfValueNodes.pop(0))
        else:
            currentNode = iListOfValueNodes.pop(0)
            return Tree(currentNode, [Tree.buildTreeFromList(iListOfValueNodes)])

    def addPath(self, iListOfValueNodes):
        # Adds a node with all the parents specified beforehand
        # Ex : if Tree(3, [Tree(4), Tree(5)]).addPath([4, 6])
        #       returns Tree(3, [Tree(4, [Tree(6)], Tree(5)])
        # The first element of the Node is not the root
        pass






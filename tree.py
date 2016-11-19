class Tree:
    """Class Tree : a node can contain an indefined number of subtrees"""

    def __init__(self, iNode, iChildren=[]):
        self.Node = iNode
        self.Children = iChildren

    def __str__(self):
        if self.Children == []:
            return str(self.Node)
        else:
            aListOfNodes = []
            for subtree in self.Children:
                aListOfNodes.append(str(subtree))
            return str(self.Node) + ':[' + str(', '.join(aListOfNodes))+ ']'

    def getNode(self):
        return self.Node

    def setNode(self, iValueNode):
        self.Node = iValueNode

    def removeNode(self, iNodeValue):
        for subtree in self.Children:
            if iNodeValue == subtree.getNode():
                self.Children.remove(subtree)

    def getChildren(self):
        return self.Children

    def hasChildren(self):
        return self.Children != []

    def getNumberOfNodes(self):
        if not self.hasChildren:
            return 1
        else:
            return 1 + sum(map(Tree.getNumberOfNodes, self.Children))

    def addTree(self, iTree):
        self.Children.append(iTree)

    def buildTreeFromList(iListOfValueNodes):
        if len(iListOfValueNodes) == 1:
            return Tree(iListOfValueNodes.pop(0))
        else:
            currentNode = iListOfValueNodes.pop(0)
            return Tree(currentNode, [Tree.buildTreeFromList(iListOfValueNodes)])

    def hasNode(self, iNodeValue):
        for child in self.Children:
            if child.getNode() == iNodeValue:
                return True
        return False

    def concatTree(self, iTree):
        # Concat the Tree with the Tree given in parameter
        # Ex : if Tree(3, [Tree(4), Tree(5)]).concatTree(Tree(3, [Tree(4, [Tree(6)]), Tree(9)])
        #   should give Tree(3, [Tree(4, [Tree(6)]), Tree(5), Tree(9)])
        #   Assume the root is the same
        assert(self.Node == iTree.getNode())
        if self.Children == []:
            self.Children = iTree.getChildren()
        else:
            for child in iTree.getChildren():
                found = False
                for treeChild in self.Children:
                    if child.getNode() == treeChild.getNode():
                        treeChild.concatTree(child)
                        found = True
                        break
                # child is not in the list of children of the Tree object
                if not found:
                    self.addTree(child)





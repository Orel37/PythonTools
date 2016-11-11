class Tree:
    """Class Tree : a node can contain an indefined number of subtrees"""

    def __init__(self, node, sons=[]):
        self.Node = node
        self.Subs = sons

    def __str__(self):
        if self.Subs == []:
            return str(self.Node)
        else:
            aListOfNodes = []
            for subtree in self.Subs:
                aListOfNodes.append(str(subtree))
            return str(self.Node) + ':[' + str(', '.join(aListOfNodes))+ ']'

    def getNode(self):
        return self.Node

    def getSubs(self):
        return self.Subs

    def addTree(self, iTree):
        self.Subs.append(iTree)

    def add_path(self, iListOfValueNodes):
        # Adds a node with all the parents specified beforehand
        # Ex : if Tree(3, [Tree(4), Tree(5)]).add_path([4, 6])
        #       returns Tree(3, [Tree(4, [Tree(6)], Tree(5)])
        # The first element of the Node is not the root
        pass





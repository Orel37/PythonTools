import unittest
from tree import Tree


class TestTree(unittest.TestCase):
    def test_init(self):
        aTree1 = Tree(3)
        self.assertEqual(3, aTree1.getNode())
        self.assertEqual([], aTree1.getChildren())

        aTree2 = Tree(4, [Tree(3), Tree(5)])
        self.assertEqual(4, aTree2.getNode())
        self.assertEqual(2, len(aTree2.getChildren()))

    def test_str(self):
        aTree1 = Tree(3)
        self.assertEqual("3", str(aTree1))

        aTree2 = Tree(4, [Tree(3), Tree(5)])
        self.assertEqual("4:[3, 5]", str(aTree2))

        aTree3 = Tree(4, [Tree(3, [Tree(2), Tree(9), Tree(7)]), Tree(5)])
        self.assertEqual("4:[3:[2, 9, 7], 5]", str(aTree3))

    def test_removeNode(self):
        aTree2 = Tree(4, [Tree(3), Tree(5)])
        aTree2.removeNode(3)
        self.assertEqual("4:[5]", str(aTree2))

        aTree3 = Tree(4, [Tree(3, [Tree(2), Tree(9), Tree(7)]), Tree(5)])
        aTree3.removeNode(3)
        self.assertEqual("4:[5]", str(aTree3))

        aTree4 = Tree(4, [Tree(3, [Tree(2), Tree(9), Tree(7)]), Tree(9)])
        aTree4.removeNode(9)
        self.assertEqual("4:[3:[2, 9, 7]]", str(aTree4))

    def test_addTree(self):
        aTree2 = Tree(4, [Tree(3), Tree(5)])
        aTree1 = Tree(7)
        aTree2.addTree(aTree1)
        self.assertEqual("4:[3, 5, 7]", str(aTree2))

    def test_buildTreeFromList(self):
        aTree2 = Tree(4, [Tree(3, [Tree(5)])])
        aListOfNodes = [4, 3, 5]
        self.assertEqual(str(aTree2), str(Tree.buildTreeFromList(aListOfNodes)))

        aTree3 = Tree(4, [Tree(3, [Tree(2, [Tree(9, [Tree(7)])])])])
        aListOfNodes2 = [4, 3, 2, 9, 7]
        self.assertEqual(str(aTree3), str(Tree.buildTreeFromList(aListOfNodes2)))

    def test_hasNode(self):
        aTree2 = Tree(4, [Tree(3), Tree(5)])
        self.assertTrue(aTree2.hasNode(3))
        self.assertTrue(aTree2.hasNode(5))
        self.assertFalse(aTree2.hasNode(4))
        self.assertFalse(aTree2.hasNode(6))

    def test_hasChildren(self):
        aTree1 = Tree(7)
        aTree2 = Tree(4, [Tree(3, [Tree(5)])])
        self.assertFalse(aTree1.hasChildren())
        self.assertTrue(aTree2.hasChildren())

    def test_getNumberOfNodes(self):
        aTree1 = Tree(7)
        aTree2 = Tree(4, [Tree(3, [Tree(5)])])
        aTree3 = Tree(4, [Tree(3, [Tree(2, [Tree(9, [Tree(7)])])])])
        aTree4 = Tree(3, [Tree(4, [Tree(6)]), Tree(5), Tree(9)])
        self.assertEqual(1, aTree1.getNumberOfNodes())
        self.assertEqual(3, aTree2.getNumberOfNodes())
        self.assertEqual(5, aTree3.getNumberOfNodes())
        self.assertEqual(5, aTree4.getNumberOfNodes())

    def test_concat(self):
        aTree1 = Tree(4, [Tree(3)])
        aTree2 = Tree(4, [Tree(5)])
        aTree1.concatTree(aTree2)
        self.assertEqual(str(Tree(4, [Tree(3), Tree(5)])), str(aTree1))

        aTree3 = Tree(4)
        aTree4 = Tree(4, [Tree(7)])
        aTree3.concatTree(aTree4)
        self.assertEqual(str(Tree(4, [Tree(7)])), str(aTree3))

        aTree5 = Tree(5, [Tree(7)])
        aTree6 = Tree(5)
        aTree5.concatTree(aTree6)
        self.assertEqual(str(Tree(5, [Tree(7)])), str(aTree5))

        aTree7 = Tree(3, [Tree(4), Tree(5)])
        aTree8 = Tree(3, [Tree(4, [Tree(6)])])
        aTree7.concatTree(aTree8)
        self.assertEqual(str(Tree(3, [Tree(4, [Tree(6)]), Tree(5)])), str(aTree7))

        aTree9 = Tree(3, [Tree(4), Tree(5)])
        aTree10 = Tree(3, [Tree(4, [Tree(6)]), Tree(5)])
        aTree9.concatTree(aTree10)
        self.assertEqual(str(Tree(3, [Tree(4, [Tree(6)]), Tree(5)])), str(aTree9))

        aTree11 = Tree(3, [Tree(4), Tree(5)])
        aTree12 = Tree(3, [Tree(4, [Tree(6)]), Tree(9)])
        aTree11.concatTree(aTree12)
        aTreeResult = Tree(3, [Tree(4, [Tree(6)]), Tree(5), Tree(9)])
        self.assertEqual(str(aTreeResult), str(aTree11))

if __name__ == '__main__':
    unittest.main()
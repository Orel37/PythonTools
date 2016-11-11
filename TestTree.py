import unittest
from tree import Tree


class TestTree(unittest.TestCase):
    def test_init(self):
        aTree1 = Tree(3)
        self.assertEqual(3, aTree1.getNode())
        self.assertEqual([], aTree1.getSubs())

        aTree2 = Tree(4, [Tree(3), Tree(5)])
        self.assertEqual(4, aTree2.getNode())
        self.assertEqual(2, len(aTree2.getSubs()))

    def test_str(self):
        aTree1 = Tree(3)
        self.assertEqual("3", str(aTree1))

        aTree2 = Tree(4, [Tree(3), Tree(5)])
        self.assertEqual("4:[3, 5]", str(aTree2))

        aTree3 = Tree(4, [Tree(3, [Tree(2), Tree(9), Tree(7)]), Tree(5)])
        self.assertEqual("4:[3:[2, 9, 7], 5]", str(aTree3))

    def test_addTree(self):
        aTree2 = Tree(4, [Tree(3), Tree(5)])
        aTree1 = Tree(7)
        aTree2.addTree(aTree1)
        self.assertEqual("4:[3, 5, 7]", str(aTree2))

    # def test_add_path(self):
    #     aTree2 = Tree(4, [Tree(3), Tree(5)])
    #     aTree2.add_path([4, 3, 6])
    #     for subtree in aTree2.getSubs():
    #         if subtree.getNode() == 3:
    #             self.assertEqual(6, subtree.getSubs()[0])


if __name__ == '__main__':
    unittest.main()
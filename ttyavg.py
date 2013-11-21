import pickle

class GameNode:
    def __init__(self):
        self._children = []
    def addchild(self, link, node):
        self._children.append((link, node))
    @staticmethod
    def run(node):
        for choice in node.display():
            if isinstance(choice, tuple):
                GameNode.save(node, choice[1])
            elif not node._children or choice == 'Q':
                return
            else:
                GameNode.run(node._children[choice][1])
                return
    @staticmethod
    def save(node, savepath):
        with open(savepath, "wb") as sf:
            pickle.dump(node, sf)
    @staticmethod
    def load(savefile):
        with open(savefile, "rb") as lf:
            node=pickle.load(lf)
        return node
import pickle

class Event:
    def __init__(self, type, arg):
        self.type = type
        self.arg = arg

def run(node):
    for event in node.display():
        if event.type == 'SAVE':
            save(node, event.arg)
        elif event.type == 'QUIT':
            return event.arg
        elif event.type == 'CONTINUE':
            return run(event.arg)

def save(node, savepath):
    with open(savepath, "wb") as sf:
        pickle.dump(node, sf)

def load(savefile):
    with open(savefile, "rb") as lf:
        node=pickle.load(lf)
    return node
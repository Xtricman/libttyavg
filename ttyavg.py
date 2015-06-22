import pickle

class Event:
    def __init__(self, ev_type, arg):
        self.ev_type = ev_type
        self.arg = arg

def run(node):
    history.append(node)
    for event in node.display():
        if event.ev_type == 'SAVE':
            with open(event.arg, "wb") as sh:
                pickle.dump(history, sh)
        elif event.ev_type == 'QUIT':
            return event.arg
        elif event.ev_type == 'CONTINUE':
            return run(event.arg)
        elif event.ev_type == 'BACK':
            if len(history) == 1:
                continue
            else:
                history.pop()
                return run(history.pop())

def load(savefile):
    with open(savefile, "rb") as lf:
        history=pickle.load(lf)
    return history
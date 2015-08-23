import pickle
import sys


class Event:
    def __init__(self, ev_type, arg=None):
        self.ev_type = ev_type
        self.arg = arg
   
            
def game_start():
    node_map = read_node_map()
    if len(sys.argv)==1:
        uuid = 0
        runtime_history = []
    else:
        with open(sys.argv[1], "rb") as savedgame:
            runtime_history, uuid = pickle.load(savedgame)

    def run(uuid):
    runtime_history.append(uuid)
    node = node_map[uuid]
    for event in render_and_send_event(node):
        if event.ev_type == 'SAVE':
            with open(event.arg, "wb") as savefile:
                pickle.dump((runtime_history[:-1], uuid), savefile)
        elif event.ev_type == 'QUIT':
            return event.arg
        elif event.ev_type == 'CONTINUE':
            return run(event.arg)
        elif event.ev_type == 'BACK':
            if len(runtime_history) > 1:
                runtime_history.pop()
                return run(runtime_history.pop())

    run(uuid)
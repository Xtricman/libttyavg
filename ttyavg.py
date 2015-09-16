import pickle
import sys


def game_start():
    if len(sys.argv)==1:
        start_uuid = 0
        runtime_history = []
    else:
        with open(sys.argv[-1], "rb") as savedgame:
            start_uuid, runtime_history = pickle.load(savedgame)

    def run(uuid):
        runtime_history.append(uuid)
        event = render_and_get_event(uuid)
        
        supported_types = ('SAVE', 'QUIT', 'CONTINUE', 'BACK')
        if event[0] not in supported_types:
            raise ValueError("Event type {} not supported.".format(event[0]))

        while event[0] == 'SAVE':
            with open(event[1], "wb") as savefile:
                pickle.dump((uuid, runtime_history[:-1]), savefile)
            event = render_and_get_event(uuid)
        if event[0] == 'QUIT':
            return event[1]
        if event[0] == 'CONTINUE':
            return run(event[1])
        if event[0] == 'BACK':
            if len(runtime_history) > 1:
                runtime_history.pop()
                return run(runtime_history.pop())

    run(start_uuid)

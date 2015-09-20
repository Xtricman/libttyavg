import pickle

class State(dict):
    """self["player_id"] = player_id
self["player_inventory"] = {each player_id:{item_id}}
self["player_positions"] = {each player_id:scene_id}
self["scene_items"] = {each scene_id:{item_id}}"""

class Event(dict):
    def __init__(self, type, arg):
        self["type"] = type
        self["arg"] = arg

def game_start(init_state):

    state = init_state

    while(True):
        event = render_and_get_event(state)
        
        supported_types = ('SAVE', 'QUIT', 'DELET', 'ADDINVENTORY')
        if event.type not in supported_types:
            raise ValueError("Event type {} not supported.".format(event.type))

        if event.type == 'SAVE':
            with open(event.arg, "wb") as save_file:
                pickle.dump(state, save_file)
        elif event.type == 'QUIT':
            return event.arg
        elif event.type == 'DELET':
            if state.player_id == event.arg:
                state.player_id = None
            state.player_inventory.pop(event.arg, None)
            state.player_positions.pop(event.arg, None)
            state.scene_items.pop(event.arg, None)
            for i in state.player_inventory:
                state.player_inventory[i].discard(event.arg)
            for i in state.scene_items:
                state.scene_items[i].discard(event.arg)
            for k,v in state.player_positions:
                if v == event.arg:
                state.player_positions[k] = None
        elif event.type == 'ADDINVENTORY':
            state.player_inventory[state.player_id].add(event.arg)
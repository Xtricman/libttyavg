import ttyavg import *

def render_and_get_event(state):
    node = uuid_node_map[uuid]
    print('=====')
    print(node['description_text'])
    print()
    if not node['options']:
        return Event('QUIT', None)
    for k in node['options']:
        print(k)
    print('=====')
    print('>>', end='')
    user_input = input()
    if user_input == 'quit':
        return Event('QUIT', None)
    if user_input[0:4] == 'save':
        return Event('SAVE', user_input[5:])

uuid_node_map = {
                 0:{'description_text':'游戏开始了', 'options':['路线1', '路线2']},
                 1:{'description_text':'路线1开端', 'options':['去发展']},
                 3:{'description_text':'路线1发展', 'options':['去结局']},
                 5:{'description_text':'路线1结局', 'options':None},
                 2:{'description_text':'路线2开端', 'options':['去发展']},
                 4:{'description_text':'路线2发展', 'options':['去结局']},
                 6:{'description_text':'路线2结局', 'options':None}
                }
init_state = {0:[1,2], 1:[3], 3:[5], 2:[4], 4:[6]}

ttyavg.render_and_get_event = render_and_get_event
ttyavg.game_start(init_state)

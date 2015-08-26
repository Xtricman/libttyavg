import ttyavg

def render_and_get_event(uuid):
    node = uuid_node_map[uuid]
    print('=====')
    print(node['description_text'])
    print()
    if not node['options']:
        return ('QUIT',)
    for k in node['options']:
        print(k)
    print('=====')
    print('>>', end='')
    user_input = input()
    if user_input == 'quit':
        return ('QUIT',)
    if user_input[0:4] == 'save':
        return ('SAVE', user_input[5:])
    if user_input == 'back':
        return ('BACK',)
    if int(user_input) in range(0, len(game_map[uuid])):
        return ('CONTINUE', game_map[uuid][int(user_input)])

uuid_node_map = {
                 0:{'description_text':'游戏开始了', 'options':['路线1', '路线2']},
                 1:{'description_text':'路线1开端', 'options':['去发展']},
                 3:{'description_text':'路线1发展', 'options':['去结局']},
                 5:{'description_text':'路线1结局', 'options':None},
                 2:{'description_text':'路线2开端', 'options':['去发展']},
                 4:{'description_text':'路线2发展', 'options':['去结局']},
                 6:{'description_text':'路线2结局', 'options':None}
                }
game_map = {0:[1,2], 1:[3], 3:[5], 2:[4], 4:[6]}

ttyavg.render_and_get_event = render_and_get_event
ttyavg.game_start()

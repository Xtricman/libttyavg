import ttyavg
from pickle import loads
from zipfile import ZipFile


def render_and_send_event(node):
    print('=====')
    print(node['description_text'])
    print()
    for k in node['options']:
        print(k[0])
    print('=====')
    while True:
        print('>>', end='')
        user_input = input()
        if user_input == 'quit':
            yield ttyavg.Event('QUIT')
        elif user_input[0:4] == 'save':
            yield ttyavg.Event('SAVE', user_input[5:])
        elif user_input == 'back':
            yield ttyavg.Event('BACK')
        elif int(user_input) in range(0, len(node['options'])):
            yield ttyavg.Event('CONTINUE', node['options'][int(user_input)][1])
        else:
            continue


#def read_node_map():
    #with ZipFile("GameData.zip","r")  as gamedata:
        #return {uuid:loads(node_map_data.read(uuid)) for uuid in gamedata.namelist()}
def read_node_map():
    return {
                  0:{'description_text':'游戏开始了', 'options':[('路线1', 1), ('路线2', 2)]},
                  1:{'description_text':'路线1开端', 'options':[('去发展', 3)]},
                 3:{'description_text':'路线1发展', 'options':[('去结局', 5)]},
                 5:{'description_text':'路线1结局', 'options':[]},
                  2:{'description_text':'路线2开端', 'options':[('去发展', 4)]},
                 4:{'description_text':'路线2发展', 'options':[('去结局', 6)]},
                 6:{'description_text':'路线2结局', 'options':[]}
                }

ttyavg.__dict__['read_node_map'] = read_node_map
ttyavg.__dict__['render_and_send_event'] = render_and_send_event
ttyavg.game_start()
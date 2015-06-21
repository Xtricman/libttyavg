from ttyavg import Event

class UserNode:
    def __init__(self, node_text):
        self.node_text = node_text
        self.options_dict = {}
    def add_option(self, op_text, op_node):
        self.options_dict[op_text] = op_node
    def display(self):
        print('==============')
        print(self.node_text)
        print()
        for k in self.options_dict:
            print(k)
        print('==============')
        while True:
            print('>>', end='')
            user_input = input()
            if user_input == 'exit':
                yield Event('QUIT', None)
            elif user_input[0:4] == 'save':
                yield Event('SAVE', user_input[5:])
            else:
                yield Event('CONTINUE', self.options_dict[user_input])

from ttyavg import GameNode

class CuNode(GameNode):
    def __init__(self, contentstring):
        super(CuNode, self).__init__()
        self.content = contentstring
    def display(self):
        print(self.content)
        for i in self._children:
            print('>>' + i[0])
        while True:
            user_input = input()
            if user_input == 'exit':
                yield 'Q'
            elif user_input[0:4] == 'save':
                yield 'S',user_input[5:]
            else:
                yield int(user_input)

import sys
sys.path.append("..")
from customnode import CuNode, GameNode
if len(sys.argv)  ==  1:
    start = CuNode("游戏序章")
    tmp01 = CuNode("路线0发展第一步")
    tmp0gaochao = CuNode("路线0隐藏画面")
    tmp02 = CuNode("路线0发展第二步")
    tmp11 = CuNode("路线1发展第一步")
    tmp12 = CuNode("路线1发展第二步")
    tmphappyend = CuNode("结局是你活着")
    tmpbadend = CuNode("结局是你死了")
    start.addchild("路线0",  tmp01)
    start.addchild("路线1",  tmp11)
    tmp01.addchild("继续",  tmp0gaochao)
    tmp0gaochao.addchild("继续", tmp02)
    tmp02.addchild("继续", tmphappyend)
    tmp11.addchild("继续", tmp12)
    tmp12.addchild("继续", tmpbadend)
    GameNode.run(start)
else:
    node=GameNode.load(sys.argv[1])
    GameNode.run(node)

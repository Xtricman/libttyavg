from customnode import UserNode
from ttyavg import run

start = UserNode("游戏序章")
tmp01 = UserNode("路线0发展第一步")
tmp0gaochao = UserNode("路线0隐藏画面")
tmp02 = UserNode("路线0发展第二步")
tmp11 = UserNode("路线1发展第一步")
tmp12 = UserNode("路线1发展第二步")
tmphappyend = UserNode("结局是你活着")
tmpbadend = UserNode("结局是你死了")
start.add_option("路线0",  tmp01)
start.add_option("路线1",  tmp11)
tmp01.add_option("继续",  tmp0gaochao)
tmp0gaochao.add_option("继续", tmp02)
tmp02.add_option("继续", tmphappyend)
tmp11.add_option("继续", tmp12)
tmp12.add_option("继续", tmpbadend)
run.__globals__['history'] = []
run(start)

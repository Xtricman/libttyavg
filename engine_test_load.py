import sys
from ttyavg import run,load

history = load(sys.argv[1])
run.__globals__['history'] = history
run(history.pop())
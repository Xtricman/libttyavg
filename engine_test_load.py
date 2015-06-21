import sys
from ttyavg import run,load

node = load(sys.argv[1])
run(node)
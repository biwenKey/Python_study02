import sys
import os
print(sys.path)
cmd_res = os.popen("dir").read()
print("----------->",cmd_res)



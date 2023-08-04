
#####TESTING#####
import sys, os

sys.path.append(os.path.abspath('My_Production_Features'))

import my_fun

my_fun.timer()

for p in sys.path:
    print(p)
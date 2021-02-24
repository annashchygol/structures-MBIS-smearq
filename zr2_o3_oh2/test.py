import sys
import os
import numpy as np
sys.path.append('%s/scripting/plams/src' % os.getenv('ADFHOME'))
from scm.plams import init, finish, KFReader

print('test')

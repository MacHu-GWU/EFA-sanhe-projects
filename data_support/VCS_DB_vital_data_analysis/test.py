##coding=utf8
import numpy as np
from StringIO import StringIO
from datetime import datetime as dt

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [xx*xx for xx in x]

fig = plt.figure(figsize=(3,3))
ax  = fig.add_subplot(111)

#box = ax.get_position()
#ax.set_position([0.3, 0.4, box.width*0.3, box.height])
# you can set the position manually, with setting left,buttom, witdh, hight of the axis
# object
ax.set_position([0.1,0.1,0.5,0.8])
ax.plot(x, y)
leg = ax.legend(['abc'], loc = 'center left', bbox_to_anchor = (1.0, 0.5))
plt.show()
fig.savefig('aaa.png')

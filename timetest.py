__author__ = 'ascott'

import time

timedict={}
timenow = time.strftime("%H:%M:%S")
timedict={'Time':timenow, 'When':'Now','Time':timenow, 'When':'Then'}
#timedict={'Time':timenow, 'When':'Then'}
print timedict

print timedict['Time']
print timedict['When']

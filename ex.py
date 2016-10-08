import time
from alert import alert

i = 0
while i < 10:
    i += 1
    alert('i: %d' % i, 'title')
    time.sleep(2)

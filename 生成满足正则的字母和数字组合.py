import string
import random
import re

while True:
    s = string.ascii_uppercase + string.digits + string.ascii_lowercase
    s_list = list(s)
    n = random.randint(6, 18)
    ss = ''.join(random.sample(s_list, 18))
    if re.match('^(?=.*[a-zA-Z])(?=.*[0-9])[A-Za-z0-9]{6,18}$', ss, flags=0):
        print(ss)
        break

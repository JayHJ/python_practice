#!/usr/bin/python3

import sys
import os
import shutil
import glob
import re
import math
import random
from urllib.request import urlopen  # url open
import smtplib
from datetime import date
import zlib


# return current work dir
os.getcwd()

# change current work dir
os.chdir('')
# perform system command, such 'mkdir temp'
os.system('')

#returns a list of all module functions
dir(os)
#returns an extensive manual page created from the module's docstrings
help(os)

# copy file
shutil.copy('data.db', 'archive.db')
shutil.move('/build/executable','installdir')

# search file
glob.glob('*.py')


# regular expression 
re.findall(r'\bf[a-z]*', 'which foot or hand fell fasteast')

math.cos(math.pi / 4)
math.log(1024, 2)

random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)
random.random()
random.randrange(6)

server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
server.quit()


now = date.today()
print(now)

birthday = date(1964,7,31)
age = now - birthday
print(age.days)

s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

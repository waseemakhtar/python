'''
    Following statement imports a function call from
    the library named subprocess
'''
from subprocess import call
#Following statement imports library 'os'
import os

#two ways to do it, this is first one
call(["ls","-l", "-t", "-r"])

#call(["ping", "www.google.com"])
#this is second one
os.system("ping www.google.com")


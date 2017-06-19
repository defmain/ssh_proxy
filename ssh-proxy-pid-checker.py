#!/usr/bin/env python
import subprocess

cmd = 'ps -x | grep 5222 | grep -v grep'
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
test = bool(output)
#print test

if test == True:
#  print "running"
   exit(0)
else:
# print "Executing start-ssh-proxy.sh"
    startscript = subprocess.call("./start-ssh-proxy.sh")
  

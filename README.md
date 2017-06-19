# ssh_proxy

This is a little script that uses the python subprocess module to grab a pid, 
and then determine if it's running or not. If it's running, exit cleanly, and if 
it isn't run another script to start it up. 

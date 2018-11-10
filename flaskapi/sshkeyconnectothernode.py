from datainit import *

def getkey():        
        
     if not nova.keypairs.findall(name="mynewkey10"):
           with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
                nova.keypairs.create(name="mynewkey10", public_key=fpubkey.read())
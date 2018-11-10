from datainit import *

#### this module get public key id_rsa.pub and store in new creating  vm .ssh/authorized_keys dir and after that we can access using ssh ubuntu@servername  
 ### 

def getkey():        
        
     if not nova.keypairs.findall(name="mynewkey10"):
           with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
                nova.keypairs.create(name="mynewkey10", public_key=fpubkey.read())
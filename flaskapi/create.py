
from datainit import *
import searchserver as S
import sshkeyconnectothernode as K

def vmcreate(servername):
        print "user authorization completed."

         #print   nova.floating_ip_create()
        #keypair_name = "key_name"
        #keypair = nova.keypairs.create(name=keypair_name)
        #print keypair.public_key
        namekey=None

        
        if private_net != None:
           net = nova.neutron.find_network(private_net)
           nics =  [{'net-id': net.id}]
        else:
           sys.exit("private-net not defined.")

        K.getkey()
        #if not nova.keypairs.findall(name="mynewkey1"):
           #with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
                #nova.keypairs.create(name="mynewkey1", public_key=fpubkey.read())
        
        
        cfg_file_path =  os.getcwd()+'/cloud-cfg.txt'
        if os.path.isfile(cfg_file_path):
           userdata = open(cfg_file_path)
        else:
           sys.exit("cloud-cfg.txt is not in current working directory")

        secgroups = ['default']

###############

        print "Creating instance ... "
        if servername!= None :
           instance = nova.servers.create(name=servername, image=image, flavor=flavor, userdata=userdata, key_name="mynewkey10", nics=nics,security_groups=secgroups)

#instance.add_floating_ip(floating_ip)
        else:
           instance = nova.servers.create(name="servername1", image=image, flavor=flavor, userdata=userdata, key_name="mynewkey10", nics=nics,security_groups=secgroups)
        
        inst_status = instance.status
        print "waiting for 10 seconds.. "
        time.sleep(10)

        while inst_status == 'BUILD':
               print "Instance: "+instance.name+" is in "+inst_status+" state, sleeping for 5 seconds more..."
               time.sleep(5)
               instance = nova.servers.get(instance.id)
               inst_status = instance.status

               print "Instance: "+ instance.name +" is in " + inst_status + "state"
       
        if  servername!= None :
            fixed_ip = S.searchserver(servername)
        else:
            fixed_ip = S.searchserver("servername1")
        print fixed_ip        
#                 return "sucess"  

        #if floating_ip != None: 
               #instance.add_floating_ip(floating_ip)
               #print "Instance booted! Name: " + instance.name + " Status: " +instance.status+ ", floating IP attached"
        #else:
                
               #print "Instance booted! Name: " + instance.name + " Status: " +instance.status+ ", No floating IP attached"


########
#def Add(a,b):
#    return a+b
    
#def Add1():
#    return flavor    

#cow()

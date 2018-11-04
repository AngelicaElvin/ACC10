
from datainit import *


def vmcreate():
        print "user authorization completed."

         #print   nova.floating_ip_create()
        keypair_name = "key_name"
        keypair = nova.keypairs.create(name=keypair_name)
        print keypair.public_key
        
        if private_net != None:
           net = nova.neutron.find_network(private_net)
           nics =  [{'net-id': net.id}]
        else:
           sys.exit("private-net not defined.")

        cfg_file_path =  os.getcwd()+'/cloud-cfg.txt'
        if os.path.isfile(cfg_file_path):
           userdata = open(cfg_file_path)
        else:
           sys.exit("cloud-cfg.txt is not in current working directory")

        secgroups = ['default']

###############

        print "Creating instance ... "
        instance = nova.servers.create(name="vm10", image=image, flavor=flavor, userdata=userdata, key_name=key, nics=nics,security_groups=secgroups)
#instance.add_floating_ip(floating_ip)
        inst_status = instance.status
        print "waiting for 10 seconds.. "
        time.sleep(10)

        while inst_status == 'BUILD':
               print "Instance: "+instance.name+" is in "+inst_status+" state, sleeping for 5 seconds more..."
               time.sleep(5)
               instance = nova.servers.get(instance.id)
               inst_status = instance.status

               print "Instance: "+ instance.name +" is in " + inst_status + "state"
#                 return "sucess"  

        if floating_ip != None: 
               instance.add_floating_ip(floating_ip)
               print "Instance booted! Name: " + instance.name + " Status: " +instance.status+ ", floating IP attached"
        else:
                
               print "Instance booted! Name: " + instance.name + " Status: " +instance.status+ ", No floating IP attached"


########
#def Add(a,b):
#    return a+b
    
#def Add1():
#    return flavor    

#cow()
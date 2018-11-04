
from datainit import *
############

#############

def vmdelete():
    servers_list = nova.servers.list()
    server_del = "vm49"
    server_exists = False

    for s in servers_list:
        if s.name == server_del:
           print("This server %s exists" % server_del)
           server_exists = True
           break
        
    if not server_exists:
        print("server %s does not exist" % server_del)
    else:
        print("deleting server..........")
        nova.servers.delete(s)
        print("server %s deleted" % server_del)


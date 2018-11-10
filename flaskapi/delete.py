
from datainit import *
############

#############

def vmdelete(servername):
    servers_list = nova.servers.list()
    server_del = servername
    server_exists = False
    print servername
    for s in servers_list:
        print s
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


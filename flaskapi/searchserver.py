
from datainit import *


def searchserver(servername):

    server = nova.servers.find(name=servername)
    netname = "SNIC 2018/10-30 Internal IPv4 Network"

    #print server.networks[netname]


    fixed_ip1  = server.networks[netname]
     
    fixed_ip = fixed_ip1[0]
    
    return  fixed_ip

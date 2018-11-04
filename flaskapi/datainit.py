import time, os, sys
import inspect
#import shade
#import novaclient.v3.client as nvclient
#from credentials import get_nova_creds
from os import environ as env
#import shade

from  novaclient import client
import keystoneclient.v3.client as ksclient
#from credentials import get_credentials
#from credentials import get_nova_creds
from keystoneauth1 import loading
from keystoneauth1 import session

import novaclient.v2.client as nvclient


############

#############


flavor = "ssc.small" 
private_net = "SNIC 2018/10-30 Internal IPv4 Network"
floating_ip_pool_name = None #"Public External IPv4 Network"
floating_ip = "130.239.81.138"
image_name = "Ubuntu 16.04 LTS (Xenial Xerus) - latest"
key = "zeelabkey"
floating_ip_pool_name = "Public External IPv4 Network"
loader = loading.get_plugin_loader('password')

auth = loader.load_from_options(auth_url="https://hpc2n.cloud.snic.se:5000/v3",
                                username="s11778",
                                password="Zee_279000",
                                project_name="SNIC 2018/10-30",
                                project_domain_name="snic",
                                project_id="ad5091c4f42e4defb98eb9550f875f4f",
                                user_domain_name="snic")

sess = session.Session(auth=auth)
nova = client.Client('2.1', session=sess)
image = nova.glance.find_image(image_name)

flavor = nova.flavors.find(name=flavor)

import os
import subprocess

def ansiblemaster():
        path = "/home/ubuntu/"

        os.chdir( path )
        os.system("  git clone https://github.com/QTLaaS/QTLaaS.git")        
        #
        path1 = "/home/ubuntu/QTLaaS/"

        os.chdir( path1 )
        os.system('./ansible_install.sh')
        #path1 = "/home/ubuntu/acc10/"

        #os.chdir( path1 )
        #os.system('ls')
        

        path = "/home/ubuntu/.ssh"
        os.chdir( path )
        #os.system('ls')
        os.system('ssh-keygen') 











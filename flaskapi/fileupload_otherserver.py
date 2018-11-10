from datainit import *

#### this module file upload other server

def uploadserver():

   
   filePath = "/home/ubuntu/"
   serverPath = "/home/ubuntu/"
   os.system("scp "+filePath+" ubuntu@servername:"+serverPath)   

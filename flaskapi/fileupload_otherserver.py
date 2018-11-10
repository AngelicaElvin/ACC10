

def uploadserver():

   
   filePath = "/home/ubuntu/"
   serverPath = "/home/ubuntu/"
   os.system("scp "+filePath+" ubuntu@servername:"+serverPath)   

import os
import shutil

class FileSystem():
    
    def copy(self,*paths):
        shutil.copyfile(*paths)
    
    def move(self,*paths):
        shutil.move(*paths)
    
    def delete(self,dest):
        os.remove(dest)
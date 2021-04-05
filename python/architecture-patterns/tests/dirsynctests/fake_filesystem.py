class FakeFileSystem(list):
    
    def copy(self,src,dest):
        self.append(('copy',src,dest))
    
    def move(self,src,dest):
        self.append(('move',src,dest))
    
    def delete(self,src,dest):
        self.append(('delete',src,dest))
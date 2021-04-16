import abc
from allocation.domain.Batch import Batch

# port pattern
class AbstractRepository(abc.ABC):
    
    @abc.abstractclassmethod
    def add(self,batch:Batch):
        raise NotImplementedError
    
    @abc.abstractclassmethod
    def get(self,batch: Batch):
        raise NotImplementedError
    
# adapters pattern
class BatchRepository(AbstractRepository):
    
    def __init__(self,session) -> None:
        self.session=session
    
    def add(self,batch):
        self.session.add(batch)
    
    def get(self,reference):
        return self.session.query(Batch).filter_by(reference=reference).one()
    
    def list(self):
        return self.session.query(Batch).all()
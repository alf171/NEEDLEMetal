import cpu_backend
import numpy as np




# possibly not best class struct 
# I might decentralize everything
class  Needle():
    def __init__():
        pass

    class Tensor():
        def __init__(self, array, dtype = "float32", device="cpu"):
            self.shape = None
            self.dtype = dtype
            self.device = "mps" if (device == "mps") else "cpu"
            self.array = self.create_data_struct(self, array)
            self.dtype = dtype

        # for now we are a python list so this is fine
        def __str__(self):
            return str(self.array)

        # if i want a better debug print - maybe I'll use numpy for this
        def __repr__(self):
            pass

        @staticmethod
        def create_data_struct(self, array):
            if(self.device == "cpu"):
                if(isinstance(array, list)): # ND array
                    shape = []
                    current_level = array
                    while(isinstance(current_level, list)):
                        shape.append(len(current_level))
                        current_level = current_level[0] if len(current_level) > 0 else [] 
                    self.shape = shape
                    return cpu_backend.CPUBackend(array, self.shape)
                else:
                    raise ValueError("Tensor data must be a list") 

            raise ValueError("Only CPU is currently implemented") 

    class Op():

        def scalar_add(self, a, scalar):
            if not isinstance(a, Needle.Tensor):
                raise ValueError("Argument is not a supported tensor")
            return a + scalar
        


x = Needle.Tensor([1,2,3])
print(x)
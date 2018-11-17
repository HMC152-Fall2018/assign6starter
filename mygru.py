import torch
import torch.nn as nn

class MyGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1,
                dropout=0):
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.weight_ih_l0 = nn.Parameter(torch.Tensor(hidden_size * 3, input_size))
        # ...
        self.init_hidden()
        
    def init_hidden(self):
        # Initialize weights and biases here
        pass

    def forward(self, inp, h_0):
        seq_len = inp.shape[0]

        # iterate seq_len times, calculating h_i at each timestep
        for i in range(seq_len):  
            # Calc r, z, n, h_i here
            pass
        # output = ...
        # h_t = ...
        return (output, h_t)

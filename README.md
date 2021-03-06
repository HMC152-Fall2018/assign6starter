# CS 152
# Assignment 6
# November 14, 2018
##  Due Tuesday, November 20, 2018, 11 PM


 
The goal in this assignment is to create a replacement for [nn.GRU](https://pytorch.org/docs/0.3.1/nn.html?highlight=gru#torch.nn.GRU). The parameters for the GRU constructor are:

* ```input_size``` – The number of expected features in the input x
* ```hidden_size``` – The number of features in the hidden state h
* ```num_layers``` – Number of recurrent layers.
* ```bias``` – If False, then the layer does not use bias weights b_ih and b_hh. Default: True
* ```batch_first``` – If True, then the input and output tensors are provided as (batch, seq, feature)
* ```dropout``` – If non-zero, introduces a dropout layer on the outputs of each RNN layer except the last layer
* ```bidirectional``` – If True, becomes a bidirectional RNN. Default: False

You only need to implement ```input_size``` and ```hidden_size``` (other parameters should be accepted, but may be silently ignored).  For extra credit, implement ```num_layers```, ```dropout```, and/or ```bidirectional```.

FYI, my implementation was about 50 lines of code.


As a testbed, use the [dickens.ipynb notebook](https://github.com/nrhodes/cs152/blob/master/notebooks/dickens.ipynb) from the cs152 repository, replacing ```nn.GRU``` with your ```MyGRU```.

### Groups
You may work by yourself or in groups of 2. All work in a group should be done with the group members physically working together.

Outside resources: You may use any pytorch and fastai documentation and general web resources on using the two libraries. You should not look at the source code of PyTorch's GRU. 

### What to turn in
A notebook named Assignment6.ipynb which is a copy of dickens.ipynb modified to use your new MyGRU class. Please make sure your notebook includes the output of the training loop so I can see the losses.  You can adjust the 2nd parameter of learn.fit from 7 to 5 to reduce the number of epochs that are trained.  If you run out of GPU memory, you'll want to reduce the batch size.

### Suggestions

* The [documentation for nn.GRU](https://pytorch.org/docs/0.3.1/nn.html?highlight=gru#torch.nn.GRU) is extremely helpful. Pay careful attention to shapes of incoming and outgoing values.

* The debugger is your friend.  To use it, import:

```from IPython.core.debugger import set_trace```

And then call ```set_trace()``` wherever you’d like a breakpoint.

* Be extremely clear about the shapes of everything.


* Useful PyTorch calls:
    * ```nn.init.normal```
    * ```nn.init.constant```
    * ```torch.mm```
    * ```torch.sigmoid```
    * ```torch.tanh```
    * ```torch.stack```
    * ```torch.unsqueeze```

* Running on a non-GPU machine:
    * It can be hard to start a GPU instance (the us-west1-b zone seems to run out of GPU instances at some times). You can always
create a non-GPU instance and reinstall the software (see [GoogleComputeEngineSetup.md](https://github.com/nrhodes/cs152/blob/master/GoogleComputeEngineSetup.md) for details.
Your notebook will work; training will just be slow.
    * You may find it useful to install PyTorch and fastai on your local machine.
This way, you can do all of your implementation of MyGRU without having to spin up a GCE instance. In order to do so, you'll need to
pick and choose the commands to run from the [GCE install script](https://github.com/nrhodes/cs152/blob/master/bin/GoogleComputeEngineSetup.sh).

* Take a look at the [source code for Embedding](https://github.com/pytorch/pytorch/blob/v0.3.1/torch/nn/modules/sparse.py), a fairly simple module.

### Starter code
As of Saturday, November 17, at 2:45 PM, I've created a unit testcase that can be used to see what GRU does, and can also be used as a beginning to test your implementation.  
In addition, I've created a skeleton of MyGRU showing the methods, and giving an idea of the inputs and outputs.
These two files are part of the [assign6starter repository](https://github.com/HMC152-Fall2018/assign6starter); you should be able to just do a ```git pull``` to get them.



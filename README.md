

<img src="http://minitorch.github.io/_images/minitorch.svg">

This repo is the full student code for minitorch. It is designed as a 
single repo that can be completed part by part following the guide book. 
It uses GitHub CI to run the tests for each module. 

* [Full Guide](http://minitorch.github.io) 

MiniTorch is a *diy teaching library*
for machine learning engineers who wish to learn about the internal
concepts underlying deep learning systems.  It is a pure Python
re-implementation of the [Torch](http://www.pytorch.org) API
designed to be simple, easy-to-read, tested, and incremental. The
final library can run Torch code. The project was developed for the
course 'Machine Learning Engineering' at Cornell Tech.

To get started, first read [setup](http://minitorch.github.io/setup) to
build your workspace.  Then follow through each of the modules to the
right. Minimal computational resources are required.
Module starting code is available on GitHub, and each proceeds
incrementally from past modules.

Enjoy!

Sasha Rush ([@srush_nlp](https://twitter.com/srush_nlp)) with Ge Gao and Anton Abilov

Topics covered:

* Basic Neural Networks and Modules
* Autodifferentiation for Scalars
* Tensors, Views, and Strides
* Parallel Tensor Operations
* GPU / CUDA Programming in NUMBA
* Convolutions and Pooling
* Advanced NN Functions


# Setup


### Clone repo
```bash
git clone https://github.com/the-sergiu/minitorch
```

### Install conda and create conda environment
Python 3.7 seems to be working best.
```bash
conda create -n minitorch python=3.7
```



### Activate environment
```bash
conda deactive
conda activate minitorch
```

### Install dependencies (except Torch)
```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements.extra.txt
python -m pip install -Ue .
```

### Install Torch and CUDA support
Should work well, but feel free to try out newer versions of PyTorch or CUDA drivers.
```bash
pip3 install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio===0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
```

### Verify that installation succeeded
```bash
python -c "import minitorch"
python -c "import torch"
```

### Final steps
From here, check out the official guide found above.

To run tests, go to repo directory, and from the tests folder run:
```bash
# cd path\to\repo\minitorch\tests
pytest
```

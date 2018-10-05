

## Installation

### Edit mode using python virtual environment (likely use case while in active development) 

See below for install of pre-built "source distribution" packages.

For development Python virtual environments are recommended.  
(See venv documentation [here](https://docs.python.org/3/library/venv.html) and [here](https://docs.python-guide.org/dev/virtualenvs/))

The workflow for this is

    0. Ensure virtualenv has been installed via pip:
    '$ pip3 install virtualenv'

    1. Create a virtualenv:
    '$ python3 -m venv /path/to/new/virtual/environment'
    E.g.
    '$ python3 -m venv ~/Envs/mpcvenv/'

    2. Activate the virtualenv:
    E.g.
    '$ source ~/Envs/mpcvenv/bin/activate'

*Some of this is dependent on your local distro/install and needs to be detailed for individual systems.*

The root or sysadmin account (*i.e.* `sudo`) is not needed to install or use a virtual environment.
Keep in mind that the directories where python packages are installed are dependent on the version
of python you are running.


For development purposes, one can use `pip -e` for "editable mode."
(See [editable-installs](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs).)


The workflow for this is

   1. Go to location on your filesystem where you want code to be. E.g. the new virtual environment you made
    'cd ~/Envs/mpcvenv/'
   
   2. Clone the mpc git repository. E.g.
      'git clone https://YOURACCOUNT@bitbucket.org/mpcdev/mpcpp.git'
      
   3. cd to the cloned repository root, then `pip install -e .`  or on CF machines `pip install --user -e .` 
   
   4. cd down one directory to tests, then `pip install -e .`  or on CF machines `pip install --user -e .`  again.
   
   5. Ensure you have an ele220 installed, either from the source distribution or with -e. 
      E.g. for now `pip install --user https://minorplanetcenter.net/pkg/ele220-0.0.0.tar.gz` but this will change as Sonia updates 
      
   6. Then can run tests from *anywhere* by doing (see below for more details on testsing, etc)
      `pytest --pyargs mpcpp_tests`


### Standard "Source Distribution" Installation: Executive summary

This does a "standard install" of mpcpp just as one does for a standard python package like `numpy`.
This makes a package that you can easily call, but it is *not* editable. 
The package may also be "old" in the sense of not having the latest edits in it made on bitbucket. 

    sudo pip3 install -r https://minorplanetcenter.net/pkg/mpcpp
    
or on CF managed machines the following seems to work ... 

    pip install --user -r https://minorplanetcenter.net/pkg/mpcpp

To test everything that's been installed (can run this from anywhere)

	python3 -m pytest --pyargs mpcpp_tests



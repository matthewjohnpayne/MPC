# MPC
WIP development of Minor Planet Center code for propagation of orbits, fitting of detections, attribution of objects, and other related functionalities.

MJP: 2018/10

Trying to get in place:
(i) package-and-module structure
(ii) structure of some modules 

Going to intially work towards implementing a working MPChecker

 - This will require there exist various supporting modules/packages

 - Initially, these supporting modules/packages can be inefficient/clunky

## Project Code Repository
Code is in the [GitHub hosted Git repository](https:??????????).

Note that there is significant heritage from the [BitBucket hosted Git repository](https://bitbucket.org/mpcdev/mpcpp/). 

When you have cloned the repository to your computer's file system, you will find the Python package source tree 
begins in the directory `src/mpc` under the repository root.


## Package Tests 
Python test modules are provided as a separate package. 
They perform validations of MPC subpackage functionality.
In the source repository they are located under [tests](?????????????).

See README\_TESTS.md for more detail on testing.



## Installation

See README\_INSTALL.rst for more detail on installation.


### Requirements

A `pip` *requirements* file indicates the required packages to install.  
The [MPCPP requirements file](https://minorplanetcenter.net/pkg/mpcpp) currently lists these packages:

https://minorplanetcenter.net/pkg/ele220-0.0.0.tar.gz
https://minorplanetcenter.net/pkg/mpcpp-0.1.tar.gz
https://minorplanetcenter.net/pkg/mpcpp_tests-0.1.tar.gz

Instead of installing all three at once with `pip -r`, each package could be installed
with an individual command:

	pip install https://minorplanetcenter.net/pkg/ele220-0.0.0.tar.gz
    pip install https://minorplanetcenter.net/pkg/mpcpp-0.1.tar.gz
    pip install https://minorplanetcenter.net/pkg/mpcpp_tests-0.1.tar.gz


Credits
-------

- `Distribute`_
- `Buildout`_
- `modern-package-template`_

.. _Buildout: http://www.buildout.org/
.. _Distribute: http://pypi.python.org/pypi/distribute
.. _`modern-package-template`: http://pypi.python.org/pypi/modern-package-template

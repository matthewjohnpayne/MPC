from setuptools import setup, find_packages
import sys, os

here    = os.path.abspath(os.path.dirname(__file__))
README  = open(os.path.join(here, 'README.md')).read()
NEWS    = open(os.path.join(here, 'NEWS.txt')).read()
LICENSE = open(os.path.join(here, 'LICENSE')).read()


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(name='mpc',
    version=version,
    description="Minor Planet Center Orbit Propagation and Determination",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='nbody orbits asteroids attribution',
    author='Matthew Payne',
    author_email='matthewjohnpayne@gmail.com',
    url='',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['mpc=mpc:main']
    }
)

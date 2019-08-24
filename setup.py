import setuptools
from setuptools import setup, find_packages

setup(
        name='BiNE',
        version='1.0',
        description='BiNE',
        author='Gao et al.',
        author_email='mgao@dase.ecnu.edu.cn',
        url='https://github.com/clhchtcjj/BiNE',
        packages=['bine'],
        package_dir={'bine': 'bine'},
        scripts=['bine/train_bine.py']
    )


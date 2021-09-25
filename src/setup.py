"""erc20transfer"""

from setuptools import setup, find_packages

setup(
    name='caaj_evm',
    version='0.1.0',
    license='mit',
    description='tools for generateing caaj',

    author='bitblt',
    author_email='hogehoge@gmail.com',
    url='None.com',

    packages=find_packages(where='erc20transfer'),
    package_dir={'': 'erc20transfer'},
)


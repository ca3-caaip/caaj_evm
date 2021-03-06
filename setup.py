"""erc20transfer"""

from setuptools import setup, find_packages
from glob import glob

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='caaj_evm',
    version='0.1.8',
    license='mit',
    description='tools for generateing caaj',

    author='bitblt',
    author_email='ywakimoto1s@gmail.com',
    url='https://github.com/ca3-caaip/caaj_evm',

    install_requires=_requires_from_file('requirements.txt'),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')] 
)


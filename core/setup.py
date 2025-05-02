from setuptools import find_packages, setup
from os import path as osp, system as runcmd
import nestpython as nsp

def parse(filename):
    return osp.join(osp.dirname(__file__), filename)

def read(filename):
    return open(parse(filename), 'r').read()


param = eval(read('param.i'))

version = param['version']
test = param['test']

nsp.files.nbuild('/spherica-npy', '/spherica', erase_dir=True, transfer_other_files=True)

with open(parse('../README.md'), 'r') as f, open(parse('README.md'), 'w') as fn:
    readme = f.read()
    fn.write(readme)

    setup(
        name='spherica',
        packages=find_packages(include=['spherica']),
        version=version,
        description='n-complex numbers (Tessarines) in Python',
        author='corruptconverter, slycedf, goblinovermind, jerridium',
        install_requires=[],
        license='MIT',
        long_description=readme,
        long_description_content_type='text/markdown',
        classifiers=["Development Status :: 3 - Alpha"]
    )

token = open(f'D:/slycefolder/ins/tsr/{ {True: "tt", False: "tr"}[test]}', 'r').read()

runcmd(
    f'pause & twine upload --repository { {True: "testpypi", False: "pypi"}[test]} dist/*{version}* -u __token__ -p {token} --verbose')

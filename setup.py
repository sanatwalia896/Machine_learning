from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path)->List[str]:
    '''
    this function will return list of required packages 
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','')for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="ai_project",
    version='0.0.1',
    author='Sanat',
    author_email='waliasanat896@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'))

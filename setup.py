from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT ='-e .'

#defining a function
def get_requirements(file_path:str)->List[str]:
    '''
    this function will retirn the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Aryan',
    author_email ='dipuaryan1111@gmail.com',
    # yesle init.py ka xa vanerw khojera import garxa
    packages=find_packages(), 
    install_requires =get_requirements('requirements.txt')
)
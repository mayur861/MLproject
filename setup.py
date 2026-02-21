from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def requirements(file_path:str)->List[str]:

    ''' this funtion will return for the list of requirements'''

    requirements=[]
    with open(file_path) as file_obj:
        requirements =file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = 'MLproject',
    version = '0.0.1',
    author = 'mayur861',
    author_email = 'mayurbirla907@gmail.com',
    packages = find_packages(),
    install_requires = requirements('requirements.txt')

)

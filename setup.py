from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:

    requirements=[]
    HYPHEN_E_DOT = "-e ."
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(
    name = 'ML Project',
    author = 'ryalisirisha',
    email = 'ssryali07@gmail.com',
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')

)
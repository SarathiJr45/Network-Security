from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    
    """This func will return the list of requirements
    """
    requirements_lst:List[str]=[]
    try:
        with open("requirements.txt","r") as f:
            
            lines= f.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!="-e .":
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found") 
        
    return requirements_lst
            
setup(
    name="networksecurity",
    version="0.0.1",
    author="Sarathi",
    author_email="sarathisjr@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
    
"""
    The setup.py file is an essential paet of packaging and distributing Python projects.
    It is used by setuptools (or distributils in older Python versions) to install your package,
    and to define the configuration of my project, such as its metadata, dependencies, and more.
"""

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    ## This function will return list of requirements from requirements.txt file 
    requirement_list:List[str] = [] 
    try:    
        with open('requirements.txt', 'r') as file:
            ## read Line from the file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## Ignore empty line and '-e .'
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
   
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name = "Spotify Song Recommender",
    version = "0.0.1",
    author = "Ranjan",
    author_email = "ranjandasbd22@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
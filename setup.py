from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) ->List[str]:
    """This function will return list of requirements"""
    requirements= []
    with open(file_path) as file_obj:
        requirements =file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements
    

setup(
    name='end2end_ML_Project',
      version='0.0.1',
      author='ajay',
      author_email='ajayzate77@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements('requirements.txt'),

      )
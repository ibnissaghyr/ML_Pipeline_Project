from setuptools import find_packages,setup
from typing import List

HYPHON_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        if HYPHON_dot in requirements:
            requirements.remove(HYPHON_dot)

setup(name="ML Project",
      version='0.0.1',
      description="Machine_learning_pipeline",
      author="Hicham",
      author_email="ibnissaghyrhicham@gmail.com",
      packages=find_packages(),
      install_packages=get_requirements())

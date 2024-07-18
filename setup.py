from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path : str)->List[str]:
    requiremets=[]
    with open(file_path, 'r') as f:
        requiremets= f.readline()
        requiremets=[req.replace("\n","") for req in requiremets]

        if HYPEN_E_DOT in requiremets:
            requiremets.remove(HYPEN_E_DOT)

setup(
    name='ML_Project',
    version='0.0.1',  # Version number should be a string
    author='Raj',
    author_email='rajbhongade4@gmail.com',
    description='A machine learning project',  # Adding a description
    packages= get_requirements('requirements.txt'),
    license='MIT',  # Including a license (adjust as needed)
)
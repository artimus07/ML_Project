from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Raj',
    author_email='rajbhongade4@gmail.com',
    description='A machine learning project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    license='MIT',
)

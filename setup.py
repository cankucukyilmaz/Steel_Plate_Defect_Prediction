from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Steel_Plate_Defect_Prediction',
    version='0.1',
    author='Can',
    author_email='canthecomputerscientist@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
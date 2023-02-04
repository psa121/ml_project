from setuptools import find_packages, setup
from setuptools import setup
from typing import List

requriment_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirements()->List[str]:
    with open(requriment_file_name) as requirement_file:
        requriment_list = requirement_file.readlines()
    requriment_list = [requriment_name.replace("\n", "") for requriment_name in requriment_list]

    if REMOVE_PACKAGE in requriment_list:
        requriment_list.remove(REMOVE_PACKAGE)
    return requriment_list

setup(name='INSURANCE',
      version='0.0.1',
      description='Insurance Industry lavel project',
      author='AMAN SHARMA',
      author_email='psa121pandit@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements())
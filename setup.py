# Basic configuration information to set up the wheel
from setuptools import find_packages, setup

def requirements(infile):
	with open(infile) as file:
		packages = file.read().splitlines()
		return [package for package in packages if not package.startswith('#') and len(package.strip()) > 0]

setup(
	name='journalmapnlp',
	description='Library to provide basic functionality for determining article study location from raw article text body',
	packages=find_packages(),
	install_requires=requirements('requirements.txt'),
)

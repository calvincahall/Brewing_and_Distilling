from setuptools import setup, find_packages
pypi_dependencies = ['numpy']
setup(name='BrewUtilities',
	version=0.1,
	description='Brew Utilities for calculating brew day information (i.e. volume water needed, final alcohol content).',
	url='',
	author='Calvin Cahall',
	author_email='calvin.cahall10@gmail.com',
	license='',
	packages=find_packages(include=['BrewUtilities']),
	zip_safe=False,
	install_requires=pypi_dependencies)
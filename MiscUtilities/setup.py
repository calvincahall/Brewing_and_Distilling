from setuptools import setup
pypi_dependencies = ['numpy','scipy']
setup(name='MiscUtilities',
	version=0.1,
	description='Misc. Utilities for unit conversions, and other calculations helpful in brewing and distilling.',
	url='',
	author='Calvin Cahall',
	author_email='calvin.cahall10@gmail.com',
	license='',
	packages=['./'],
	zip_safe=False,
	install_requires=pypi_dependencies)

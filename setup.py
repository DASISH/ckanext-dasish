from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-dasish',
	version=version,
	description="A ckan extension for the DASISH project",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Binyam Gebrekidan Gebre',
	author_email='bingeb@mpi.nl',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.dasish'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	dasish=ckanext.dasish.plugin:DasishPlugin
	""",
)

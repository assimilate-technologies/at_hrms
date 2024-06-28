from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in business_theme_v14/__init__.py
from at_hrms import __version__ as version

setup(
	name="at_hrms",
	version=version,
	description="HRMS From Assimilate Technologies",
	author="Assimilate Technologies",
	author_email="developer@assimilatetechnologies.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in printechs_website/__init__.py
from printechs_website import __version__ as version

setup(
	name="printechs_website",
	version=version,
	description="Website",
	author="Printechs",
	author_email="info@printechs.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

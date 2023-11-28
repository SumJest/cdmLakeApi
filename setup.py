from setuptools import setup, find_packages

DESCRIPTION = 'API for accessing the data lake'
LONG_DESCRIPTION = 'API for accessing the data lake of CDM project'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="lakeApi",
    version='0.9.0',
    author="Roman Fakhrutdinov",
    author_email="<summedjesters@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['aiohttp~=3.8.5', 'setuptools'],
)

from setuptools import setup, find_packages

install_requires=[
   'rdflib>=6.0.2,<=6.0.2'
]

setup(name='fredclient', version='1.0.0',
    packages=find_packages(), install_requires=install_requires)
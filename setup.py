from setuptools import setup, find_packages

setup(
    name='kholmatov-sdk',
    version='0.1',
    description='A Python SDK for the Lord of the Rings API',
    packages=find_packages(),
    install_requires=[
        'requests',
        'requests_mock'
    ],
)

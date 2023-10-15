from setuptools import setup, find_packages

setup(
    name='myapi',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'myapi-cli = myapi.api_client:main',
        ],
    },
    author='foglib',
    author_email='foglibiotcs3@email.com',
    description='Fog computing enabling lib for ioT',
)

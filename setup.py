from setuptools import setup, find_packages
import listdates

setup(
    name='listdates',
    version=listdates.__version__,
    author='guan ming',
    author_email='i@guanming.me',
    packages=find_packages(),
    description='A tools that list all dates in the given range',
    entry_points=dict(
        console_scripts=[
            'listdates = listdates:main',
        ],
    ),
)

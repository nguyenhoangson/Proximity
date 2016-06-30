from setuptools import setup, find_packages

setup(
    name='Proximity',
    version='0.1',
    description='Proximity Package',
    keyword='Proximity',
    url='http://github.com/',
    author='Nguyen Hoang Son',
    author_email='nguyenhoangson@example.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['scipy>=0.17.0', 'numpy>=1.10.4', 'python>=3.5'],
    zip_safe=False)

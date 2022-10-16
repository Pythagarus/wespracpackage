from setuptools import setup, find_packages

setup(
    name='wespracpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='My first package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='',
    author='Wesley Naidoo',
    author_email='wesleyn@discovery.co.za'
)

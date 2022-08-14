from setuptools import setup, find_packages

setup(name='tempy',
      version='0.1',
      url='https://github.com/GreatPack/tempy',
      license='MIT',
      author='GreatPack',
      author_email='m6338687@gmail.com',
      description='a simple package that allows you to convert Celsius to Fahrenheit, and vice versa',
      packages=find_packages(exclude=['tests']),
      zip_safe=False)

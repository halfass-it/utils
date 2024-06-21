from setuptools import setup, find_packages

setup(
  name='utils',
  version='0.5.1',
  python_requires='>=3.6, <4.0',
  packages=find_packages(),
  install_requires=[
    'loguru',
  ],
)

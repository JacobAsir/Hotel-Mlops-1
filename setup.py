from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(

    name = "mlops test",
    version= 0.1,
    author = "Jacob",
    packages = find_packages(),
    install_requires = requirements
)
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_package_Theodoro_Fraga_DIO",
    version="0.0.4",
    author="Theodoro Fraga",
    author_email="theodorofragadecastro.dev@gmail.com",
    description="A simple image processing package for educational purposes.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tedtheotheodoro/simple-package-template.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
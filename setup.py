from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_descriprion = f.read()

setup(
    name="pgbackup",
    version="0.1.0",
    author="Einar Kazakov",
    author_email="services1620@protonmail.com",
    description="A utility for backing up PostgreSQL databases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kazakoveinar/pgbackup",
    package=find_package("src")
)

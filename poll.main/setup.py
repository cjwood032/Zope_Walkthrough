from setuptools import setup, find_packages

setup(
    name="poll.main",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["poll"],
    install_requires=["setuptools",
                      "Zope"],
    )
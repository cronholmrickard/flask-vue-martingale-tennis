import os
from setuptools import setup, find_packages

# get __version__ from _version.py
base_dir = os.path.dirname(os.path.realpath(__file__))
ver_file = os.path.join(base_dir, "martingale_backend", "_version.py")
with open(ver_file) as f:
    exec(f.read())


setup(
    name = "martingale_backend",
    version=__version__,
    author="Rickard Cronholm",
    author_email="rickard.cronholm@gmail.com",
    description="A Falsk RESTful backend for a martingale demonstrator",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=True,
)

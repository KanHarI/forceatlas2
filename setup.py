from setuptools import setup, Extension
from os import path

print("Installing fa2 package (fastest forceatlas2 python implementation)\n")

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), 'r') as f:
    long_description = f.read()

# Use pre-generated C files for the extension
ext_modules = [
    Extension(
        "fa2.fa2util",
        ["fa2/fa2util.c"],  # Only use the .c file
    )
]

setup(
    name="fa2",
    version="0.3.5",
    description="The fastest ForceAtlas2 algorithm for Python (and NetworkX)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bhargav Chippada",
    author_email="bhargavchippada19@gmail.com",
    url="https://github.com/bhargavchippada/forceatlas2",
    download_url="https://github.com/bhargavchippada/forceatlas2/archive/v0.3.5.tar.gz",
    keywords=["forceatlas2", "networkx", "force-directed-graph", "force-layout", "graph"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["fa2"],
    install_requires=["numpy", "scipy", "tqdm"],
    extras_require={
        "networkx": ["networkx"],
        "igraph": ["python-igraph"],
    },
    include_package_data=True,
    ext_modules=ext_modules,  # Use only pre-generated C files
)

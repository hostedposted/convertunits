import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="convertunits",
    version="1.0.4",
    author="Hostedposted",
    author_email="hostedpostedsite@gmail.com",
    description="Convert units in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hostedposted/convertunits",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
)
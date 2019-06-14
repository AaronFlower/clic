import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='clic',
    version='0.1',
    scripts=['clic'],
    author="AaronFlower",
    author_email="haojunzhan@gmail.com",
    description="A c/c++ cli ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aaronflower/clic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

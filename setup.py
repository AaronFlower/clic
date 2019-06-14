import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='clic',
    version='0.1',
    # scripts=['clic'],
    author="AaronFlower",
    author_email="haojunzhan@gmail.com",
    description="A c/c++ cli ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AaronFlower/clic",
    # packages=setuptools.find_packages(),
    # include_package_data with MANIFEST.in to include data files.
    include_package_data=True,
    packages=['clic'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "clic=clic.clic:main",
        ]
    },
)

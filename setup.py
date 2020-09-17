import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fileGL", # Replace with your own username

    version="1.2.0b1",


    author="Abishek Sriram",
    author_email="abisheksriram2001@gmail.com",
    description="File organiser with many ways",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abisheksriram/fileGL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        
    ],
    python_requires='>=3.6',
)
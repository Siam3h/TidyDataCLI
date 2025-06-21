from setuptools import setup, find_packages

setup(
    name="TidyDataCLI",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # only add the ones suitable for a user to use
    ],
    entry_points={
        "console_scripts": [
            "tidydata = src.cmd:main",
        ],
    },
    test_suite="tests",
    author="Philbert Siama",
    author_email="siamaphilbert@outlook.com",
    description="A CLI tool to automate cleaning, report generation, transformation and visualisation of CSV data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Siam3h/TidyDataCLI.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">3.9",
)

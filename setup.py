from setuptools import setup, find_packages

setup(
 name="TidyDataCLI",
 version="0.2.0",
 packages=find_packages(),
 install_requires=[
     "pandas",
     "matplotlib",
     "openpyxl",
     "argparse"
 ],
 entry_points={
     "console_scripts": [
         'tidydata = app.cmd:main',
     ],
 },
 test_suite='tests',
 author="Philbert Siama",
 author_email='siamaphilbert@outlook.com',
 description="A CLI tool to automate cleaning, transformation and visualisation of Excel/CSV data.",
 long_description=open('README.md').read(),
 long_description_content_type="text/markdown",
 url="https://github.com/Siam3h/TidyDataCLI.git",
 classifiers=[
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Operating System :: OS Independent",
 ],
 python_requires='>3.9',
)

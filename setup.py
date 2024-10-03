from setuptools import setup, find_packages

setup(
 name="TidyDataCLI",
 version="1.0.0",
 packages=find_packages(),
 install_requires=[
        "pandas==2.2.2",
        "matplotlib==3.9.2",
        "openpyxl==3.1.5",
        "numpy==2.0.1",
        "seaborn==0.13.2",
        "requests==2.32.3",
        "python-dateutil==2.9.0.post0",
        "pytz==2024.1",
        "colorama==0.4.6",
    ],
 entry_points={
     "console_scripts": [
         'tidydata = src.cmd:main',
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

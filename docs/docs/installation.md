#### Requirements

* `Python 3.7 or higher`: Required for native installation. <br>
* `Pip`: Python package manager for installing dependencies.  <br>
* `Docker (Optional)`: For containerized execution. <br>

#### Install via pip
The simplest way to install TidyDataCLI is using pip. <br>

`pip install TidyDataCLI`

#### Install from Source
To install from the source code:<br>

Clone the repository: `git clone https://github.com/Siam3h/TidyDataCLI`


Navigate to the repository directory: `cd tidydatacli`


Install the package: `pip install`

#### Running with Docker
For users preferring a containerized environment: <br>

Pull the Docker image: `docker pull tidydatacli`


Run the tool, mounting the current directory to, <br> Example: `/data:docker run -v $(pwd):/data tidydatacli tidydata <command> --input /data/input.csv --output /data/output.csv`


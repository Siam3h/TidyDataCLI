## Installation

### Requirements

- Python 3.7 or higher
- Pip (Python package installer)
- Docker (optional)

### Install via `pip`

Install the latest version of TidyDataCLI using pip:

```bash
pip install TidyDataCLI
```

### Install from Source

To install TidyDataCLI from the source:

1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/Siam3h/tidydatacli.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tidydatacli
   ```
3. Install the package locally:
   ```bash
   pip install .
   ```

### Running via Docker

If you prefer not to install Python dependencies, you can run TidyDataCLI inside a Docker container.

1. Pull the Docker image:
   ```bash
   docker pull tidydatacli
   ```
2. Run the CLI commands from the container:
   ```bash
   docker run -v $(pwd):/data tidydatacli tidydata <command> --input /data/input.csv --output /data/output.csv
   ```

# CnameSnoop


Usage

    python cnamesnoop.py [-d DOMAIN] [-l FILE] [-H]

## Features

- Retrieve the CNAME of a single domain
- Retrieve CNAME for multiple domains listed in a file
- Built with Python and DNS resolver library for fast and accurate results

## Requirements

    Python 3.x
    dns library (install using pip install dnspython)

## Installation
- Clone the repository:

      git clone https://github.com/iRoyall/cnamesnoop.git
      cd cnamesnoop

### Install the required dns library:

    pip install dnspython

### How to Use

- To retrieve the CNAME record for a single domain, use the -d or --domain option followed by the domain name:

      python CSnoop.py -d example.com

- To retrieve CNAME records for multiple domains listed in a file, use the -l or --list option followed by the path to the file:

      python CSnoop.py -l domains.txt

- To display the help message, use the -H or --helpmsg option:

      python CSnoop.py -H

# Examples

### Retrieve CNAME for a single domain
    python CSnoop.py -d example.com

### Retrieve CNAME for multiple domains listed in a file
    python CSnoop.py -l domains.txt

### Display help message
    python CSnoop.py -H

Contributing:

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request.

# Animal Web Generator

## Overview

This animal web generator application retrieve animal data from external ninjas API, process it and generate pretty a
HTML file. 

## Features

- **Fetch Animal Data**: Retrieve data from an external animal data from ninjas API.
- **Format Data**: Convert the fetched data into an HTML format.
- **Generate HTML File**: Create and save an HTML file with animal information.

## Requirements

Ensure you have the following Python packages installed:

- `certifi==2024.7.4`
- `charset-normalizer==3.3.2`
- `idna==3.7`
- `python-dotenv==1.0.1`
- `requests==2.32.3`
- `urllib3==2.2.2`

You can install these dependencies using the `requirements.txt` file:

```sh
pip install -r requirements.txt
```
## Setup

### Clone the Repository
Clone this repository to your local machine:

```sh
git clone https://github.com/narayanghimire/My-Zootopia.git
cd My-Zootopia
```

### Install Dependencies
Install the required Python packages:
```sh
pip install -r requirements.txt
```
### Configure Environment Variables
Create a .env file in the root directory of the project and add your API key. The .env file should contain:
```
API_KEY=your_api_key_here
```

### Run the Application
```
python3 animal_web_generator.py
```

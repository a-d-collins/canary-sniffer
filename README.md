# canary-sniffer
Scratches and/or sniffs (a mocked version of) the HouseCanary api for home details.

This projects provides a simple flask api for retrieving sewer system data from a MOCKED version of the HouseCanary api. A Postman mock server was utilized to mock the HouseCanary api. The mock server is private and requires an api key.

## Requirements
- Python 3.7+
- virtualenv
- config.py file (provided by repository contributor)

## Setup canary-sniffer (macOS):
1. Open up a terminal window.
2. Create and/or cd into a projects directory.
3. Use `git clone` to clone this repository.
4. Move a copy of your config.py file into the canary-sniffer directory.
5. Run the following commands:
```
$ pip install virtualenv
$ virtualenv sniff
$ source sniff/bin/activate
$ cd canary-sniffer
$ pip install -r requirements.txt
```

If no errors have occurred up to this point you are ready to run the application.

## Running canary-sniffer (macOS):
1. Open two terminal tabs/windows and, in each tab/window, `cd` into the canary-sniffer project directory.
2. In one of the terminal tabs/windows, start the flask server by running:
```
python api.py
```
3. In the other terminal tab/window, run:
```
python query.py
```
This will query the flask api.

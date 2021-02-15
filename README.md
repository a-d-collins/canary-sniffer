# canary-sniffer
Scratches and/or sniffs (a mocked version of) the HouseCanary api for home details.

This projects provides a simple flask api for retrieving sewer system data from a MOCKED version of the HouseCanary api and determining if a property has a septic system (if known). A Postman mock server was utilized to mock the HouseCanary api. The mock server is private and requires an api key.

## Requirements
- Python 3.7+
- virtualenv
- config.py file (provided by repository contributor)

## Setup canary-sniffer (macOS)
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

## Running canary-sniffer (macOS)
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

## Project notes
This was specifically designed in response to a coding challenge. If there was a real-world need for this, a few things would/could be done differently.

Firstly, the challenge prompt was focused on septic systems. The HouseCanary API contains a lot of other property details, so, in a real scenario (with more time), an immediate question one could ask about this task would be: why is our only query "does this property run on a septic system?"?

One could make the "intermediate web service" a little different by allowing it to handle more than just one question. For example, if you focus only on the question "does this property run on a septic system?" then you can make an endpoint like "/property/has-septic/" that takes an address/zip and then answers that question. That's it and that's what this repo accomplishes. However, if we wanted to make things more flexible we could have something like "/property/has-sewer-type" (or even "/property/has-attribute") where a variety of possible sewer values (or other possible property detail values) can be passed to that endpoint. The result of that, more flexible, endpoint would answer the questions similarly but it's more reusable and configurable. The trade-off is that it's not as simple and potentially allows for more mistakes on the caller's side of the code.

Secondly, regarding security, this application does utilize user authentication. Using a database and the directions in Flask-Login (https://flask-login.readthedocs.io/en/latest/), for example, could allow for user authentication for this api. That being said, this api is only meant to be a portion of a larger project. The larger project would, presumably, have its own form of authentication, so it made sense to not worry about that aspect.

Thirdly, project structure for this application was simplified due to the fact that it is intended to be part of a larger api.
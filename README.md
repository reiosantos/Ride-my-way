# Ride My Way

Ride-my App is a carpooling application that provides drivers with the ability to create ride offers and passengers to join available ride offers.

## Motivation

This is driven by the increase in technology, which has proven to be more effective in time saving.
We there fore develop this app to apply tech in the transportation industry with the main purpose of saving more and earnig more.

## Build status, and test coverage

Build status of continus integration i.e. travis, -
Test coverage of code climate and coveralls -

[![Build Status](https://travis-ci.org/reiosantos/Ride-my-way.svg?branch=develop)](https://travis-ci.org/reiosantos/Ride-my-way)
[![Maintainability](https://api.codeclimate.com/v1/badges/3b09b9ffe616d7ba85e4/maintainability)](https://codeclimate.com/github/reiosantos/Ride-my-way/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3b09b9ffe616d7ba85e4/test_coverage)](https://codeclimate.com/github/reiosantos/Ride-my-way/test_coverage)
[![Coverage Status](https://coveralls.io/repos/github/reiosantos/Ride-my-way/badge.svg?branch=develop)](https://coveralls.io/github/reiosantos/Ride-my-way?branch=develop)



***Features***

 * Users ==(Driver and pasenger)== can fetch all ride offers
 * Users c can fetch a specific ride offer
 * Driver creates a ride offer
 * Passengers make a request to join a ride.
 * Driver can deletes and update ride offer

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
- git : to update and clone the repository
- python3: The base language used to develop the api
- pip: a python package used to install project requirements
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```bash
Type: git clone https://github.com/reiosantos/ride-my-way.git in your terminal.
```
The UI folder houses the user interface. To access the user interface, open the login.html file inside the UI/templates folder


The api older contains the system backend services.

- To install the requirements. run:

```bash
pip install -r requirements
```

They can be run with the folowing commands.

```bash
cd api

python app.py
```

- Now you can access the system api via URL:

```http
http://localhost:5000/apis/v1/rides/
```

## Running the tests

- To run the tests, make sure you are working under api/, Then run the following commands

```bash
pytest
```

### And coding style tests

The tests carried out in the above commands, indicate the coverages for api endpoints


## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Python](https://www.python.org/) - Framework laguage
* HTML
* CSS

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Ssekitto Ronald** - *Initial work* - [reiosantos](https://github.com/reiosantos)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Andela Software Development Community
* Inspiration
* Bootcamp 9 team-mates

# Works Single View
This project has been made with [flask](https://github.com/pallets/flask), [flask-restx](https://github.com/python-restx/flask-restx) and [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy).

## Purpose

The purpose of this API is creating a Single View for a musical work. Each musical work is identified by its ISWC, in case the ISWC is not provided the title will be taken into account.
With this API you'll be able to maintain the works by sending POST requests or upload CSV files.
You'll also be able to get a CSV or a JSON with a GET request.

_Note: to be able to get the CSV you shouldn't use de Swagger interface, since it can't interpret the response correctly thus it won't download the file.
Fore more information please refer to the Swagger documentation at: [localhost:5000/{version}](http://localhost:5000/1.0)_

## Initialization
With simplification purposes the database and the server have been separated into two different Docker containers.
The project contains a Makefile with several commands that will simplify the management and development within it.

The steps to have the server working are the following:
1. `make start-db`
2. `make build`
3. `make db-upgrade`
4. `make start`

One that's done you'll have a running server at [localhost:5000](http://localhost:5000). Also you'll have the Swagger
documentation for the corresponding version of the API at [localhost:5000/{version}](http://localhost:5000/1.0).

## Testing

A unit + integration test is also provided in the [tests](https://github.com/aitorbouzas/workssingleview/tree/master/tests) directory. It covers, right now, a 92% of the server's directory code.

To run them all you can execute `make test` or `make test-coverage`.

## About the project

A [Clean Architecture](https://www.google.com/url?sa=i&url=https%3A%2F%2Fblog.cleancoder.com%2Funcle-bob%2F2012%2F08%2F13%2Fthe-clean-architecture.html&psig=AOvVaw0chTKvhMqcaw20TldeNmmX&ust=1591447297590000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLDM8KjZ6ukCFQAAAAAdAAAAABAD) approach has been selected as the most appropiate for this project. All the different layers
of this project are contained inside [server/business_layers](https://github.com/aitorbouzas/workssingleview/tree/master/server/business_layers).
The reason to pick this software architecture is that it provides a lot of decoupling between the different
components allowing us to change any part of it without compromising the rest and also, and most important,
that it will simplify the mocking and testing of the different layers (refer to: [tests](https://github.com/aitorbouzas/workssingleview/tree/master/tests)). My focus
was trying to produce a project that was the most production-ready possible, even though the API is very simple.
# iLabs Server

Core of iLabs

Build using Django and React

## Prerequisites
1. Python 3
2. [Pipenv](https://docs.pipenv.org/)

## Setting up
1. Install pre-requisites.
2. Clone this repository and cd into `server`.
3. Run `pipenv install --dev` to install all required packages.
4. Run `pipenv shell` to start a shell configured with required python version and packages.
5. Run `python manage.py migrate` to create the initial database structure.
6. Run `python manage.py runserver` to start the server.

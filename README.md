# Project Name

This is a small KittyStore. Has some functions as send message to any user, a CRUD for the items, etc.

## Requirements

- Python 3.9
- Django 4.2

## Setup

1. Clone this repository to your machine
2. Open a terminal in the project directory
3. Run `pip install -r requirements.txt` to install dependencies
4. Run `python manage.py migrate` to apply migrations
5. Run `python manage.py runserver` to start the server
6. Open your browser to `http://localhost:8000` to see the application in action

## Project Structure

- `manage.py` file: Django's main file
- `requirements.txt` file: file containing all project dependencies

## Users

In order for a demo version, you can use the superuser by default or create a new superuse

- Default superuser name: master
- Default superuser password: 123456789

Create a new superuser:

`python manage.py createsuperuser`


## Contributing

If you want to contribute to this project, follow these steps:

1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a pull request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
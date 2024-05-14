<p align="center">
  <img src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" />
</p>

# This project incorporates a comprehensive testing strategy that leverages both unit tests and integration tests to ensure the quality and reliability of the back-end code.

## Tasks

### [0. Basic Flask app](https://github.com/ehabsmh/alx-backend/blob/main/0x02-i18n/0-app.py)
First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an [`index.html`](https://github.com/ehabsmh/alx-backend/blob/main/0x02-i18n/templates/0-index.html)template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

---

### [1. Basic Babel setup](https://github.com/ehabsmh/alx-backend/blob/main/0x02-i18n/1-app.py)
Install the Babel Flask extension:

`$ pip3 install flask_babel==2.0.0`
Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

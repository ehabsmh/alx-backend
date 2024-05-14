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

---

### [2. Get locale from request](https://github.com/ehabsmh/alx-backend/blob/main/0x02-i18n/2-app.py)
Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

---

### [3. Parametrize templates](https://github.com/ehabsmh/alx-backend/blob/main/0x02-i18n/3-app.py)

Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing

```conf
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

Then initialize your translations with

`$ pybabel extract -F babel.cfg -o messages.pot .`

and your two dictionaries with

```bash
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:


msgid                   English                           French
__________________________________________________________________________________
`home_title`      `"Welcome to Holberton"`	    `"Bienvenue chez Holberton"`
`home_header`         `"Hello world!"`              `"Bonjour monde!"`

Then compile your dictionaries with

`$ pybabel compile -d translations`
Reload the home page of your app and make sure that the correct messages show up.

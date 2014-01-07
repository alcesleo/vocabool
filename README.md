# Vocabool

Pretty much everything is Python3 ready except Compressor

## Supported languages

- Czech
- Danish
- German
- Greek
- English
- Spanish
- Finnish
- French
- Croatian
- Hungarian
- Italian
- Russian
- Swedish

## Credits

During this project I have worked with a bunch of **awesome** framewoks/services that
have seriously impressed me, and make me proud to be a human being.

- Backend is driven by [Django](LINK HERE) and [DRF](LINK HERE)
- Frontend is driven by [Backbone](LINK HERE), [Handlebars](LINK HERE) and of course [jQuery](LINK HERE) and [Underscore](LINK HERE)
- Design is based on [Bootstrap 3](LINK HERE)
- Definitions are from [Wiktionary](LINK HERE) and translations are from [Yandex Translate](LINK HERE)

Minor:

- flags from <http://flag-sprites.com/>
- caching django compressor
- django-registration login outside the SPA

# License

TODO

## PythonAnywhere deployment

### Initial deployment

Initial deploy to PythonAnywhere for future reference.

First, create a Python2.7 web app, then enter a console.

    # create and activate the virtualenv
    source virtuanenvwrapper.sh
    mkvirtualenv vocabool --python=/usr/bin/python2.7 --system-site-packages # system mysql
    workon vocabool

    # download the project
    git clone https://github.com/alcesleo/vocabool.git
    cd vocabool

    # install python dependencies
    pip install -r requirements.txt

Enter `vocabool/settings/environment.py` and insert the appropriate credentials.

    # create/update the database
    python manage.py syncdb

Add static files to Web configuration, like so:

`/static/` -> `/home/alcesleo/vocabool/static/`

    # install css/js dependencies
    npm install bower
    python manage.py bower_install
    python manage.py collectstatic

Paste `wsgi-pythonanywhere.py` to the global wsgi (from web tab), then reload the web app.

### Updating

TODO: fabric

Get access to a terminal.

    cd to/wherever/it/is
    git pull

    # PLEASE don't forget to do this
    source virtualenvwrapper.sh
    workon vocabool

    # install python deps
    pip install -r requirements.txt

    # install static deps
    python manage.py bower_install
    python manage.py collectstatic

Reload the webapp, or

    touch /var/www/web_app_name_wsgi.py'

### Getting to the MySQL database

    ssh -L 3306:mysql.server:3306 username@ssh.pythonanywhere.com
    mysql -h 127.0.0.1 -u username -p

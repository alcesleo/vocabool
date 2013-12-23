
## Deployment steps

Initial deploy to PythonAnywhere for future reference.

First, create a Python3.3 web app, then enter a console.

    # create and activate the virtualenv
    source virtuanenvwrapper.sh
    mkvirtualenv vocabool --no-site-packages --python=/usr/bin/python3.3
    workon vocabool

    # download the project
    git clone https://github.com/alcesleo/vocabool.git
    cd vocabool

    # install python dependencies
    pip install -r requirements.txt

    # create/update the database
    python manage.py syncdb

Add static files to Web configuration, like so:

`/static/` -> `/home/alcesleo/vocabool/static/`

    # install css/js dependencies
    npm install bower
    python manage.py bower_install
    python manage.py collectstatic # optional, for production

Paste `wsgi.py` to the global wsgi (from web tab), then reload the web app.

### TODO

- mysql-python
- wsgi.py production settings
- requirements.production txt


## API:s

- Yandex Translate
- Google Dictionary

### Potential

- Wiktionary
    - Sadly, **extremely** messy output, very difficult to make sense of and
    would take a lot of work to get the short concise definitions I'm looking for
- Wordnik
    - Looks very nice, if I was only interested in English definitions I would
    probably have gone for this one
- Yandex seems to have a decent dictionary API as well.
- http://www.dictionaryapi.com/products/index.htm

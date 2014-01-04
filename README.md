## API

Endpoints:
Variables are listed as examples, it should be obvious which they are.

|                 URL                 |                      Descriptions                     |
| ----------------------------------- | ----------------------------------------------------- |
| /api/vocabulary/                    | List logged in users vocabularies                     |
| /api/vocabulary/terms               | List terms in that vocabulary                         |
| /api/term/3                         | View a specific term                                  |
| /api/term/3/?define                 | Adds a definition to the object before it is returned |
| /api/term/3/?translate_to=de        | Adds a translation to german before returning         |
| /api/term/3/?define&translate_to=ru | The query params can be used together                 |
|                                     |                                                       |


## Standards

I do my best to follow PEP8 and JSHint standards. I like Python's one **module**
per file, so I've carried that over to the JS as well.

## Deployment steps

### Initial deployment

Initial deploy to PythonAnywhere for future reference.

First, create a Python2.7 web app, then enter a console.

    # create and activate the virtualenv
    source virtuanenvwrapper.sh
    mkvirtualenv vocabool --python=/usr/bin/python2.7
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


## Supported languages

    ('cs', gettext_noop('Czech')),
    ('da', gettext_noop('Danish')),
    ('de', gettext_noop('German')),
    ('el', gettext_noop('Greek')),
    ('en', gettext_noop('English')),
    ('es', gettext_noop('Spanish')),
    ('fi', gettext_noop('Finnish')),
    ('fr', gettext_noop('French')),
    ('hr', gettext_noop('Croatian')),
    ('hu', gettext_noop('Hungarian')),
    ('it', gettext_noop('Italian')),
    ('ru', gettext_noop('Russian')),
    ('sv', gettext_noop('Swedish')),

## Technologies

- flags from http://flag-sprites.com/
- caching django compressor, only on debug


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

# License

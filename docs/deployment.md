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

Make sure `vocabool/settings/environment.py` contains your correct credentials.

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

#### Local

If you've made changes to the models, create a migration schema with something like:

    python manage.py schemamigration myapp --auto

and commit it.

Push all your changes.

#### Remote

Get access to a terminal.

    cd to/wherever/it/is
    git pull

    # PLEASE don't forget to do this
    source virtualenvwrapper.sh
    workon vocabool

    # install python deps
    pip install -r requirements.txt

    # update the db
    python manage.py syncdb
    python manage.py migrate

    # install static deps
    python manage.py bower_install
    python manage.py collectstatic

Reload the webapp, or

    touch /var/www/web_app_name_wsgi.py'

### Getting to the MySQL database

    ssh -L 3306:mysql.server:3306 username@ssh.pythonanywhere.com
    mysql -h 127.0.0.1 -u username -p

# Vocabool

- [Link to the live app](http://alcesleo.pythonanywhere.com/)

## Version

Couldn't get the deps to work on Python 3, but I believe all of my code is Python 3 compatible, it's
running on 2.7.5 for now though.

## Structure

Overview of the folder structure.

- `docs/` - documentation
- `templates` - template overrides, other templates are in their apps
- `vocabool` - pretty much the whole application, contains a bunch of apps
    - `accounts/` - login and registration
    - `api/` - the REST interface
    - `client/` - the javascript client app
        - `jstemplates` - the handlebars templates, handled on the client
        - `static` - all js and css
        - `templates` - the few django templates needed to start up the client app
    - `domain` - the domain models
    - `libs` - what couldn't fit anywhere else
    - `settings` - a settings.py module, but as a folder
    - `webservices` - handles communication with external api:s

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

-   Backend is driven by [Django](https://www.djangoproject.com/) and [DRF](http://django-rest-framework.org/)
-   Frontend is driven by [Backbone](http://backbonejs.org/), [Handlebars](http://handlebarsjs.com/)
    and of course [jQuery](http://jquery.com/) and [Underscore](http://underscorejs.org/)
-   Design is based on [Bootstrap 3](http://getbootstrap.com/)
-   Definitions are from [Wiktionary](http://www.wiktionary.org/)
    and translations are from [Yandex Translate](http://translate.yandex.com/)

Minor:

- Flags from <http://flag-sprites.com/>
- Caching using [Django Pipeline](http://django-pipeline.readthedocs.org/)
- Authentication using [Django Registration](https://django-registration.readthedocs.org/en/latest/)
- [MWParserFromHell](http://mwparserfromhell.readthedocs.org/en/latest/) helped with parsing Wiktionary data

## License

**MIT**

## TODO

- **Success messages**
- **Vocabulary restore** - permanent cascading delete is way too easy
- Validate vocabulary names for duplicates and empty
- Sorting
- Page numbering
- Smarter defaults of language select menus
- Change name of vocabulary
- Better caching on client
- Offline cache manifest (https://github.com/nephila/django-html5-appcache)
- Correct spelling mistakes
- Define based on translation
- Custom text input
- Move terms between vocabularies
- Batch delete
- Loading icon
- django-profiles
- fabric deployment automation
- deploy-branch to not have to do a lot of processing on the server
- touch icon for mobile devices
- Get a domain

## Bugs

Needs fixing!

- Adding something to a term breaks the accordion effect
- Adding a duplicate term adds it to the list even if it doesn't register on the backend

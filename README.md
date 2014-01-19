# Vocabool

- [Link to the live app](http://alcesleo.pythonanywhere.com/)
- [Link to a video demo (swedish)](https://www.youtube.com/watch?v=WhHxrrN5yBU&feature=youtu.be)

## Version

Pretty much everything is Python3 ready except Compressor, so it's running on 2.7.5 for now

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
- Caching using [Django Compressor](http://django-compressor.readthedocs.org/en/latest/)
- Authentication using [Django Registration](https://django-registration.readthedocs.org/en/latest/)
- [MWParserFromHell](http://mwparserfromhell.readthedocs.org/en/latest/) helped with parsing Wiktionary data

## License

**MIT**

## TODO

- Change name of vocabulary
- Sorting
- "Added 5 minutes ago"-type timestamps
- Offline cache manifest
- Correct spelling mistakes
- Define based on translation
- Custom text input
- Move terms between vocabularies
- Batch delete
- Loading icon
- django-profiles

## Bugs

Needs fixing!

- Adding something to a term breaks the accordion effect

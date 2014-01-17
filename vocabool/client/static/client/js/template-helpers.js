(function () {
'use strict';

/**
 * Replace all occurences in text
 */
Handlebars.registerHelper('replace', function (text, replace_this, with_this) {
    return new Handlebars.SafeString(text.split(replace_this).join(with_this));
});


/**
 * Iterate over every line in a string
 */
Handlebars.registerHelper('eachLine', function(text, options) {
    var lines = text.trim().split('\n'),
        ret = '';

    for(var i in lines) {
        ret = ret + options.fn({line: lines[i]});
    }
    return ret;
});

// Gives Handlebars access to global variable
Handlebars.registerHelper('global', function (name, options) {
    return options.fn(window[name]);
});

Handlebars.registerHelper('debug', function(optionalValue) {
    console.log('Current Context');
    console.log(this);

    if (optionalValue) {
        console.log('Value');
        console.log(optionalValue);
    }
});

// TODO: This should probably be a partial
/**
 * A flag icon
 */
Handlebars.registerHelper('countryFlag', function (country_code) {
    return new Handlebars.SafeString('<div class="flag flag-' + country_code + '" />');
});


Handlebars.registerPartial('selectLanguage', $('#tpl-partial-selectlanguage').html());

}());

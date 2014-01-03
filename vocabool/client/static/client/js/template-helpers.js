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
    var lines = text.split('\n'),
        ret = '';

    for(var i in lines) {
        ret = ret + options.fn({line: lines[i]});
    }
    return ret;
});

/**
 * Create a select-element from an object
 */
Handlebars.registerHelper('selectFrom', function (hash, name, options) {
    // TODO if hash len
    // TODO selected option
    var ret = '<select name="' + name + '">';
    for (var key in hash) {
        ret += '<option value="' + key + '">' + hash[key] + '</option>';
    }
    ret += '</select>';

    return new Handlebars.SafeString(ret);
});

/**
 * A flag icon
 */
Handlebars.registerHelper('countryFlag', function (country_code) {
    return new Handlebars.SafeString('<div class="flag flag-' + country_code + '" />');
});

'use strict';
window.VB = window.VB || {};

// FIXME: Code duplication from fields.py
VB.language_codes = {
    'cs': 'Czech',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    'it': 'Italian',
    'ru': 'Russian',
    'sv': 'Swedish'
};

VB.vent = _.extend({}, Backbone.Events);

VB.helpers = {};

/**
 * Places text at the start and end of every line in a string,
 * for example, to put <br /> tags at the end of every line do:
 *
 *      surroundLines(textWithMultipleLines, '', '<br />');
 *
 * @param  {string} text
 * @param  {string} start
 * @param  {string} end
 * @return {string}
 */
VB.helpers.surroundLines = function (text, start, end) {
    var lines = text.trim().split('\n');
    return start + lines.join(end + start) + end;
}

Handlebars.registerHelper('bootstrapListLines', function (text) {
    return new Handlebars.SafeString('<ul class="list-group">' +
            VB.helpers.surroundLines(text, '<li class="list-group-item">', '</li>') +
            '</ul>');
});

Handlebars.registerHelper('countryFlag', function (country_code) {
    return new Handlebars.SafeString('<div class="flag flag-' + country_code + '" />');
});

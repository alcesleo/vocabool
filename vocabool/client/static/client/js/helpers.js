(function () {

'use strict';
window.VB = window.VB || {};

// FIXME: Code duplication from fields.py
VB.languages = {
    'cs': 'Czech',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'fi': 'Finnish',
    'fr': 'French',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    'it': 'Italian',
    'ru': 'Russian',
    'sv': 'Swedish'
};

VB.helpers = {};

VB.helpers.enableCsrf = function () {
    // sets up csrf-protection for backbone
    // https://gist.github.com/gcollazo/1240683
    var oldSync = Backbone.sync;
    Backbone.sync = function(method, model, options){
        options.beforeSend = function(xhr){
            xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
        };
        return oldSync(method, model, options);
    };
};


VB.debug = {
    disable: function () {
        // Set console functions to no-op
        var noop = function () {};
        console.error = noop;
        console.log = noop;
        console.warn = noop;
        console.info = noop;
    }
};

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
};

}());

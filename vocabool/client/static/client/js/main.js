'use strict';
// Initialize namespace
window.VB = window.VB || {};
VB.app = VB.app || {}; // holds global intances

$(function () {
    // window.vocabularies = new VB.Collections.VocabularyCollection();
    // window.listView = new VB.Views.VocabularyList({ collection: vocabularies });
    // window.appView = new VB.Views.App({ el: '#view' });

    // function initSpinner(options) {
    //     options = options || {};
    //     $("#loading").spin(options).hide();
    //     $('#loading').ajaxStart(function(){ $(this).fadeIn(); });
    //     $('#loading').ajaxComplete(function(){ $(this).fadeOut(); });
    // }

    // initSpinner();

    // sets up csrf-protection for backbone
    // https://gist.github.com/gcollazo/1240683
    var oldSync = Backbone.sync;
    Backbone.sync = function(method, model, options){
        options.beforeSend = function(xhr){
            xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
        };
        return oldSync(method, model, options);
    };


    // Router

    VB.app.router = new VB.Router();
    Backbone.history.start({pushState: false, root: '/app/'})

});





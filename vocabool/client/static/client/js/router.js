'use strict';
window.VB = window.VB || {};

VB.Router = Backbone.Router.extend({

    initialize: function () {
        this.app = new VB.Views.App({el: '#view'});
    },

    routes: {
        '': 'listVocabularies',
        'vocabularies(/)': 'listVocabularies',
        'vocabulary/:id(/)': 'showVocabulary',
        'login(/)': 'login'
    },

    index: function () {
        // var c = new VB.Collections.Vocabularies();
        // c.fetch({reset: true});
        // var view = new VB.Views.VocabularyList({collection: c});
        // VB.app.view.show(view);
        console.log('index');
    },

    listVocabularies: function () {
        var self = this;
        var vocabularies = new VB.Collections.Vocabularies()

        // Fetch vocabularies and display a list on success
        // TODO: Fail
        vocabularies.fetch().done(function () {
            var view = new VB.Views.VocabularyList({collection: vocabularies});
            self.app.show(view);
        });
    },

    showVocabulary: function (id) {
        id = parseInt(id, 10);
        // TODO: use vocabulary model from already downloaded collection?

        var self = this,
            // The vocabulary model does not actually need to be fetched, if it
            // has the right id it will use the correct URL to fetch its terms
            vocabulary = new VB.Models.Vocabulary({id: id});

        vocabulary.terms.fetch().done(function () {
            var view = new VB.Views.TermList({collection: vocabulary.terms});
            self.app.show(view);
        });
    },

    login: function () {
        // TODO: check if logged in and show different pages?
        var view = new VB.Views.Login();
        this.app.show(view);
    }
});

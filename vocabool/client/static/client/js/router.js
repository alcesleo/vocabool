'use strict';
window.VB = window.VB || {};

VB.Router = Backbone.Router.extend({

    initialize: function () {
        this.appView = new VB.Views.RegionManager({el: '#view'});
    },

    routes: {
        '': 'listVocabularies',
        'vocabularies(/)': 'listVocabularies',
        'vocabulary/:id(/)': 'showVocabulary',
        'login(/)': 'login'
    },

    listVocabularies: function () {
        var self = this;
        var vocabularies = new VB.Collections.Vocabularies()

        // Fetch vocabularies and display a list on success
        // TODO: Fail
        vocabularies.fetch().done(function () {
            var view = new VB.Views.VocabularyList({collection: vocabularies});
            self.appView.show(view);
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
            self.appView.show(view);
        });
    },

    login: function () {
        // TODO: check if logged in and show different pages?
        var view = new VB.Views.Login();
        this.appView.show(view);
    }
});

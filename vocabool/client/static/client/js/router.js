(function () {
'use strict';
window.VB = window.VB || {};


VB.Router = Backbone.Router.extend({

    initialize: function (options) {
        this.region = new VB.Views.RegionManager({el: '#view'});
    },

    routes: {
        '': 'vocabularies',
        'vocabularies(/)': 'vocabularies',
        'vocabulary/:id(/)': 'terms',
    },

    vocabularies: function () {
        var self = this;
        var vocabularies = new VB.Collections.Vocabularies();

        // Fetch vocabularies and display a list on success
        // TODO: Fail
        vocabularies.fetch().done(function () {
            var view = new VB.Views.VocabulariesPage({vocabularies: vocabularies});
            self.region.show(view);
        });
    },

    terms: function (id) {
        id = parseInt(id, 10);
        // TODO: use vocabulary model from already downloaded collection?

        var self = this,
            // The vocabulary model does not actually need to be fetched, if it
            // has the right id it will use the correct URL to fetch its terms
            vocabulary = new VB.Models.Vocabulary({id: id});

        // FIXME: this is really ugly
        // Fetch both the vocabulary and its terms
        vocabulary.fetch().done(function () {
            // fetch and show terms
            vocabulary.terms.fetch().done(function () {
                var view = new VB.Views.TermsPage({vocabulary: vocabulary});
                self.region.show(view);
            });
        });

    },
});


}());

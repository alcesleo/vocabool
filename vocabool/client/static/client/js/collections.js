'use strict';
window.VB = window.VB || {};
VB.Collections = VB.Collections || {};

/**
 * Baseclass that handles paginated result-sets from Django Rest Framework
 */
VB.Collections.DRFCollection = Backbone.PageableCollection.extend({
    parseRecords: function (resp) {
        return resp.results;
    }
});

VB.Collections.Terms = VB.Collections.DRFCollection.extend({
    model: VB.Models.Term,
    initialize: function (models, options) {
        this.vocabulary = options.vocabulary;
    },
    url: function () {
        // TODO: Slug
        return this.vocabulary.url() + '/terms';
    }
});


VB.Collections.Vocabularies = VB.Collections.DRFCollection.extend({
    model: VB.Models.Vocabulary,
    url: '/api/vocabulary',
});

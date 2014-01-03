'use strict';
window.VB = window.VB || {};
VB.Collections = VB.Collections || {};

/**
 * Baseclass that handles paginated result-sets from Django Rest Framework
 */
VB.Collections.DRFCollection = Backbone.PageableCollection.extend({
    mode: 'server',

    queryParams: {
        currentPage: 'page'
    },

    parseRecords: function (resp) {
        return resp.results;
    },
    parseState: function (resp, queryParams, state, options) {
        return { totalRecords: resp.count };
    }
});

// new Terms({vocabulary: v});
VB.Collections.Terms = VB.Collections.DRFCollection.extend({
    model: VB.Models.Term,
    initialize: function (models, options) {
        // TODO: throw on no vocabulary
        this.vocabulary = options.vocabulary;
    },
    url: function () {
        return this.vocabulary.url() + '/terms';
    }
});


VB.Collections.Vocabularies = VB.Collections.DRFCollection.extend({
    model: VB.Models.Vocabulary,
    url: '/api/vocabulary',
});

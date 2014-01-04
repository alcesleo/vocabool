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


// new Terms([], {vocabulary: v});
VB.Collections.Terms = VB.Collections.DRFCollection.extend({
    model: VB.Models.Term,
    initialize: function (models, options) {
        // Must get a vocabulary
        if (!(options.vocabulary instanceof VB.Models.Vocabulary)) {
            throw new Error('Terms must be associated with a Vocabulary.')
        }
        this.vocabulary = options.vocabulary;
    },
    url: function () {
        return this.vocabulary.url() + '/terms/';
    }
});


VB.Collections.Vocabularies = VB.Collections.DRFCollection.extend({
    model: VB.Models.Vocabulary,
    url: '/api/vocabulary',
});

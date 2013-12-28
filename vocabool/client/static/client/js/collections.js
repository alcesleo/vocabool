'use strict';
window.VB = window.VB || {};
VB.Collections = VB.Collections || {};

VB.Collections.Terms = Backbone.Collection.extend({
    model: VB.Models.Term,
    initialize: function (models, options) {
        this.vocabulary = options.vocabulary;
    },
    url: function () {
        // TODO: Slug
        return this.vocabulary.url() + '/terms';
    }
});


VB.Collections.Vocabularies = Backbone.Collection.extend({
    model: VB.Models.Vocabulary,
    url: '/api/vocabulary',
});

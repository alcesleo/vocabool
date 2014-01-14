(function () {

'use strict';
window.VB = window.VB || {};
VB.Collections = VB.Collections || {};


// new Terms([], {vocabulary: v});
VB.Collections.Terms = VB.Bases.DRFCollection.extend({
    model: VB.Models.Term,
    initialize: function (models, options) {
        // Must get a vocabulary
        if (!(options.vocabulary instanceof VB.Models.Vocabulary)) {
            throw new Error('Terms must be associated with a Vocabulary.')
        }
        this.vocabulary = options.vocabulary;
    },
    url: function () {
        return this.vocabulary.url() + '/term/';
    }

});


VB.Collections.Vocabularies = VB.Bases.DRFCollection.extend({
    model: VB.Models.Vocabulary,
    url: '/api/vocabulary/',
});

}());

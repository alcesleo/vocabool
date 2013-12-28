'use strict';
window.VB = window.VB || {};
VB.Models = VB.Models || {};

VB.Models.Term = Backbone.Model.extend({});

VB.Models.Vocabulary = Backbone.Model.extend({
    initialize: function () {
        // create empty term collection with reference to this vocabulary
        this.terms = new VB.Collections.Terms([], { vocabulary: this });
    },
    addTerm: function (props) {
        // TODO
    },
    fetchTerms: function () {
        return this.terms.fetch();
    }
    // TODO: override url with slug?
});

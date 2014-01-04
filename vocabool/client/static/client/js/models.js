'use strict';
window.VB = window.VB || {};
VB.Models = VB.Models || {};

VB.Models.Term = Backbone.Model.extend({

    url: function () {
        return '/api/term/' + this.get('id');
    },

    translateAndDefine: function (language) {

        var params = {define: '', translate_to: language},
            self = this;

        this.fetch({ data: $.param(params) }).done(function () {
            // TODO: Complete events, remove deepmodel
            self.trigger('change');
        });
        return this;

    }
});

VB.Models.Vocabulary = Backbone.Model.extend({
    initialize: function () {
        // create empty term collection with reference to this vocabulary
        this.terms = new VB.Collections.Terms([], { vocabulary: this });
    },
    url: function () {
        return '/api/vocabulary/' + this.get('id');
    }
});


VB.Models.Status = Backbone.Model.extend({
    defaults: {
        user: null,
        vocabulary: null,
    }
});

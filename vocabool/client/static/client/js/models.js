'use strict';
window.VB = window.VB || {};
VB.Models = VB.Models || {};

VB.Models.Term = Backbone.Model.extend({

    // url: function () {
    //     return '/api/term/' + this.get('id');
    // },

    // urlRoot: '/api/term/', // should work only when not in a collection
    defaults: {
        text: ''
    },

    validate: function (attributes, options) {
        if (attributes.text.trim().length === 0) {
            return 'Text can not be empty!';
        }
    },

    translateAndDefine: function (language) {

        var params = {define: '', translate_to: language},
            self = this;

        this.fetch({ data: params }).done(function () {
            // TODO: Complete events
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
    urlRoot: '/api/vocabulary/'
});


VB.Models.Status = Backbone.Model.extend({
    defaults: {
        user: null,
        vocabulary: null,
    }
});

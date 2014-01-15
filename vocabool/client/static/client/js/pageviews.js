(function () {
'use strict';

// var FlowView = Backbone.View.extend({

//     viewClasses: [],
//     subviews: [],
//     createViews: function (options) {
//         for (var i = 0, len = viewClasses.length; i < len; i++) {
//             this.subviews[i] = new viewClasses[i](options);
//         }
//     }

// });

// PAGES

VB.Views.TermsPage = Backbone.View.extend({
    id: 'terms-page',

    initialize: function (options) {
        this.addView = new VB.Views.AddTerm({collection: options.vocabulary.terms});
        this.listView = new VB.Views.TermList({collection: options.vocabulary.terms});
        this.paginationView = new VB.Views.PaginationLinks({collection: options.vocabulary.terms});
    },

    render: function () {
        // TODO: cleaner
        this.$el.empty();
        this.$el.append(this.addView.render().el);
        this.$el.append(this.listView.render().el);
        this.$el.append(this.paginationView.render().el);
        return this;
    }

});

VB.Views.VocabulariesPage = Backbone.View.extend({

    initialize: function (options) {
        this.addView = new VB.Views.AddVocabulary({collection: options.vocabularies});
        this.listView = new VB.Views.VocabularyList({collection: options.vocabularies});
    },

    render: function () {
        this.$el.empty();
        this.$el.append(this.addView.render().el);
        this.$el.append(this.listView.render().el);
        return this;
    }
});

}());

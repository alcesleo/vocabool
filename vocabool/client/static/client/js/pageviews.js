(function () {
'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};


var View = VB.Views.View;


VB.Views.TermsPage = View.extend({
    id: 'terms-page',

    templateId: 'heading',

    initialize: function (options) {
        this.vocabulary = options.vocabulary;
        this.addView = new VB.Views.AddTerm({collection: options.vocabulary.terms});
        this.listView = new VB.Views.TermList({collection: options.vocabulary.terms});
        this.paginationView = new VB.Views.PaginationLinks({collection: options.vocabulary.terms});
    },

    render: function () {
        // TODO: cleaner
        this.$el.empty();
        this.$el.append(this.template(this.vocabulary.toJSON()));
        this.$el.append(this.addView.render().el);
        this.$el.append(this.listView.render().el);
        this.$el.append(this.paginationView.render().el);
        return this;
    }

});


VB.Views.VocabulariesPage = View.extend({

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

'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};


// http://mikefowler.me/2013/11/18/page-transitions-in-backbone/
// new RegionManager({el: '#my-region'});
VB.Views.RegionManager = Backbone.View.extend({

    show: function (view) {

        if (this.currentView) {
            this.currentView.remove();
        }

        this.currentView = view;
        this.currentView.render();

        this.$el.html(this.currentView.el);
    }

});


// REPRESENTATION


VB.Views.Vocabulary = Backbone.View.extend({
    tagName: 'li',
    className: 'vocabulary',
    template: Handlebars.compile($('#tpl-vocabulary').html()),

    // TODO: don't hardcode the links

    render: function () {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});


VB.Views.Term = Backbone.View.extend({
    className: 'term panel panel-default',

    initialize: function () {
        this.listenTo(this.model, 'change', this.render);
        this.listenTo(this.model, 'error', this.error);
    },

    template: Handlebars.compile($('#tpl-term').html()),

    events: {
        'click .default-term-action': 'termAction'
    },

    error: function (obj, xhr, options) {
        alert(xhr.responseJSON.detail);
    },

    render: function () {
        // FIXME: ugly hack to get language context
        var context = _.extend(this.model.toJSON(), { languages: VB.languages });
        this.$el.html(this.template(context));
        return this;
    }
});

// PAGES

VB.Views.TermsPage = Backbone.View.extend({
    className: 'row',
    id: 'terms-page',

    initialize: function (options) {
        this.addView = new VB.Views.AddTerm({collection: options.vocabulary.terms});
        this.listView = new VB.Views.TermList({collection: options.vocabulary.terms});
    },

    render: function () {
        // TODO: cleaner
        this.$el.empty();
        this.$el.append(this.addView.render().el);
        this.$el.append(this.listView.render().el);
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

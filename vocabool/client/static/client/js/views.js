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

    termAction: function () {
        this.model.translateAndDefine('sv'); // TODO: Dynamic
    },

    error: function (obj, xhr, options) {
        alert(xhr.responseJSON.detail);
    },

    render: function () {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});

// FORMS

VB.Views.AddTerm = Backbone.View.extend({

    className: 'row add-term',

    // TODO: Handle 'invalid' event

    // TODO: override template, extensions.js?
    template: Handlebars.compile($('#tpl-addterm').html()),

    events: {
        'click #add-term-btn': 'addTerm'
    },

    addTerm: function () {
        // get attributes
        var text = this.$('#add-term-text').val();

        // add to collection
        this.collection.create({
            text: text,
            language: 'en' // TODO: lang
        });
        // TODO: scroll to added term, make sure it's open
    },

    render: function () {
        this.$el.html(this.template({languages: VB.languages}));
        return this;
    }
});

VB.Views.AddVocabulary = Backbone.View.extend({
    className: 'col-md-12 add-vocabulary',

    template: Handlebars.compile($('#tpl-addvocabulary').html()),
    events: {
        'click #add-vocabulary-btn': 'addVocabulary'
    },
    render: function () {
        this.$el.html(this.template());
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

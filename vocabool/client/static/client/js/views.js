'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};

// Misc

// http://mikefowler.me/2013/11/18/page-transitions-in-backbone/
VB.Views.App = Backbone.View.extend({

    show: function (view) {

        if (this.currentPage) {
            this.currentPage.remove();
        }

        this.currentPage = view;
        this.currentPage.render();

        this.$el.html(this.currentPage.el);
    }

});

// Vocabularies

VB.Views.Vocabulary = Backbone.View.extend({
    tagName: 'li',
    className: 'vocabulary',
    template: Handlebars.compile($('#tpl-vocabulary').html()),

    render: function () {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});

VB.Views.VocabularyList = Backbone.View.extend({

    // TODO: remove views on destroy
    tagName: 'ul',
    className: 'vocabularies',

    render: function () {
        var self = this;
        // FIXME: reset safely
        this.$el.empty();
        this.collection.each(function (vocabulary) {
            var view = new VB.Views.Vocabulary({model: vocabulary});
            self.$el.append(view.render().el);
        });
        return this;
    }
});

// Terms

VB.Views.Term = Backbone.View.extend({

    template: Handlebars.compile($('#tpl-term').html()),

    render: function () {
        // TODO: zombie events when re-rendering?
        // FIXME: nicer... this sets the element directly without wrapping a div for bootstraps accordion
        this.el = this.template(this.model.toJSON());
        this.delegateEvents()
        return this;
    }
});

VB.Views.TermList = Backbone.View.extend({

    // FIXME: Define these in template
    className: 'panel-group',
    id: 'term-list',

    render: function () {
        var self = this;

        this.$el.empty(); // FIXME: Reset safely
        this.collection.each(function (term) {
            var view = new VB.Views.Term({model: term});
            self.$el.append(view.render().el);
        });
        return this;
    }
});

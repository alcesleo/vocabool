'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};

// Misc
// VB.Views.DRFPageableCollection

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

    // TODO: don't hardcode the links

    render: function () {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});

VB.Views.VocabularyList = Backbone.View.extend({

    initialize: function () {
        // TODO: this.listenTo(this.collection, 'add', this.appendOne)
    },
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

    // TODO: put this in template
    className: 'panel panel-default',

    initialize: function () {
        this.listenTo(this.model, 'change', this.render);
    },

    template: Handlebars.compile($('#tpl-term').html()),

    events: {
        'click .default-term-action': 'termAction'
    },

    termAction: function () {
        this.model.translateAndDefine('sv'); // TODO: Dynamic
    },

    render: function () {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});

VB.Views.TermList = Backbone.View.extend({

    // FIXME: Define these in template
    className: 'panel-group',
    id: 'term-list',


    render: function () {

        console.log('TermList:render');

        var self = this;

        this.$el.empty(); // FIXME: Reset safely
        this.collection.each(function (term) {
            var view = new VB.Views.Term({model: term});
            self.$el.append(view.render().el);
        });
        return this;
    }
});

VB.Views.CreateTerm = Backbone.View.extend({

})

// Users

VB.Views.Login = Backbone.View.extend({
    template: Handlebars.compile($('#tpl-login').html()),

    events: {
        'click .login': 'login'
    },

    login: function () {

    },

    render: function () {
        // TODO: zombie events
        this.$el.html(this.template());
        return this;
    }
});

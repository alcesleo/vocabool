'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};

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
    ItemView: VB.Views.Vocabulary,

    render: function () {
        var self = this;
        // FIXME: reset safely
        this.$el.empty();
        this.collection.each(function (vocabulary) {
            var view = new self.ItemView({model: vocabulary});
            self.$el.append(view.render().el);
        });
        return this;
    }
});

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

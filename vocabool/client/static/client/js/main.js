// Initialize namespace
var App = App || {};
App.Models = App.Models || {};
App.Views = App.Views || {};
App.Collections = App.Collections || {};


App.Models.Vocabulary = Backbone.Model.extend({

});

App.Views.Vocabulary = Backbone.View.extend({

    template: Handlebars.compile($('#tpl-index').html()),

    initialize: function () {
        this.listenTo(model, 'change', this.render);
    },

    render: function () {
        this.$el.html(this.template(this.model.attributes));
        return this;
    }

});

// http://mikefowler.me/2013/11/18/page-transitions-in-backbone/
App.Views.App = Backbone.View.extend({

    show: function (view) {
        var previous = this.currentPage || null;
        var next = view;

        if (previous) {
            previous.remove();
        }

        next.render();
        this.$el.html(next.el);
        this.currentPage = next;
    }

});


$(function () {
    model = new App.Models.Vocabulary({ test: 'hello'})
    testview = new App.Views.Vocabulary({ model: model });
    appView = new App.Views.App({ el: $('#view') });
    appView.render();
    appView.show(testview);
});



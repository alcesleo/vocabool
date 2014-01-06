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

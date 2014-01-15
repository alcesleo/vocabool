(function () {

'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};

var View = VB.Bases.View;


// http://mikefowler.me/2013/11/18/page-transitions-in-backbone/
// new RegionManager({el: '#my-region'});
VB.Views.RegionManager = View.extend({

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


VB.Views.Vocabulary = View.extend({
    tagName: 'li',
    className: 'vocabulary',
    templateId: 'vocabulary',

    // TODO: don't hardcode the links

    render: function () {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});


VB.Views.Term = View.extend({
    className: 'term panel panel-default',
    templateId: 'term',

    initialize: function () {
        this.listenTo(this.model, 'change', this.render);
        this.listenTo(this.model, 'error', this.error);
    },


    events: {
        'click .btn-define': 'define',
        'click .btn-translate': 'translate',
    },

    error: function (obj, xhr, options) {
        alert(xhr.responseJSON.detail);
    },

    define: function () {
        var btn = this.$('.btn-define').button('loading');
        this.model.define();
    },

    translate: function () {
        // TODO: Refactor loading buttons
        var btn = this.$('.btn-translate').button('loading');
        var lang = this.$('.language-selector :selected').val();
        this.model.translate(lang);
    },

    render: function () {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});

}());

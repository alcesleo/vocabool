(function () {
'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};


var View = VB.Views.View;


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


VB.Views.Vocabulary = View.extend({
    className: 'vocabulary panel panel-default',
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
        this.listenTo(this.model, 'change', function () {this.render(true)});
        this.listenTo(this.model, 'error', this.error);
        this.listenTo(this.model, 'destroy', this.remove); // TODO: handle in collection as well
    },


    events: {
        'click .btn-define': 'define',
        'click .btn-translate': 'translate',
        'click .btn-trash': 'trash',
        'click .btn-clear': 'empty',
    },

    error: function (obj, xhr, options) {
        alert(xhr.responseJSON.detail);
    },

    define: function () {
        // TODO: DRY
        var btn = this.$('.btn-define');
        btn.button('loading');
        this.model.define().always(function () {
            btn.button('reset');
        });
    },

    translate: function () {
        // TODO: Refactor loading buttons
        var btn = this.$('.btn-translate'),
            lang = this.$('.language-selector :selected').val();

        btn.button('loading');
        this.model.translate(lang).always(function () {
            btn.button('reset');
        });
    },

    // worth noting is that both 'delete' and 'remove' are already taken
    trash: function () {
        if (confirm('Are you sure you want to delete this term?')) {
            this.model.destroy();
        }
    },

    // 'clear' is also taken
    empty: function () {
        if (confirm('Remove all translations and definitions?')) {
            this.model.empty();
        }
    },

    render: function (collapse) {
        this.$el.html(this.template(this.model.toJSON()));
        if (collapse) {
            // FIXME: make it stay down
            this.$('.collapse').collapse('show');
        }
        return this;
    }
});


}());

(function () {
'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};

var ListView = VB.Bases.ListView,
    View = VB.Bases.View;

VB.Views.VocabularyList = ListView.extend({

    className: 'panel-group',
    id: 'vocabulary-list',
    itemView: VB.Views.Vocabulary,

    initialize: function () {
        this.listenTo(this.collection, 'sync', this.render);
    },

});


VB.Views.TermList = ListView.extend({
    className: 'panel-group',
    id: 'term-list',
    itemView: VB.Views.Term,

    initialize: function () {
        this.listenTo(this.collection, 'add', this.addOne);
    },

});

VB.Views.PaginationLinks = View.extend({

    templateId: 'paginationlinks',

    getOptions: function () {
        return {
            nextDisabled: !this.collection.hasNext(),
            previousDisabled: !this.collection.hasPrevious(),
        }
    },

    events: {
        'click .previous': 'previous',
        'click .next a': 'next',
    },

    next: function (e) {
        if (this.collection.hasNext()) {
            this.collection.getNextPage();
        }
        return false;
    },

    previous: function (e) {
        if (this.collection.hasPrevious()) {
            this.collection.getPreviousPage();
        }
        return false;
    },

    render: function () {
        this.$el.html(this.template(this.getOptions()));
        return this;
    }

});

}());

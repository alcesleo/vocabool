(function () {
'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};


// Dependencies
var ListView = VB.Views.ListView,
    View = VB.Views.View,
    TermView = VB.Views.Term,
    VocabularyView = VB.Views.Vocabulary;


VB.Views.VocabularyList = ListView.extend({

    className: 'panel-group',
    id: 'vocabulary-list',
    itemView: VocabularyView,

    initialize: function () {
        this.listenTo(this.collection, 'sync', this.render);
    }

});


VB.Views.TermList = ListView.extend({

    className: 'panel-group',
    id: 'term-list',
    itemView: TermView,

    // TODO: Open terms when added, maybe add them to the top of the list

    initialize: function () {
        this.listenTo(this.collection, 'sync', this.render); // re-render when new page etc
        this.listenTo(this.collection, 'add', this.addOne); // a new term has been added
    },

});


VB.Views.PaginationLinks = View.extend({

    templateId: 'paginationlinks',

    initialize: function () {
        this.listenTo(this.collection, 'sync', this.render);
        this.listenTo(this.collection, 'all', function () {console.log(arguments)});
    },

    // Disable buttons if necessary
    getOptions: function () {
        return {
            nextDisabled: !this.collection.hasNext(),
            previousDisabled: !this.collection.hasPrevious(),
        };
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

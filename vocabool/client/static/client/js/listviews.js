(function () {

'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};

VB.Views.VocabularyList = VB.Bases.ListView.extend({

    tagName: 'ul',
    className: 'vocabularies',
    itemView: VB.Views.Vocabulary,

    initialize: function () {
        this.listenTo(this.collection, 'add', this.addOne);
    },

});


VB.Views.TermList = VB.Bases.ListView.extend({
    className: 'panel-group',
    id: 'term-list',
    itemView: VB.Views.Term,

    initialize: function () {
        this.listenTo(this.collection, 'add', this.addOne);
    },

});

}());

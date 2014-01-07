
VB.Views.VocabularyList = Backbone.ListView.extend({

    tagName: 'ul',
    className: 'vocabularies',
    itemView: VB.Views.Vocabulary

});


VB.Views.TermList = Backbone.ListView.extend({
    className: 'panel-group',
    id: 'term-list',
    itemView: VB.Views.Term,

    initialize: function () {
        this.listenTo(this.collection, 'add', this.addOne);
    },

});

// Super

VB.Views.ListView = Backbone.View.extend({

    itemView: null,
    subviews: [],

    // TODO: use constructor to allow childclasses to use initialize?
    initialize: function () {
        // This gets me every time. Needed when a method calls another method that uses 'this'.
        _.bindAll(this, 'renderItem');
    },

    // override remove to take care of subviews
    remove: function () {
        this.removeSubviews();
        Backbone.View.prototype.remove.apply(this, arguments);
    },

    removeSubviews: function () {
        console.log(this)
        // remove all subviews
        this.subviews.forEach(function (view) {
            view.remove();
        });
        // empty subiews
        this.subviews.length = 0;
    },

    renderItem: function (model) {
        var view = new this.itemView({model: model});
        this.subviews.push(view);
        this.$el.append(view.render().el);
    },

    render: function () {
        this.removeSubviews();
        this.collection.each(this.renderItem);
        return this;
    }
});


VB.Views.VocabularyList = VB.Views.ListView.extend({

    tagName: 'ul',
    className: 'vocabularies',
    itemView: VB.Views.Vocabulary

});


VB.Views.TermList = VB.Views.ListView.extend({

    className: 'panel-group',
    id: 'term-list',
    itemView: VB.Views.Term

});

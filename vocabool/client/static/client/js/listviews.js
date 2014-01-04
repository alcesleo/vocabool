// Super

/**
 * // All that's needed!
 * var MyListView = VB.Views.ListView.extend({
 *     itemView: MyBackboneView
 * })
 */
VB.Views.ListView = Backbone.View.extend({

    itemView: null,
    subviews: [],

    // overriding constructor to allow childs to have an initialize-method without
    // needing to, and probably forgetting to call super.
    constructor: function () {
        // This gets me every time. Needed when a method calls another method that uses 'this'.
        _.bindAll(this, 'renderItem');
        Backbone.View.apply(this, arguments); // super
    },

    // override remove to take care of subviews
    remove: function () {
        this.removeSubviews();
        Backbone.View.prototype.remove.apply(this, arguments);
    },

    removeSubviews: function () {
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

    // TODO: listento add
    initialize: function () {
        console.log('I work now!')
    },

    className: 'panel-group',
    id: 'term-list',
    itemView: VB.Views.Term,
    template: Handlebars.compile($('#tpl-termlist').html()),

    events: {
        'click #add-term-btn': 'addTerm'
    },

    addTerm: function () {
        console.log(this.$('#add-term-text').val());
        // get attributes
        // add to collection
        // sync
        // scroll to added term
    },

    // override to prepend template
    render: function () {
        this.$el.html(this.template());
        this.constructor.__super__.render.apply(this);
    }

});

'use strict';
window.VB = window.VB || {};
VB.Bases = VB.Bases || {};

/**
 * // All that's needed!
 * var MyListView = VB.Bases.ListView.extend({
 *     itemView: MyBackboneView
 * })
 */
VB.Bases.ListView = Backbone.View.extend({

    itemView: null,
    subviews: [],

    // overriding constructor to allow childs to have an initialize-method without
    // needing to, and probably forgetting to call super.
    constructor: function () {
        // This gets me every time. Needed when a method calls another method that uses 'this'.
        _.bindAll(this, 'addOne');
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

    addOne: function (model) {
        var view = new this.itemView({model: model});
        this.subviews.push(view);
        this.$el.append(view.render().el);
    },

    render: function () {
        this.removeSubviews();
        this.collection.each(this.addOne);
        return this;
    }
});

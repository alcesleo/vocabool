(function () {

'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};


/**
 * More convenient handlebars templates
 */
VB.Views.View = Backbone.View.extend({

    // TODO: name as class templates
    // Set this to the name of the template instead of compiling yourself
    templateId: '',

    constructor: function () {
        this.setTemplate(this.templateId);
        Backbone.View.apply(this, arguments); // super
    },

    setTemplate: function (templateId) {
        // non-empty string
        if (_.isString(this.templateId) && this.templateId) {
            this.template = Handlebars.compile($('#tpl-' + this.templateId).html());
        }
    },

});

/**
 * Makes it easier to have subviews
 */
VB.Views.ParentView = VB.Views.View.extend({

    // it is important to use this array to store subviews for
    // the rest to work
    subviews: [],

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

});

/**
 * // All that's needed!
 * var MyListView = VB.Views.ListView.extend({
 *     itemView: MyBackboneView
 * })
 */
VB.Views.ListView = VB.Views.ParentView.extend({

    itemView: null,

    // overriding constructor to allow childs to have an initialize-method without
    // needing to, and probably forgetting to call super.
    constructor: function () {
        // This gets me every time. Needed when a method calls another method that uses 'this'.
        _.bindAll(this, 'addOne');
        Backbone.View.apply(this, arguments); // super
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


}());

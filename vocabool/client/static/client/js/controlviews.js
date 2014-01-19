(function () {
'use strict';
window.VB = window.VB || {};
VB.Views = VB.Views || {};

var View = VB.Views.View;

VB.Views.AddTerm = View.extend({

    initialize: function () {
        this.listenTo(this.collection, 'invalid', this.validationError);
        this.listenTo(this.collection, 'error', this.serverError);
        this.listenTo(this.collection, 'all', function () {console.log(arguments)});
    },

    className: 'add-term',

    templateId: 'termcontrols',

    events: {
        'click #btn-extend-vocabulary': 'addTerm',
        'click .btn-sort': 'sort'
    },

    // renders errormessage
    showError: function (message) {
        alert(message);
    },

    // local error
    validationError: function (model, errors) {
        this.showError(errors.join('\n'));
    },

    // remote error
    serverError: function (model, xhr, options) {
        // FIXME: Should be done in a nicer way
        this.showError(xhr.responseJSON.detail);
    },

    // TODO: Implement sorting
    sort: function (event) {
        // Get data attr
        var $target = $(event.target);
        var sortBy = $target.data('sort') || $target.parent().data('sort'); // if you click the glyph

        switch (sortBy) {
            case 'a-z':
                console.log('a-z')
                break;
            case 'z-a':
                console.log('z-a')
                break;
            case 'new-old':
                console.log('new-old')
                break;
            case 'old-new':
                console.log('old-new')
                break;
            default:
                console.log('none');
        }
    },

    addTerm: function () {
        // get attributes
        var attrs = {
            text: this.$('#term-text').val(),
            language: this.$('.language-selector :selected').val()
        };

        // add to collection
        console.log(['Create term', attrs]);
        this.collection.create(attrs, {validate: true});

        // TODO: scroll to added term, make sure it's open
        // TODO: Successmessage!!!
    },

    render: function () {
        this.$el.html(this.template({languages: VB.languages}));
        return this;
    }
});


VB.Views.AddVocabulary = View.extend({
    className: 'add-vocabulary',

    template: Handlebars.compile($('#tpl-addvocabulary').html()),
    events: {
        'click #add-vocabulary-btn': 'addVocabulary'
    },

    addVocabulary: function () {
        var attrs = {
            name: this.$('#add-vocabulary-name').val()
        }
        // Wait for the server to respond,
        // the link will not work until the model gets a PK.
        this.collection.create(attrs);
    },

    render: function () {
        this.$el.html(this.template());
        return this;
    }
});

}());

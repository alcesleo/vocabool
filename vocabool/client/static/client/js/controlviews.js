(function () {

'use strict';

VB.Views.AddTerm = VB.Bases.View.extend({

    initialize: function () {
        this.listenTo(this.collection, 'invalid', this.showErrors);
    },

    className: 'add-term',

    // TODO: Handle 'invalid' event

    templateId: 'termcontrols',

    events: {
        'click #btn-extend-vocabulary': 'addTerm',
        'click .btn-sort': 'sort'
    },

    showErrors: function (model, errors) {
        alert(errors.join('\n'));
    },

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
    },

    render: function () {
        this.$el.html(this.template({languages: VB.languages}));
        return this;
    }
});


VB.Views.AddVocabulary = Backbone.View.extend({
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
        this.collection.create(attrs, {wait: true});
    },

    render: function () {
        this.$el.html(this.template());
        return this;
    }
});

}());

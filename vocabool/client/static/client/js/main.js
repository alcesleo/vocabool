// Initialize namespace
var VOCABOOL = VOCABOOL || {};
VOCABOOL.Models = VOCABOOL.Models || {};
VOCABOOL.Views = VOCABOOL.Views || {};
VOCABOOL.Collections = VOCABOOL.Collections || {};

VOCABOOL.Views.Vocabulary = Backbone.View.extend({

    initialize: function () {
        console.log('VocabularyView');
    },

    template: Handlebars.compile($('#tpl-index').html()),

    render: function () {
        this.$el.html(this.template({ test: 'hello '}));
        return this.el;
    }

});

$(function () {
    var listeme = new VOCABOOL.Views.Vocabulary();
});



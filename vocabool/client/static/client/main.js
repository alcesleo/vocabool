// Initialize namespace
var VOCABOOL = VOCABOOL || {};
VOCABOOL.Models = VOCABOOL.Models || {};
VOCABOOL.Views = VOCABOOL.Views || {};
VOCABOOL.Collections = VOCABOOL.Collections || {};

VOCABOOL.Models.Listeme = Backbone.Model.extend({
    initialize: function () {
        console.log('Listeme');
    },

});

$(function () {
    var listeme = new VOCABOOL.Models.Listeme();
});



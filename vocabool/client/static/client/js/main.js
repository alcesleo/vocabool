// 'use strict';
// Initialize namespace
window.VB = window.VB || {};
VB.Models = VB.Models || {};
VB.Views = VB.Views || {};
VB.Collections = VB.Collections || {};

// TODO: p_tagify linebreaks in definitions


$(function () {
    // window.vocabularies = new VB.Collections.VocabularyCollection();
    // window.listView = new VB.Views.VocabularyList({ collection: vocabularies });
    // window.appView = new VB.Views.App({ el: '#view' });

    // VB.app = {};
    // VB.app.view = new VB.Views.App();

    // VB.app.router = new VB.Router();
    // // Backbone.history.start();
    //
    //
    // TESTING CODE
    vs = new VB.Collections.Vocabularies()
    vs.fetch({success: function () {
        v = vs.at(0)
        vv = new VB.Views.Vocabulary({model: v})
        vv.render()

        // coll
        vl = new VB.Views.VocabularyList({collection: vs});

        app = new VB.Views.App({el: '#view'});
        app.show(vl);
    }})

    Backbone.history.start({pushState: true, root: '/app/'})

});





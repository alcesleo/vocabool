$(function () {
    'use strict';
    window.VB = window.VB || {};
    VB.app = VB.app || {}; // holds global intances

    VB.helpers.enableCsrf();
    VB.app.router = new VB.Router();
    Backbone.history.start({pushState: false, root: '/app/'})
});

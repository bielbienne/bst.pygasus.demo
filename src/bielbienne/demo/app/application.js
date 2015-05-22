Ext.define('bielbienne.demo.Application', {
    extend: 'Ext.app.Application',
    requires: [
    	'scaffolding.bufferedstore.Card'
    ],

    name: 'DEMO',

    views: [
        'bielbienne.demo.view.MainView'
    ],
    
    controllers: [
    	'bielbienne.demo.controller.Main'
    ],
    
    launch: function() {
        Ext.create('bielbienne.demo.view.MainView');
    }
});
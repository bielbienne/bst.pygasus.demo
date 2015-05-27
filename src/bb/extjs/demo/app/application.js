Ext.define('bb.extjs.demo.Application', {
    extend: 'Ext.app.Application',
    requires: [
    	'scaffolding.bufferedstore.Card'
    ],

    name: 'DEMO',

    views: [
        'bb.extjs.demo.view.MainView'
    ],
    
    controllers: [
    	'bb.extjs.demo.controller.Main'
    ],
    
    launch: function() {
        Ext.create('bb.extjs.demo.view.MainView');
    }
});

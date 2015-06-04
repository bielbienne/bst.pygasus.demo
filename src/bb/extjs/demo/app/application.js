Ext.define('bb.extjs.demo.Application', {
    extend: 'Ext.app.Application',
    requires: [
        'Ext.data.Request',
    	'scaffolding.bufferedstore.Card'
    ],

    name: 'DEMO',

    views: [
        'bb.extjs.demo.view.MainView',
        'bb.extjs.demo.view.CardView'
    ],
    
    controllers: [
    	'bb.extjs.demo.controller.Main',
        'bb.extjs.demo.controller.Card'
    ],
    
    launch: function() {
        Ext.create('bb.extjs.demo.view.MainView');
    }
});

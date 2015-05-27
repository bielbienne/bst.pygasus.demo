Ext.define('bb.extjs.demo.view.MainView', {
    extend: 'Ext.container.Viewport',
    
    requires: [
    	'scaffolding.grid.Card',
    	'scaffolding.editgrid.Card',
    	'scaffolding.form.Card',
    	'scaffolding.display.Card'
    ],    

    itemId: 'mainView',
    layout: 'fit',

    initComponent: function() {
        var me = this;

        Ext.applyIf(me, {
        	xtype: 'panel',
        	items: [{
	       		xtype: 'tabpanel',
            	items: [{
	                xtype: 'GridCard',
	                title: 'Grid'
	            },
	            {
	            	xtype: 'EditGridCard',
	            	title: 'EditGrid'
	            },
	            {
	            	xtype: 'FormCard',
	            	title: 'Form'
	            },
	            {
	            	xtype: 'DisplayCard',
	            	title: 'Display'
	            }]
			}]
        });

        me.callParent(arguments);
    }

});

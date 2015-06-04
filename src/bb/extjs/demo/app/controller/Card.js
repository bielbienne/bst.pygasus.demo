Ext.define('bb.extjs.demo.controller.Card', {
    extend: 'Ext.app.Controller',

    requires: [
        'scaffolding.display.Card'
    ],

    refs: [{
        ref: 'display',
        selector: 'DisplayCard'
    }],


    init: function(){
        this.control({
            '#cardView button[action=delete]': {
                click: this.onDeleteClick
            },
            'window': {
                close: this.onCloseClick
            }
        });
    },

    addContent: function(record){
        var view = Ext.create('bb.extjs.demo.view.CardView');
        var display = this.getDisplay();
        display.loadRecord(record);
        view.setTitle(record.getData()['name']);
        view.show();
    },

    onCloseClick: function(){
        var grid = this.application.controllers.get('bb.extjs.demo.controller.Main').getGrid();
        var sel = grid.getSelectionModel();
        sel.deselect(sel.getSelection());
    },

    onDeleteClick: function(e, eOpts){
        var display = this.getDisplay();
        var record = display.getRecord();    
        this.application.controllers.get('bb.extjs.demo.controller.Main').deleteRecord(record);
        e.up('window').close();
    }

});

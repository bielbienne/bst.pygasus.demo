Ext.define('bb.extjs.demo.controller.Main', {
    extend: 'Ext.app.Controller',
    
    requires: [
        'scaffolding.bufferedstore.Card'
    ],    

    refs: [{
        ref: 'form',
        selector: 'FormCard'
    }, {
        ref: 'idform',
        selector: 'FormCard field[name=id]'
    }],

    init: function(){
        this.control({
            'FormCard button[action=save]': {
                click: this.onFormSave
            },
            '#mainView': {
                afterrender: this.onContentRendered
            }
        });
        
    },


    onContentRendered: function(){
        this.getIdform().hide();
    },


    
    onFormSave: function(button, event){
        var form = this.getForm();
        var store = this.getStore('scaffolding.store.Card');
        var record = Ext.create('scaffolding.model.Card');
        form.updateRecord(record);
        record.set('id', 0);
        store.add(record);
    }


});

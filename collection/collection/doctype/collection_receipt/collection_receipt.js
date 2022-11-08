// Copyright (c) 2022, Hns and contributors
// For license information, please see license.txt

frappe.ui.form.on('Collection Receipt', {
	customer: function(frm) {
		frm.call({
			method:"invoice_details",
			doc:frm.doc,
			callback:function(r){
				if(r.message){
					console.log(r.message)
					frm.fields_dict.receipt_collection_details.grid.update_docfield_property(
						"invoice_no","options",r.message
					);
				}
			}
		})
	}
});
frappe.ui.form.on('Receipt Collection Details', {
	from_render: function(frm) {
		frm.call({
			method:"invoice_details",
			doc:frm.doc,
			callback:function(r){
				if(r.message){
					console.log(r.message)
					frm.fields_dict.receipt_collection_details.grid.update_docfield_property(
						"invoice_no","options",r.message
					);
				}
			}
		})
	},
	invoice_no: function(frm,cdt,cdn) {
		var child=locals[cdt][cdn]
		frm.call({
			method:"collection.collection.doctype.collection_receipt.collection_receipt.get_invoice_details",
			args:{
				invoice:child.invoice_no
			},
			callback:function(r){
				if(r.message){
					child.invoice_date=r.message[0]
					child.planned_amount=r.message[1]
					child.upto_received=r.message[2]
					frm.refresh_fields("receipt_collection_details")
					
				}
			}
		})
	},

})
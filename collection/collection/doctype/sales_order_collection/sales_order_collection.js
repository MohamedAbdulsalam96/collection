// Copyright (c) 2022, Hns and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Order Collection', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('Sales Invoice Items', {
	planned_amount: function(frm) {
		frappe.call({
			method:"total_order_amount",
			doc:frm.doc,
			callback:function(r){
				if(r.message){
					frm.refresh_fields("total_order_amt")
				}

			}
		})

	}
});

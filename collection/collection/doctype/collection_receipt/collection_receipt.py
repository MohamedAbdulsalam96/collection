# Copyright (c) 2022, Hns and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CollectionReceipt(Document):
	@frappe.whitelist()
	def invoice_details(self):
		invoice=[]
		clst=frappe.db.get_all("Sales Order Collection",{"customer":self.customer},["name"])
		for i in clst:
			doc=frappe.get_doc("Sales Order Collection",i.get("name"))
			for i in doc.items:
				if i.status!="Complete":
					invoice.append(i.bill_no)
		return invoice
	
	def after_insert(self):
		for i in self.receipt_collection_details:
			invdet=frappe.db.get_value("Sales Invoice Items",{"bill_no":i.invoice_no},["parent"])
			if invdet:
				doc=frappe.get_doc("Sales Order Collection",invdet)
				for j in doc.items:
					if j.bill_no==i.invoice_no:
						j.rec_amount=j.rec_amount+i.amount
						j.rec_date=self.date
						if not j.rec_det:
							j.rec_det=str(self.date)+":"+str(i.amount)
						else:
							j.rec_det=str(j.rec_det)+"\n"+str(self.date)+":"+str(i.amount)
						if j.planned_amount==i.amount:
							j.status="Complete"
				doc.save(ignore_permissions=True)


	
@frappe.whitelist()
def get_invoice_details(invoice):
	invdet=frappe.db.get_value("Sales Invoice Items",{"bill_no":invoice},["planed_date","planned_amount","rec_amount"])
	return invdet

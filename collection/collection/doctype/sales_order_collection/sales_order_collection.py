# Copyright (c) 2022, Hns and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SalesOrderCollection(Document):
	@frappe.whitelist()
	def total_order_amount(self):
		amt=[]
		for item in self.get("items"):
			amt.append(item.planned_amount)
		self.total_order_amt=sum(amt)
		return True
            
	# def validate(self):
	# 	self.validate_customer()
    
	# def validate_customer(self):
	# 	cust=frappe.get_all("Sales Order Collection",["order_no"])
	# 	if cust:
	# 		for i in cust:
	# 			if self.order_no==i.get("order_no"):
	# 				frappe.throw("Sales Order Collection Already Exist against Order no {0}".format(self.order_no))

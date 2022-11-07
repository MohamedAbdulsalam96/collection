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
		# self.validate_customer()
    
	# def validate_customer(self):
	# 	self.description="Abc"
	# 	customer=[]
	# 	cust=frappe.get_all("Sales Order Collection",["customer"])
		# if cust:
		# 	for i in cust:
		# 		# if self.customer==i.get("customer"):
		# 		pass
					# frappe.throw("Sales Order Collection Already Exist For Customer {0}".format(self.customer))

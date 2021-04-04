from django.contrib import admin
from MedicalStoreApp.models import Company,CompanyBank,Medicine,MedicalDetails,Employee,EmployeeSalary,EmployeeBank,Customer,CustomerRequest,CompanyAccount,Bill,BillDetails


admin.site.site_header = "Medical Store Management"
admin.site.site_title = "Medical Store Management"

admin.site.register(Company)
admin.site.register(CompanyBank)
admin.site.register(CompanyAccount)
admin.site.register(Medicine)
admin.site.register(MedicalDetails)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(CustomerRequest)
admin.site.register(EmployeeSalary)
admin.site.register(EmployeeBank)
admin.site.register(Bill)
admin.site.register(BillDetails)
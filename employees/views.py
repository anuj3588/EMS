from django.db import transaction
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, redirect, HttpResponse

from employees.forms import EmpRegister
from employees import models as emp_models


class Employee(View):
    def get(self, request, *args, **kwargs):
        template_name = 'employees/register.html'
        form = EmpRegister()
        return render(request, template_name, {'form': form})

    def post(self, request):
        form = EmpRegister(request.POST, request.FILES)
        # import pdb
        # pdb.set_trace()
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Perform your database operations here
                    employee_obj = emp_models.Employee(
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        email=form.cleaned_data['email']
                    )
                    employee_obj.save()
                    employee_detail = emp_models.EmployeeDetails(
                        employee=employee_obj,
                        address=form.cleaned_data['address'],
                        phone_number=form.cleaned_data['phone_number'],
                        document=request.FILES['document']

                    )
                    employee_detail.save()

                # If everything is successful, commit the transaction
                transaction.commit()
                return HttpResponse("Success")

            except Exception as e:
                # If any exception occurs, rollback the transaction
                transaction.rollback()
                print(e)
                return HttpResponse("Failed")
        else:
            # Form is not valid, return validation errors
            return JsonResponse({'errors': form.errors}, status=400)

        return HttpResponse("Something Went wrong")

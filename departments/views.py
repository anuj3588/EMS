# views.py
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def department_list(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM departments_department;')
            departments = cursor.fetchall()
            departments_dict = [{'id': department[0], 'name': department[1], 'description': department[2]} for
                                department in departments]

        return JsonResponse({'departments': departments_dict}, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        description = data.get('description')

        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO departments_department (name, description) VALUES (%s, %s);',
                           [name, description])

        return JsonResponse({'message': 'Department created successfully'}, status=201)


@csrf_exempt
def department_detail(request, pk):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM departments_department WHERE id = %s;', [pk])
        department = cursor.fetchone()

    if not department:
        return JsonResponse({'message': 'Department not found'}, status=404)

    if request.method == 'GET':
        department = {'id': department[0], 'name': department[1], 'description': department[2]}
        return JsonResponse({'Department': department})

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        description = data.get('description')

        with connection.cursor() as cursor:
            cursor.execute('UPDATE departments_department SET name = %s, description = %s WHERE id = %s;',
                           [name, description, pk])

        return JsonResponse({'message': 'Department updated successfully'})

    elif request.method == 'DELETE':
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM departments_department WHERE id = %s;', [pk])

        return JsonResponse({'message': 'Department deleted successfully'}, status=204)

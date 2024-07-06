from django.shortcuts import render
from django.http import JsonResponse
from account.models import Course
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def apiCourse(request):
    if (request.method == "GET"):
        #Serialize the data into json
        data = serializers.serialize("json", Course.objects.all())
        #Turn the JSON data into a dict and send as JSON response
        return JsonResponse(json.loads(data), safe=False)

    if (request.method == "POST"):
            # Turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
            # filter data
        if not body:
            data = '{"message": "data is not json type!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
        else:
            created = Course.objects.create(
                course_name=body['course_name']
            )
            data = '{"message": "data successfully created!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)

    if (request.method == 'PUT'):
        try:
            body = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)

        if 'course_name' not in body:
            return JsonResponse({'message': 'Missing course name'}, status=400)

        courses = Course.objects.filter(course_name=body['course_name'])
        if courses.count() == 0:
            return JsonResponse({'message': 'Course not found'}, status=404)
        elif courses.count() > 1:
            return JsonResponse({'message': 'Multiple courses found'}, status=409)
        else:
            course = courses[0]
            course.course_name = body.get('course_name', course.course_name)
            course.save()
            return JsonResponse({'message': 'Course successfully updated!', 'course_name': course.course_name})

    if (request.method == 'DELETE'):
        try:
            body = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)

        if 'course_name' in body:
            courses = Course.objects.filter(course_name=body['course_name'])
            if courses.count() == 0:
                return JsonResponse({'message': 'Course not found'}, status=404)
            else:
                courses.delete()
                return JsonResponse({'message': 'Course(s) successfully deleted!'})
        else:
            try:
                course = Course.objects.latest('course_created_date')
                course.delete()
                return JsonResponse({'message': 'Course successfully deleted!'})
            except Course.DoesNotExist:
                return JsonResponse({'message': 'No courses found'}, status=404)


# Command CMD
            # <!Get!>
            # curl http://127.0.0.1:8000/api/course
            # <!POST!>
            # curl -X POST -H "Content-Type: application/json" -d '{"course_name":"example_course"}' http://127.0.0.1:8000/api/course
            # <!PUT!>
            # curl -X PUT -H "Content-Type: application/json" -d '{"course_name":"name course", "new_course_name":"Updated Course Name"}' http://127.0.0.1:8000/api/course
            # <!DELETE!>
            # curl -X DELETE -H "Content-Type: application/json" -d '{"course_name":"Updated Course Name"}' http://127.0.0.1:8000/api/course
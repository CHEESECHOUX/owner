
import json

from django.http import JsonResponse
from django.views import View

from owner.models import Owner, Dog

class OwnerView(View): 
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name  = data['name'],
            age   = data['age'],
            email = data['email']
        )
        return JsonResponse({'messasge':'created'}, status=201)

#    def get(self, request):
#        owners = Owner.objects.all()
#        result  = [] 
#
#        for owner in owners:
#            owner_information = {
#                'name'  : owner.name,
#                'email' : owner.email,
#                'age'   : owner.age
#            }
#            result.append(owner_information)     
#        return JsonResponse({'result':result}, status=200)

    def get(self, request):
            owners = Owner.objects.all()
            result  = [] 

            for owner in owners:
                dogs = owner.dog_set.all()
                dog_list = []

                for dog in dogs:
                    dog_information = {
                        'name' : dog.name,
                        'age'  : dog.age
                    }
                    dog_list.append(dog_information)

                owner_information = {
                            'name' : owner.name,
                            'email' : owner.email,
                            'age' : owner.age,
                            'dogs' : dog_list
                        }
                result.append(owner_information)     
            return JsonResponse({'result':result}, status=200)

class DogView(View):
    def post(self, request):
        try:
            data  = json.loads(request.body)
            owner = Owner.objects.get(id=data['owner_id'])
            dog   = Dog.objects.create( 
                name  = data['name'],
                age   = data['age'],
                owner = owner
            )
            return JsonResponse({'messasge':'created'}, status=201)
        except Owner.DoesNotExist:
            return JsonResponse({'messasge':'Bad Request'}, status=400)

    def get(self, request):
        dogs = Dog.objects.all()
        result  = [] 

        for dog in dogs:
            dog_information = {
                'name'  : dog.name,
                'age'   : dog.age,
                'owner' : dog.owner.name
            }
            result.append(dog_information)     
        return JsonResponse({'result':result}, status=200)
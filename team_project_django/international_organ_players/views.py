from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.shortcuts import render, redirect

from .create_random_objects import CreateRandomOrganDonor
from .forms import SignUpForm, LoginForm, EditUserForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Location
from .serializers import LocationSerializer

class LocationListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Location items for given requested user
        '''
        locations = Location.objects
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Location with given Location data
        '''
        data = {
            'location_name': request.data.get('location_name'), 
            'coordinator_x': request.data.get('coordinator_x'), 
            'coordinator_y': request.data.get('coordinator_y')
        }
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, location):
        try:
            return Location.objects.get(location_name = location)
        except Location.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, location, *args, **kwargs):
        '''
        Retrieves the location with given location_id
        '''
        location_instance = self.get_object(location)
        if not location_instance:
            return Response(
                {"res": "Object with location name does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LocationSerializer(location_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, location, *args, **kwargs):
        '''
        Updates the location item with given location_id if exists
        '''
        location_instance = self.get_object(location)
        if not location_instance:
            return Response(
                {"res": "Object with location id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'location_name': request.data.get('location_name'), 
            'coordinator_x': request.data.get('coordinator_x'), 
            'coordinator_y': request.data.get('coordinator_y')
        }
        serializer = LocationSerializer(instance = location_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, location, *args, **kwargs):
        '''
        Deletes the location item with given location_id if exists
        '''
        location_instance = self.get_object(location)
        if not location_instance:
            return Response(
                {"res": "Object with location id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        location_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


@login_required
def home(request):          #strona główna
    # log.info(f"User {request.user} went to the homepage")
    return render(request, 'home.html')

def login_view(request):    #wbudowana funkcja login (dlatego login_view)
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # log.info(f"User {username} just logged in")
                return redirect('../')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):   #wbudowana funkcja logout (dlatego logout_view)
    logout(request)
    # log.info(f"User {request.user} just logged out")
    return redirect('../login/')

def signup(request):        #rejestracja
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # log.info(f"User {username} just registered")
            return redirect('../')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def create_random_organ_donor(request):
        create_random_organ_donor = CreateRandomOrganDonor()
        create_random_organ_donor.create_random_organ_donor()
        return redirect("../")
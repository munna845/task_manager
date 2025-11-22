from rest_framework import serializers
from . models import User,Project,Task
#User serializer
class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  class Meta:
    model = User
    fields = ['id','name','email','password','created_at']


#Project serializer
class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ['id','name','description','start_date','end_date','created_by']

#Task serializer
class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ['id','title','description','status','priority','due_date','project','assigned_to','created_by','created_at','updated_at']
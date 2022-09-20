from rest_framework import serializers


from.models import Bookingreq, Category, Employee,File,Userregister



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
        


class UserregSerializers(serializers.ModelSerializer):
    class Meta:
        model = Userregister
        fields = '__all__'
                
        
        
        
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"        
        
        
        
class BookingreqSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bookingreq
        fields = '__all__'        
        
    
        
        
        
        



        
        
        
        

        
        
                
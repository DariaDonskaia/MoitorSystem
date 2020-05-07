from django.db import models

def user_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Type(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

class Node(models.Model):
    node_description = models.CharField(max_length=100)
    node_MAC = models.IntegerField(unique=True)
    node_type = models.ForeignKey(Type, on_delete = models.CASCADE)
    node_x = models.IntegerField(null=True)
    node_y = models.IntegerField(null=True)

class Node_Data(models.Model):
    node_data_node = models.ForeignKey(Node, on_delete = models.CASCADE)
    node_data_getdata = models.TextField()
    node_data_time = models.DateTimeField()
    node_data_battery = models.IntegerField()

class Gateway(models.Model):
    gateway_description = models.CharField(max_length=100)
    gateway_MAC = models.IntegerField(unique=True)
    gateway_image = models.ImageField(upload_to='uploads/',null = True, blank = True)


#class Users(models.Model):
 #   users_name = models.CharField(max_length=15)
 #   users_surname = models.CharField(max_length=25)
 #   users_login = models.CharField(max_length=10)
 #   users_password = models.CharField(max_length=10)
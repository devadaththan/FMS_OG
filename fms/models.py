from django.db import models

# Create your models here.



class newfile(models.Model):
    file_no = models.IntegerField(default=10, unique=True)
    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is being created (not updated)
            max_value = newfile.objects.aggregate(models.Max('file_no')) 
            max_file_no = max_value['file_no__max']
            self.file_no = max_file_no + 1 if max_file_no is not None else 1  # Increment the field
        super().save(*args, **kwargs)
    reciver = models.CharField(max_length=20,default='principal')
    senders=models.CharField(max_length=10,default='admin')
    created_date=models.DateTimeField()

    def __str__(self):
        return f'File No: {self.file_no}'
    



class v_file(models.Model):
    vf_computer_no=models.IntegerField(primary_key=True)
    vf_file_no=models.ForeignKey(newfile,on_delete=models.CASCADE,to_field='file_no',null=True)
    vf_description=models.TextField()
    vf_file_opned=models.DateField()
    vf_file_closed=models.DateField()




    

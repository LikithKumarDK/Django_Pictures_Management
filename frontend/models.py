from django.db import models
import uuid




#Image model
class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', related_name="images", on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255, null=True, blank=True)
    original_url = models.TextField()
    file_size = models.IntegerField()
    file_format = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=[
        ('uploaded', 'Uploaded'),
        ('processed', 'Processed'),
        ('edited', 'Edited'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Image'

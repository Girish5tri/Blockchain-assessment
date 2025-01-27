from django.db import models

# Create your models here.
class BlockchainNode(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)  
    uptime = models.FloatField()  
    resource_utilization = models.JSONField()  

    def __str__(self):
        return self.name
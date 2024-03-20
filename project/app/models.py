from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)


class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)


class CustomerSupport(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    representative = models.CharField(max_length=100)
    notes = models.TextField()


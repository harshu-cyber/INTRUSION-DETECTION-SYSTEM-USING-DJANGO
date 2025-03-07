from django.db import models

# Create your models here.
from django.db import models

# ✅ Model to Store Intrusion Logs
class IntrusionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto timestamp
    image = models.ImageField(upload_to='intrusion_images/', null=True, blank=True)  # Intrusion Image
    detected_person = models.CharField(max_length=100, default="Unknown")  # Name of detected person

    def __str__(self):
        return f"{self.timestamp} - {self.detected_person}"

# ✅ Model to Store Known Faces
class KnownPerson(models.Model):
    name = models.CharField(max_length=100)  # Person's Name
    image = models.ImageField(upload_to='known_faces/')  # Store Known Face Image

    def __str__(self):
        return self.name

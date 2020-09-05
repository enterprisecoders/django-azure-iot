from django.db import models
import uuid


class SessionData(models.Model):
    session_id = models.UUIDFIELD(blank=False, unique=True)
    authorization_code = models.CharField(max=6000, blank=False)
    client_id = models.CharField(max=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)
    valid_till = models.DateTimeField(blank=True)

    # def save(self, *args, **kwargs):
    #     if self.valid_till is None:
    #         self.valid_till = datetime.utcnow() + timedelta(hours=24)
    #     return super(SessionData, self).save(*args, **kwargs)

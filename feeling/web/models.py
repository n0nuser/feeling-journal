from django.db import models


class Journal(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ocurred_at = models.DateTimeField(blank=False, null=True)
    number_of_times = models.IntegerField(blank=False, null=True)
    situation_emotion = models.CharField(max_length=1000, blank=False, null=True)
    afterwards_feeling = models.CharField(max_length=1000, blank=False, null=True)

    def __str__(self):
        return f"{self.ocurred_at} - {self.situation_emotion:5.50}"

    class Meta:
        verbose_name_plural = "Journal"
        ordering = ["-ocurred_at"]


class Thought(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    journal = models.ForeignKey(Journal, on_delete=models.DO_NOTHING, blank=True, null=True)
    thought = models.CharField(max_length=1000, blank=False, null=True)
    
    def __str__(self):
        return f"{self.created_at} - {self.user}"

    class Meta:
        verbose_name_plural = "Thoughts"
        ordering = ["-created_at"]
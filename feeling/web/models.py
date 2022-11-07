from django.db import models


class Journal(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ocurred_at = models.DateTimeField(blank=False, null=True)
    number_of_times = models.IntegerField(blank=False, null=True)
    situation_emotion = models.CharField(max_length=560, blank=False, null=True)
    afterwards_feeling = models.CharField(max_length=560, blank=False, null=True)

    def __str__(self):
        return f"{self.ocurred_at} - {self.situation_emotion:5.50}"

    class Meta:
        verbose_name_plural = "Journal"
        ordering = ["-ocurred_at"]


class Cue(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE, null=True)
    trigger = models.CharField(max_length=280, blank=False, null=True)
    general = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.trigger}"


class Routine(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE, null=True)
    response = models.CharField(max_length=280, blank=False, null=True)
    type = models.CharField(
        max_length=1, choices=[("M", "Mental"), ("E", "Emotional"), ("P", "Physical")], default="E"
    )
    general = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.response}"


class Reward(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE, null=True)
    reward = models.CharField(max_length=280, blank=False, null=True)
    general = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reward}"


class Habit(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ocurred_at = models.DateTimeField(blank=False, null=True)
    number_of_times = models.IntegerField(blank=False, null=True)
    cue = models.ForeignKey(Cue, on_delete=models.SET_NULL, blank=False, null=True)
    routine = models.ForeignKey(Routine, on_delete=models.SET_NULL, blank=False, null=True)
    reward = models.ForeignKey(Reward, on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return f"{self.ocurred_at} - {self.cue:5.50}"


class Thought(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    journal = models.ForeignKey(Journal, on_delete=models.DO_NOTHING, blank=True, null=True)
    thought = models.CharField(max_length=560, blank=False, null=True)

    def __str__(self):
        return f"{self.created_at} - {self.user}"

    class Meta:
        ordering = ["-created_at"]

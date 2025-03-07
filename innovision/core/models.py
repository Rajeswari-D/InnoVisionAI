from django.db import models

class StartupIdea(models.Model):
    title = models.CharField(max_length=255)  # Idea title
    description = models.TextField()  # Detailed idea
    submission_date = models.DateTimeField(auto_now_add=True)  # Auto timestamp
    prediction_result = models.TextField(blank=True, null=True)  # AI Evaluation Result

    def __str__(self):
        return self.title

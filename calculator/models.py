from django.db import models

class CalculationResult(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    input = models.TextField(max_length=15)
    result = models.TextField(max_length=15)

    def __str__(self):
        return f"Result for '{self.input}' at {self.timestamp}"
from django.db import models
from django.urls import reverse


class Task(models.Model):
    task_title = models.CharField(max_length=100)
    due_date = models.DateField()
    description = models.TextField()


    def get_detail_url(self):
        return reverse('tasks:detail', args=[self.pk])


    def get_delete_url(self):
        return reverse('tasks:delete', args=[self.pk])


    def get_update_url(self):
        return reverse('tasks:update', args=[self.pk])

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/course_images/', blank=True, null=True)
    video = models.FileField(upload_to='media/course_videos/', blank=True, null=True)
    content = models.TextField(blank=True)  # This field can contain HTML or Markdown text
    code_snippet = models.TextField(blank=True)  # Optional field for code examples
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

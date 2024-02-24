from django.db import models

class Teacher(models.Model):
      name = models.CharField(max_length=50)
      experience = models.TextField(max_length=50)
      about = models.TextField(max_length=100)
      photo = models.ImageField(blank=True)

      def __str__(self):
            return self.name
      

class Course(models.Model):
      title = models.CharField(max_length=50)
      desc = models.TextField(max_length=100)
      # photo = models.ImageField(blank=True)
      price = models.IntegerField()

      def __str__(self):
            return self.title
      
class Results(models.Model):
      photo = models.ImageField(blank=True)
      student_name = models.CharField(max_length=10)
      student_result = models.IntegerField()

      def __str__(self):
            return self.student_name
      

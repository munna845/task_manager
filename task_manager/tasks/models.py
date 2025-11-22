from django.db import models

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=15)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Project(models.Model):
  name =models.CharField(max_length=30)
  description = models.TextField(max_length=500)
  start_date = models.DateField()
  end_date = models.DateField(null=True,blank=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

  def __str__(self):
    return self.name
  
class Task(models.Model):
  STATUS_CHOICES =[
    ('pending', 'Pending'),
    ('in_progress', 'In_Progress'),
    ('completed', 'Completed'),
  ]
  PRIORITY_CHOICES =[
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('high','High'),
  ]

  title = models.CharField(max_length=50)
  description = models.TextField(max_length=500)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
  priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES,default='medium')
  due_date = models.DateField()
  project =models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
  assigned_to =models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

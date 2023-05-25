from django.db import models
from django.utils import timezone

class CategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class JobCreateModel(models.Model):
    jobtitle = models.CharField(max_length=255)
    jobdescription = models.TextField()
    NATURE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('Featured', 'Featured'),
    )
    nature = models.CharField(max_length=20, choices=NATURE_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    vacancy_count = models.PositiveIntegerField(default=1)
    deadline = models.DateTimeField()
    company_description = models.TextField()
    company_website = models.URLField(max_length=200) 
    responsibilities = models.TextField()
    qualifications = models.TextField()
    image = models.ImageField(upload_to='job_images')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.jobtitle



class ContactModel(models.Model) :
    sno =models.AutoField(primary_key=True)
    name =   models.CharField(max_length=255)
    email =  models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

class ApplyJobModel(models.Model):
    sno = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobCreateModel, on_delete=models.CASCADE, default=None)
    company = models.CharField(max_length=255)
    jobtitle = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    portfolio = models.URLField(max_length=200)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

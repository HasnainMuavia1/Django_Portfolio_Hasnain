from django.db import models
from django.contrib.auth.models import User


class extend(models.Model):
    ex_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extend')
    description = models.TextField()

    def __str__(self):
        return self.description


class Skills(models.Model):
    skill_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name


class Certifications_license(models.Model):
    cert_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certifications')
    certificate = models.CharField(max_length=100)
    url = models.URLField(max_length=400)
    institution = models.CharField(max_length=50)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.certificate


class Education(models.Model):
    education_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    Degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    year = models.CharField(max_length=30)

    def __str__(self):
        return self.institute


class Experience(models.Model):
    experience_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience')
    experience = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    year = models.CharField(max_length=30)

    def __str__(self):
        return self.experience


class image(models.Model):
    img = models.ImageField()

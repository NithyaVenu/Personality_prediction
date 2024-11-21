from django.db import models

# Create your models here.
TYPE_CHOICES = (
    ('type','TYPE'),
    ('english', 'ENGLISH'),
    ('maths','MATHS'),
    ('programming','PROGRAMMING'),
)
class AptiQues(models.Model):

    Type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='type')
    Question = models.TextField()
    Option1 = models.CharField(max_length=15)
    Option2 = models.CharField(max_length=15)
    Option3 = models.CharField(max_length=15)
    Option4 = models.CharField(max_length=15)
    Answer = models.CharField(max_length=15)

PERSON_CHOICES = (
    ('--select--','--SELECT--'),
    ('agree','AGREE'),
    ('strongly agree', 'STRONGLY AGREE'),
    ('disagree','DISAGREE'),
    ('strongly disagree','STRONGLY DISAGREE'),
    ('neither agree nor disagree','NEITHER AGREE NOR DISAGREE'),
)

class PersonQues(models.Model):

    Question = models.TextField()
    Openness_to_experience = models.CharField(max_length=30, choices=PERSON_CHOICES, default='--select--')
    Conscientiousness = models.CharField(max_length=30, choices=PERSON_CHOICES, default='--select--')
    Extraversion = models.CharField(max_length=30, choices=PERSON_CHOICES, default='--select--')
    Agreeableness = models.CharField(max_length=30, choices=PERSON_CHOICES, default='--select--')
    Neuroticism = models.CharField(max_length=30, choices=PERSON_CHOICES, default='--select--')



class BaseInfo(models.Model):

    Job_Id = models.IntegerField(default="101")
    Designation = models.CharField(max_length=30)
    Salary = models.CharField(max_length=30)
   

    class Meta:
        abstract = True

class JobDetails(BaseInfo):
     Place = models.CharField(max_length=30)

class JobRequirement(BaseInfo):
    
    
    Experience = models.CharField(max_length=30)
    Qualification = models.CharField(max_length=30)
    Key_Skills = models.CharField(max_length=30)
    

class PreferredCV(BaseInfo):
    
    PreferredCVs = models.ImageField(upload_to='pics')
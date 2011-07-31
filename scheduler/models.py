from django.contrib.auth.models import User
from django.db import models
import scheduler

class School(models.Model):
    def __str__(self):
        return "%s" % (self.name)
    def __unicode__(self):
        return u'%s' % (self.name)
    name = models.CharField(max_length=40)
    
class Department(models.Model):
    def __str__(self):
        return "%s (%s)" % (self.name, self.school)
    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.school)
    name = models.CharField(max_length=40)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    
class Proffesor(models.Model):
    def __str__(self):
        return "%s, (%s)" % (self.name, self.department)
    def __unicode__(self):
        return u'%s, (%s)' % (self.name, self.department)
    name = models.CharField(max_length=40)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

class Course(models.Model):
    def __str__(self):
        return "%s, (%s)" % (self.name, self.department)
    def __unicode__(self):
        return u'%s, (%s)' % (self.name, self.department)
    #General
    name = models.CharField(max_length=40, )
    proffesor = models.ForeignKey(Proffesor, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    
    #Semester
    SEMESTER_CHOICES = (
        ('F', 'Fall'),
        ('S', 'Spring'),
    )
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    year = models.IntegerField(max_length=4, validators=[scheduler.validateModernAndExistingYear])
    
    #Scheduling        
    HOUR_CHOICES = (    
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    MINUTE_CHOICES = (
        ('00', '00'),
        ('05', '05'),
        ('10', '10'),
        ('15', '15'),
        ('20', '20'),
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
        ('45', '45'),
        ('50', '50'),
        ('55', '55'),
    )
    PERIOD_CHOICES = (
        ('AM', 'AM'),
        ('PM', 'PM'),
    )
    startHour = models.CharField(max_length=2, choices=HOUR_CHOICES)
    startMinute = models.CharField(max_length=2, choices=MINUTE_CHOICES)
    startPeriod = models.CharField(max_length=2, choices=PERIOD_CHOICES)
    endHour = models.CharField(max_length=2, choices=HOUR_CHOICES)
    endMinute = models.CharField(max_length=2, choices=MINUTE_CHOICES)
    endPeriod = models.CharField(max_length=2, choices=PERIOD_CHOICES)
    days_of_the_week = models.CharField(max_length=7, validators=[scheduler.validateDayOfWeek])
    
class Class(models.Model):
    def __str__(self):
        return "%s; %s credits" % (self.course, self.credits)
    def __unicode__(self):
        return u'%s; %s credits' % (self.course, self.credits)
    #Grades
    credits = models.DecimalField(max_digits=3, decimal_places=2)
    GRADE_CHOICES = (
        ('4.33', 'A+'),
        ('4.00', 'A'),
        ('3.66', 'A-'),
        ('3.33', 'B+'),
        ('3.00', 'B'),
        ('2.66', 'B-'),
        ('2.33', 'C+'),
        ('2.00', 'C'),
        ('1.66', 'C-'),
        ('1.00', 'D'),
        ('0.00', 'F'),
    )
    grade = models.CharField(max_length=4, choices=GRADE_CHOICES)
    course = models.ForeignKey(Course)
    user = models.ForeignKey(User)
    
class UserProfile(models.Model):
    def __str__(self):
        return "%s" % (self.user)
    def __unicode__(self):
        return u'%s' % (self.user)
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    major1 = models.CharField(max_length=40)
    major2 = models.CharField(max_length=40, blank=True)
    minor1 = models.CharField(max_length=40, blank=True)
    minor2 = models.CharField(max_length=40, blank=True)
    
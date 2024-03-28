from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

"""--------------------------User's profile table----------------------------------"""
class UserProfile(models.Model):    

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    pets = models.BooleanField(default=False)
    allergies = models.TextField(max_length=500, blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sleep_schedule = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.user.username


"""--------------------------Room Listing board table----------------------------------"""
class RoomListing(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    available_from = models.DateField()
    duration = models.CharField(max_length=100)  # Example: "3 months", "indefinite", etc.
    preferences = models.TextField(blank=True, null=True)  # Roommate preferences
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
"""-------------------------Messege box------------------------------------------------"""
class Message(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.user.username} to {self.recipient.user.username} at {self.timestamp}"
    
"""------------------------------Favorite the unit------------------------------------"""
class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='favorites')
    listing = models.ForeignKey(RoomListing, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'listing')  # Ensures a user can't favorite the same listing more than once

    def __str__(self):
        return f"{self.user.user.username} favorites {self.listing.title}"  
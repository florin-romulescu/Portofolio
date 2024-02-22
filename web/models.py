from django.db import models
from colorfield.fields import ColorField

class Owner(models.Model):
    """
    Represent the owner of the portofolio and its properties.
    Properties with blank=True and null=True are optional.
    """
    last_name = models.CharField(max_length=127, blank=False, null=False)
    first_name= models.CharField(max_length=127, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=True, null=True)
    github_url = models.URLField(max_length=200, blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

# Create your models here.
class Project(models.Model):
    """
    Represent a project and its properties.
    """
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=1023, null=False, blank=False)
    pub_date = models.DateField(null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class Tag(models.Model):
    """
    Represent a tag and its properties
    """
    name = models.CharField(max_length=31)
    color = ColorField(default='#FFFFFF') # white
    projects = models.ManyToManyField(Project, related_name="tags", null=True, blank=True)
    
    @property
    def fg_color(self):
        """
        Determine whether the foreground color should be white or black
        based on the background color.
        """
        # Convert the hexadecimal color code to RGB
        r = int(self.color[1:3], 16)
        g = int(self.color[3:5], 16)
        b = int(self.color[5:7], 16)

        # Calculate the luminance using the formula for relative luminance
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255

        # Determine if the luminance is above a threshold
        # If the luminance is high, use black as the foreground color, otherwise use white
        if luminance > 0.5:
            return '#000000'  # Black
        else:
            return '#FFFFFF'  # White
        
    def __str__(self):
        return self.name
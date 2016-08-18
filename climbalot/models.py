from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator

# Grade Choices are defined outside of classes because two classes use their values (i.e. Monkey and Session).
BOULDER_COLOR_GRADES = (
    ('Y', 'Yellow'),
    ('G', 'Green'),
    ('R', 'Red'),
    ('B', 'Blue'),
    ('O', 'Orange'),
    ('P', 'Purple'),
    ('K', 'Black'),
)

BOULDER_V_GRADES = (
    ('V1', 'V1'),
    ('V2', 'V2'),
    ('V3', 'V3'),
    ('V4', 'V4'),
    ('V5', 'V5'),
    ('V6', 'V6'),
    ('V7', 'V7'),
    ('V8', 'V8'),
    ('V9', 'V9'),
    ('V10', 'V10'),
)

CLIMBING_Y_GRADES = (
    ('5.7', '5.7'),
    ('5.8', (
            ('5.8-', '5.8-'),
            ('5.8+', '5.8+'),
        )
    ),
    ('5.9', (
            ('5.9-', '5.9-'),
            ('5.9+', '5.9+'),
        )
    ),
    ('5.10', (
            ('5.10a', '5.10a'),
            ('5.10b', '5.10b'),
            ('5.10c', '5.10c'),
            ('5.10d', '5.10d'),
        )
    ),
    ('5.11', (
            ('5.11a', '5.11a'),
            ('5.11b', '5.11b'),
            ('5.11c', '5.11c'),
            ('5.11d', '5.11d'),
        )
    ),
    ('5.12', (
            ('5.12a', '5.12a'),
            ('5.12b', '5.12b'),
            ('5.12c', '5.12c'),
            ('5.12d', '5.12d'),
        )
    ),
)

# Create your models here.
class Gym(models.Model):
    gym = models.CharField(max_length = 25)

    def __str__(self):
        return self.gym

class Monkey(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("monkey name", max_length = 25, help_text="Name your monkey")
    # Validate crest image size through a script on upload. See http://goo.gl/fyTaqd
    # Need to rework image upload. Media serving not working properly.
    crest = models.ImageField(upload_to='crests/')
    date_created = models.DateTimeField(auto_now_add = True)
    home_gym = models.ForeignKey(Gym)
    experience = models.IntegerField(default = 0, validators = [MinValueValidator(0)])
    level = models.IntegerField(default = 1, validators = [MinValueValidator(1)])
    main_color_grade = models.CharField(max_length = 1,choices = BOULDER_COLOR_GRADES, blank = True)
    main_v_grade = models.CharField(max_length = 3, choices = BOULDER_V_GRADES, blank = True)
    main_y_grade = models.CharField(max_length = 5,choices = CLIMBING_Y_GRADES, blank = True)

    def __str__(self):
        return self.name

    def create_session(self):
        return Session()#Args will go here.

class Quest(models.Model):
    QUEST_STATUS = (
        ('A', 'Active'),
        ('C', 'Completed'),
        ('F', 'Failed'),
    )

    start_date = models.DateField()
    monkey = models.ForeignKey(Monkey, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    short_description = models.TextField()
    c_value = models.CharField(max_length = 1, choices = BOULDER_COLOR_GRADES, blank = True)
    v_value = models.CharField(max_length = 3, choices = BOULDER_V_GRADES, blank = True)
    y_value = models.CharField(max_length = 5, choices = CLIMBING_Y_GRADES, blank = True)
    attempts_total = models.IntegerField(default = 0)
    days_open = models.IntegerField(default = 1)
    status = models.CharField(max_length = 1, choices = QUEST_STATUS)

    def __str__(self):
        return self.name


# Session class must come after Quest class, since it references it as a foreign key.
class Session(models.Model):
    monkey = models.ForeignKey(Monkey, on_delete=models.CASCADE)
    session_date = models.DateField()
    gym = models.ForeignKey(Gym)
    extra_points = models.IntegerField(default = 0, blank = True, null = True)
    # Map values for yes/no Booleans in forms by using the following: {{ value|yesno: "Yes, No"}}.  For additional information see: https://goo.gl/WvyK6f
    workout = models.BooleanField(default = False)
    # Can pipe through quest status by using : {{ session.quest_<number>_id.status }}. See http://goo.gl/SWjPaZ
    quest_one_id = models.ForeignKey(Quest, related_name = "quest_one", on_delete = models.SET_NULL, blank = True, null = True)
    quest_one_attempts = models.IntegerField(default = 0, blank = True, null = True)
    quest_two_id = models.ForeignKey(Quest, related_name = "quest_two", on_delete = models.SET_NULL, blank = True, null = True)
    quest_two_attempts = models.IntegerField(default = 0, blank = True, null = True)
    quest_three_id = models.ForeignKey(Quest, related_name = "quest_three", on_delete = models.SET_NULL, blank = True, null = True)
    quest_three_attempts = models.IntegerField(default = 0, blank = True, null = True)
    session_exp = models.IntegerField(default = 0)

    def __str__(self):
        return "%s at %s on %s" % (self.monkey, self.gym, self.session_date.strftime('%m/%d/%Y'))

    class Meta:
        ordering = ['-session_date']



# Class for inputing scores for sessions involving Colored Bouldering Route ranks (using SBP scale)
class C_Routes(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE, blank = True, null = True)
    yellow = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    red = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)
    orange = models.IntegerField(default=0)
    purple = models.IntegerField(default=0)
    black = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'C-Routes'

# Class for inputing scores for sessions involving V Bouldering Route ranks.
class V_Routes(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE, blank = True, null = True)
    v1 = models.IntegerField(default=0)
    v2 = models.IntegerField(default=0)
    v3 = models.IntegerField(default=0)
    v4 = models.IntegerField(default=0)
    v5 = models.IntegerField(default=0)
    v6 = models.IntegerField(default=0)
    v7 = models.IntegerField(default=0)
    v8 = models.IntegerField(default=0)
    v9 = models.IntegerField(default=0)
    v10 = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'V-Routes'

# Class for inputing scores for sessions involving Yosemite Climbing Route ranks.
class Y_Routes(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE, blank = True, null = True)
    # fields are prepended with c (for climbing) because Django gets confused if fields start with numbers.
    c5_7 = models.IntegerField('5.7', default=0)
    c5_8_neg = models.IntegerField('5.8-',default=0)
    c5_8_pos = models.IntegerField('5.8+',default=0)
    c5_9_neg = models.IntegerField('5.9-', default=0)
    c5_9_pos = models.IntegerField('5.9+', default=0)
    c5_10_a = models.IntegerField('5.10a', default=0)
    c5_10_b = models.IntegerField('5.10b', default=0)
    c5_10_c = models.IntegerField('5.10c', default=0)
    c5_10_d = models.IntegerField('5.10d', default=0)
    c5_11_a = models.IntegerField('5.11a', default=0)
    c5_11_b = models.IntegerField('5.11b', default=0)
    c5_11_c = models.IntegerField('5.11c', default=0)
    c5_11_d = models.IntegerField('5.11d', default=0)
    c5_12_a = models.IntegerField('5.12a', default=0)
    c5_12_b = models.IntegerField('5.12b', default=0)
    c5_12_c = models.IntegerField('5.12c', default=0)
    c5_12_d = models.IntegerField('5.12d', default=0)

    class Meta:
        verbose_name_plural = 'Y-Routes'

from django.db import models
from datetime import date
from django.contrib.auth.models import  PermissionsMixin, AbstractUser

class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=10, unique=True, blank=True, null=True)

    full_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    RANK_CHOICES = [
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
        ('diamond', 'Diamond'),
    ]
    rank = models.CharField(max_length=10, choices=RANK_CHOICES, default='bronze')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    def __str__(self):
        return str(self.username) if self.username else "Unnamed"

    def level_up(self):
        attendance_count = self.classes_attended.count()
        if attendance_count >= 20:
            self.rank = 'diamond'
        elif attendance_count >= 15:
            self.rank = 'platinum'
        elif attendance_count >= 10:
            self.rank = 'gold'
        elif attendance_count >= 5:
            self.rank = 'silver'
        else:
            self.rank = 'bronze'
        self.save()


class BlogModel(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.name

class Product(models.Model):
    p_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="products/")
    price = models.IntegerField()

    CATEGORY_CHOICES = [
        ('sports_equipment', 'Sports equipment'),
        ('protein', 'Protein'),
        ('smart_watch', 'Smart Watch'),
        ('clothes', 'Clothes'),
        ('accessories', 'Accessories'),
        ('weights', 'Weights'),
        ('sports_bags', 'Sports bags'),
        ('shoes', 'Shoes'),
        ('yoga_mat', 'Yoga mat'),
        ('supplement', 'Supplement'),
        ('towel', 'Towel'),
        ('shaker', 'Shaker'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='sports_equipment')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.p_id:
            last_product = Product.objects.order_by('-id').first()
            next_number = 77770000 if not last_product else max(77770000, int(last_product.p_id or 9999999) + 1)
            self.p_id = str(next_number)
        super().save(*args, **kwargs)

class GymClass(models.Model):  # Renamed from `Class` to avoid reserved keyword issues
    title = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

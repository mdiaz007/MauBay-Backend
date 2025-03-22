from django.db import models

# Create your models here.

# Cannot be null in the database. null = False
# Cannot be null in the forms. blank = False
class active(models.Model):
    
    # Universal
    # Removes plurality to name of model.
    class Meta:
        verbose_name_plural = "active"

    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=100, null=False, blank=False)
    title = models.TextField(max_length=50, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    post_date = models.DateField(auto_now=True)
    description = models.TextField(max_length=200, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)

    # Should be an ImageField!
    image_url = models.TextField(max_length=200, null=False, blank=False)

    category = models.CharField(max_length=50, null=False, blank=False, choices=[("Cars", "Cars"),("Jewelry", "Jewelry"),("Clothing", "Clothing")])
    condition = models.CharField(max_length=50, null=False, blank=False, choices=[("New", "New"),("Used", "Used")])

    listing_type = models.CharField(max_length=10, default="Active", editable=False, null=False)

    def __str__(self):
        return f"{self.id} | {self.user_id} | {self.title}"

class sold(models.Model):
    
    # Universal

    # Removes plurality to name of model.
    class Meta:
        verbose_name_plural = "sold"

    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=100, null=False, blank=False)
    title = models.TextField(max_length=50, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    post_date = models.DateField(auto_now=True)
    description = models.TextField(max_length=200, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)

    # Should be an ImageField!
    image_url = models.TextField(max_length=200, null=False, blank=False)

    category = models.CharField(max_length=50, null=False, blank=False, choices=[("Cars", "Cars"),("Jewelry", "Jewelry"),("Clothing", "Clothing")])
    condition = models.CharField(max_length=50, null=False, blank=False, choices=[("New", "New"),("Used", "Used")])

    # Sold
    sell_price = models.IntegerField(null=False, blank=False)
    sold_date = models.DateField(max_length=50, null=False, blank=False)
    listing_type = models.CharField(max_length=10, default="Sold", editable=False, null=False)

    def __str__(self):
        return f"{self.id} | {self.user_id} | {self.title}"

class draft(models.Model):
    
    # Universal
    # Removes plurality to name of model.
    class Meta:
        verbose_name_plural = "draft"

    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=100, null=False, blank=False)
    title = models.TextField(max_length=50, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    post_date = models.DateField(auto_now=True)
    description = models.TextField(max_length=200, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)

    # Should be an ImageField!
    image_url = models.TextField(max_length=200, null=False, blank=False)

    category = models.CharField(max_length=50, null=False, blank=False, choices=[("Cars", "Cars"),("Jewelry", "Jewelry"),("Clothing", "Clothing")])
    condition = models.CharField(max_length=50, null=False, blank=False, choices=[("New", "New"),("Used", "Used")])

    listing_type = models.CharField(max_length=10, default="Draft", editable=False, null=False)

    def __str__(self):
        return f"{self.id} | {self.user_id} | {self.title}"

class deleted(models.Model):
    
    # Universal
    # Removes plurality to name of model.
    class Meta:
        verbose_name_plural = "deleted"

    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=100, null=False, blank=False)
    title = models.TextField(max_length=50, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    post_date = models.DateField(auto_now=True)
    description = models.TextField(max_length=200, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)

    # Should be an ImageField!
    image_url = models.TextField(max_length=200, null=False, blank=False)

    category = models.CharField(max_length=50, null=False, blank=False, choices=[("Cars", "Cars"),("Jewelry", "Jewelry"),("Clothing", "Clothing")])
    condition = models.CharField(max_length=50, null=False, blank=False, choices=[("New", "New"),("Used", "Used")])

    listing_type = models.CharField(max_length=10, default="Draft", editable=False, null=False)

    def __str__(self):
        return f"{self.id} | {self.user_id} | {self.title}"

class maubay_users(models.Model):
    
    # Universal
    # Removes plurality to name of model.
    class Meta:
        verbose_name_plural = "maubay_users"

    user_id = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    account_created = models.DateField(auto_now=True)
    seller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id} | {self.username} | {self.seller}"   
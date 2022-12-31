from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    """
    Create category model and associate it with product model using one-to-many relationship
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        slug=models.SlugField(max_length=200, unique=True),
    )

    class Meta:
        # Parler does not support meta properties for translated fields
        # ordering = ['name']
        # indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(TranslatableModel):
    """
    Create product model and associate it with category model using many-to-one relationship
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        slug=models.SlugField(max_length=200),
        description=models.TextField(blank=True),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Parler does not support meta properties for translated fields
        # ordering = ['name']
        # indexes = [models.Index(fields=['id', 'slug']), models.Index(fields=['name']),
        indexes = [models.Index(fields=["-created_at"])]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

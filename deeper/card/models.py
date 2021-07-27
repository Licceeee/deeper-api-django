from django.db import models


class Timestamps(models.Model):
    """timestamp model"""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Timestamps):
    """model for card categories:
            family, friends, partners, etc
    """
    name = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=50, null=True, blank=False)
    icon_web = models.CharField(max_length=50, default="fas fa-heart")
    icon_mobile = models.CharField(max_length=50, default="heart")
    icon_package_name_mobile = models.CharField(max_length=90,
                                                default="AntDesign")
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    def get_nr_questions(self):
        return self.question_set.count()
    get_nr_questions.short_description = "# Questions"


class Question(Timestamps):
    """model for card question:
            how do you feel about etc...
    """
    content = models.CharField(max_length=256, unique=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.content}"
    
    def get_categories(self):
        return ", ".join([
            category.name for category in self.categories.all()])
    get_categories.short_description = "Categories"
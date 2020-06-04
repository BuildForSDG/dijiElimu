from django.db import models


class Subscription(models.Model):
    TYPES = [
        ('WK', 'Weekly'),
        ('MT', 'Monthly'),
        ('FL', 'Full')
    ]
    subscription_type = models.CharField(
        max_length=100, choices=TYPES)
    description = models.TextField(null=True)
    is_paid = models.BooleanField(default=False)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    amount_paid = models.DecimalField(
        decimal_places=2, max_digits=10, default=0.00)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(
        'users.User', null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(
        'course.Course', null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('date_subscribed',)

    def __str__(self):
        return self.subscription_type

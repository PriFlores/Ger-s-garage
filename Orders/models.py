from django.db import models



class Orders(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    emailAddress = models.EmailField(max_length= 250, blank= True)

    class Meta:
        db_table = 'Orders'
        ordering = ('created',)

    def __str__(self):
        return 'Orders {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_items(self):
        return OrdersItem.objects.filter(orders=self)


class OrdersItem(models.Model):
    orders = models.ForeignKey(Orders, related_name= 'items', on_delete=models.CASCADE)
    product = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

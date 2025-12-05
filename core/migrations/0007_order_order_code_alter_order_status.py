
from django.db import migrations, models
import random
import string


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_stocklevel_quantity_sold'),
    ]

    def generate_codes(apps, schema_editor):
        Order = apps.get_model('core', 'Order')
        existing = set(Order.objects.exclude(order_code__isnull=True).values_list('order_code', flat=True))
        for order in Order.objects.all():
            if order.order_code:
                continue
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            while code in existing:
                code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            order.order_code = code
            order.save(update_fields=['order_code'])
            existing.add(code)

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_code',
            field=models.CharField(blank=True, null=True, default=None, max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled'), ('REFUNDED', 'Refunded')], default='DRAFT', max_length=20),
        ),
        migrations.RunPython(generate_codes, migrations.RunPython.noop),
    ]

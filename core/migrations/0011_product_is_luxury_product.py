
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_add_return_exchange_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_luxury_product',
            field=models.BooleanField(default=False),
        ),
    ]

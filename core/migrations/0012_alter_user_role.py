
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_product_is_luxury_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('OWNER', 'Owner'), ('CASHIER', 'Cashier'), ('SALES_ASSOCIATE', 'Sales Associate')], default='SALES_ASSOCIATE', max_length=20),
        ),
    ]


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_product_packaging_condition_product_provenance_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocklevel',
            name='quantity_sold',
            field=models.IntegerField(default=0),
        ),
    ]

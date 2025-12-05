
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_image_product_material_composition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

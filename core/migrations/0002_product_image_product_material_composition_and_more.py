
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='material_composition',
            field=models.TextField(blank=True, help_text='Specific blend details or other material name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Gucci', 'Gucci'), ('Prada', 'Prada'), ('Louis Vuitton', 'Louis Vuitton'), ('Hermès', 'Hermès'), ('Chanel', 'Chanel'), ('Dior', 'Dior'), ('Balenciaga', 'Balenciaga'), ('Saint Laurent', 'Saint Laurent'), ('Burberry', 'Burberry'), ('Fendi', 'Fendi'), ('Versace', 'Versace'), ('Valentino', 'Valentino'), ('Givenchy', 'Givenchy'), ('Bottega Veneta', 'Bottega Veneta'), ('Loewe', 'Loewe'), ('Celine', 'Celine'), ('Alexander McQueen', 'Alexander McQueen'), ('Dolce & Gabbana', 'Dolce & Gabbana'), ('Tom Ford', 'Tom Ford'), ('The Row', 'The Row'), ('Brunello Cucinelli', 'Brunello Cucinelli'), ('Loro Piana', 'Loro Piana'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, choices=[('Cotton', 'Cotton'), ('Silk', 'Silk'), ('Wool', 'Wool'), ('Cashmere', 'Cashmere'), ('Linen', 'Linen'), ('Leather', 'Leather'), ('Denim', 'Denim'), ('Velvet', 'Velvet'), ('Satin', 'Satin'), ('Chiffon', 'Chiffon'), ('Tweed', 'Tweed'), ('Polyester', 'Polyester'), ('Viscose', 'Viscose'), ('Nylon', 'Nylon'), ('Elastane', 'Elastane'), ('Other', 'Other'), ('Blend', 'Blend')], max_length=100),
        ),
    ]

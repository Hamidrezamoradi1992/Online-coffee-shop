

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_merge_20240926_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]

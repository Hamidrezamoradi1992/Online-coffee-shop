

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='order',
            managers=[
                ('completed', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]

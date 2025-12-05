# 0004_delete_tag.py
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_post_tags'),  # replace with your last correct migration
    ]

    operations = [
        # 1️⃣ Remove old M2M field
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        # 2️⃣ Delete old Tag model
        migrations.DeleteModel(
            name='Tag',
        ),
    ]

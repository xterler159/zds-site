# Generated by Django 4.2.16 on 2024-10-20 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tutorialv2", "0041_remove_must_reindex"),
        ("utils", "0027_remove_update_index_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alert",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="alerts_on_this_comment",
                to="utils.comment",
                verbose_name="Commentaire",
            ),
        ),
        migrations.AlterField(
            model_name="alert",
            name="content",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="alerts_on_this_content",
                to="tutorialv2.publishablecontent",
                verbose_name="Contenu",
            ),
        ),
    ]

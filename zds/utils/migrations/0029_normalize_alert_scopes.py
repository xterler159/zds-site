# Generated by Django 4.2.16 on 2024-10-19 22:55

"""
In production, the column `scope` of the table containg the alerts contains
leftovers from older alert management:

SELECT BINARY scope, COUNT(*) AS nb, MIN(pubdate) AS first_pubdate, MAX(pubdate) AS last_pubdate FROM utils_alert WHERE solved=1 GROUP BY BINARY scope;
+--------------+------+---------------------+---------------------+
| BINARY scope | nb   | first_pubdate       | last_pubdate        |
+--------------+------+---------------------+---------------------+
| ARTICLE      |  113 | 2017-05-15 11:03:23 | 2024-09-04 10:09:20 |
| Article      |    5 | 2017-01-24 21:34:56 | 2017-04-20 15:56:43 |
| CONTENT      |  115 | 2017-05-04 12:28:11 | 2024-08-08 08:46:31 |
| FORUM        | 3756 | 2016-12-13 19:03:00 | 2024-09-15 22:37:04 |
| OPINION      |  202 | 2017-05-21 14:28:24 | 2024-09-04 15:20:13 |
| PROFILE      | 1088 | 2019-09-18 22:16:55 | 2024-09-16 17:39:55 |
| TUTORIAL     |  392 | 2017-05-21 21:48:11 | 2024-09-12 20:07:01 |
| Tutoriel     |    7 | 2016-12-21 22:56:29 | 2017-04-26 12:21:32 |
+--------------+------+---------------------+---------------------+

This migration normalizes the scope values of all alerts.
"""

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0028_alert_cascade_delete"),
    ]

    operations = [
        # These WHERE are actually case *in*sensitive, but it will not change
        # the result (just modify more records which don't need it), but
        # having a WHERE which is case-sensitive *and* compatible with both
        # SQLite and MariaDB seems tricky...
        migrations.RunSQL(
            ("UPDATE utils_alert SET scope = 'ARTICLE' WHERE scope = 'Article';"),
        ),
        migrations.RunSQL(
            ("UPDATE utils_alert SET scope = 'TUTORIAL' WHERE scope = 'Tutoriel';"),
        ),
    ]

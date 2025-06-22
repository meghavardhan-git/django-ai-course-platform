import csv
from django.core.management.base import BaseCommand
from recommender.models import Course

class Command(BaseCommand):
    help = 'Import courses from CSV (for production)'

    def handle(self, *args, **kwargs):
        with open('courses.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                Course.objects.get_or_create(
                    title=row['title'],
                    category=row['category'],
                    difficulty=row['difficulty'],
                    description=row['description'],
                    youtube_link=row['youtube_link'],
                    thumbnail_url=row['thumbnail_url']
                )
                count += 1
            self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} courses.'))

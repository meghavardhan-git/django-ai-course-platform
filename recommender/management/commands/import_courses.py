import csv
from django.core.management.base import BaseCommand
from recommender.models import Course

class Command(BaseCommand):
    help = 'Import courses from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0
            for row in reader:
                course, created = Course.objects.get_or_create(
                    title=row['title'],
                    defaults={
                        'category': row['category'],
                        'difficulty': row['difficulty'],
                        'description': row['description'],
                        'youtube_link': row['youtube_link'],
                        'thumbnail_url': row['thumbnail_url'],
                    }
                )
                if created:
                    count += 1

            self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} courses.'))

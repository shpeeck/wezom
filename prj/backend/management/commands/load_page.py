from django.core.management.base import BaseCommand, CommandError
from backend.models import StaticPage
from prj.settings import DATA_DIR

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        StaticPage.objects.all().delete()

        try:
            print('Start json parse about_page')
            with open(DATA_DIR+'/about_page.json', 'r', encoding='utf-8') as f:
                result_data = json.load(f)
                page = StaticPage()
                page.title = result_data['title']
                page.content = result_data['content']
                page.save()
        except:
            print('Impossible parse about_page')

        try:
            print('Start json parse contact_page')
            with open(DATA_DIR+'/contact_page.json', 'r', encoding='utf-8') as f:
                result_data = json.load(f)
                page = StaticPage()
                page.title = result_data['title']
                page.content = result_data['content']
                page.save()
        except:
            print('Impossible parse contact_page')


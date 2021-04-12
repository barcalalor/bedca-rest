from django.core.management.base import BaseCommand

from core.scrapper.BEDCA import BEDCAScrapper


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        bedca = BEDCAScrapper("https://www.bedca.net/bdpub/procquery.php")
        bedca.import_component_groups()

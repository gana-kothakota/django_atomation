from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "greetings"
    def handle(self,*args, **Kwargs):
        self.stdout.write("hello tharun")
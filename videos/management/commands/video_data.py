__author__ = 'james'

from os import listdir
from os.path import isfile, join
from django.core.management.base import BaseCommand
from videos.models import Video


class Command(BaseCommand):
    args = "<Dir> <Dir> ..."
    help = "Pass in the directories with videos that you want to add"

    def handle(self, *args, **kwargs):
        for dir in args:
            for vid in self.get_videos(dir):
                *title, extension = vid.split(".")
                title = ".".join(title)
                self.stdout.write("Title is {}".format(title))
                try:
                    Video.objects.get(title=title)
                    self.stdout.write("exists")
                except Video.DoesNotExist:
                    Video.objects.create(title=title, path=join(dir, vid))
                    self.stdout.write("created")

    @staticmethod
    def get_videos(dir):
        return [vid for vid in listdir(dir) if isfile(join(dir, vid))]

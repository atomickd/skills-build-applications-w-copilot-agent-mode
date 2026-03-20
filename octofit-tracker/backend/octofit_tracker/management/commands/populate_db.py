from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', username='ironman', team=marvel),
            User.objects.create(email='captain@marvel.com', username='captain', team=marvel),
            User.objects.create(email='batman@dc.com', username='batman', team=dc),
            User.objects.create(email='superman@dc.com', username='superman', team=dc),
        ]

        # Create activities
        for user in users:
            Activity.objects.create(user=user, type='run', duration=30)
            Activity.objects.create(user=user, type='cycle', duration=45)

        # Create workouts
        Workout.objects.create(name='Hero Strength', description='Superhero workout')
        Workout.objects.create(name='Speed Training', description='Speed workout')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))

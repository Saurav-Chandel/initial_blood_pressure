# Generated by Django 3.2.13 on 2022-06-25 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessModel',
            fields=[
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('ProfileImage', models.ImageField(blank=True, null=True, upload_to='BusineesProfileImages')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('BusinessImages', models.FileField(blank=True, max_length=500, null=True, upload_to='BusinessImages')),
                ('Location', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.FloatField(blank=True, max_length=500, null=True)),
                ('longitude', models.FloatField(blank=True, max_length=500, null=True)),
                ('Contact', models.BigIntegerField(blank=True, null=True)),
                ('CPFNumber', models.CharField(blank=True, max_length=14, null=True)),
                ('Description', models.CharField(blank=True, max_length=1000, null=True)),
                ('TennisCourts', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomname', models.CharField(max_length=255)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HostMatches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=200, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Time', models.TimeField(blank=True, null=True)),
                ('Location', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('player_counts', models.IntegerField(blank=True, null=True)),
                ('SelectMode', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Private', max_length=200)),
                ('Status', models.CharField(choices=[('Initiated', 'Initiated'), (1, '1'), (2, '2'), (3, '3')], default='Initiated', max_length=200)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('ProfileImage', models.ImageField(blank=True, null=True, upload_to='UserProfileImages')),
                ('FirstName', models.CharField(blank=True, max_length=200, null=True)),
                ('LastName', models.CharField(blank=True, max_length=200, null=True)),
                ('Country', models.CharField(blank=True, max_length=200, null=True)),
                ('City', models.CharField(blank=True, max_length=200, null=True)),
                ('State', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('ZipCode', models.CharField(blank=True, max_length=10, null=True)),
                ('CPFNumber', models.CharField(blank=True, max_length=14, null=True)),
                ('MatchesHosted', models.IntegerField(blank=True, default=0, null=True)),
                ('MatchesWon', models.IntegerField(blank=True, default=0, null=True)),
                ('MatchesPlayed', models.IntegerField(blank=True, default=0, null=True)),
                ('Feedback', models.TextField()),
                ('IsSuspended', models.BooleanField(blank=True, default=False, null=True)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SingleChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomname', models.CharField(max_length=255)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User1InRoom', to='app.profiles')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User2InRoom', to='app.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='Team2Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Result', models.CharField(blank=True, max_length=5, null=True)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('HostMatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hostmatches')),
                ('Player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='Team1Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Result', models.CharField(blank=True, max_length=5, null=True)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('HostMatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hostmatches')),
                ('Player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='SingleRoomMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('messageType', models.CharField(choices=[('text', 'text'), ('media', 'media')], default='text', max_length=255)),
                ('message_read', models.BooleanField(default=False)),
                ('Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SingleRoom', to='app.singlechatroom')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SingleUserMessage', to='app.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='RoomMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Room', to='app.chatroom')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserSendingMessage', to='app.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.FloatField(blank=True, default=0, null=True)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('HostMatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hostmatches')),
                ('PlayerRated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PlayerRated', to='app.profiles')),
                ('PlayerRating', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PlayerRating', to='app.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfRecord', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('SelectMode', models.CharField(blank=True, choices=[('Open', 'Open'), ('Close', 'Close')], default='Open', max_length=200, null=True)),
                ('Day', models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=200, null=True)),
                ('StartTime', models.TimeField(blank=True, null=True)),
                ('CloseTime', models.TimeField(blank=True, null=True)),
                ('Business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.businessmodel')),
                ('Player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(blank=True, max_length=500, null=True)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('HostMatch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='app.hostmatches')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='app.profiles')),
                ('UserSending', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserSending', to='app.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='MatchSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team1', models.IntegerField(blank=True, default=0, null=True)),
                ('Team2', models.IntegerField(blank=True, default=0, null=True)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('HostMatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hostmatches')),
            ],
        ),
        migrations.CreateModel(
            name='MatchRounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team1Score', models.IntegerField(blank=True, default=0, null=True)),
                ('Team2Score', models.IntegerField(blank=True, default=0, null=True)),
                ('Round', models.IntegerField(blank=True, default=0, null=True)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('HostMatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hostmatches')),
            ],
        ),
        migrations.AddField(
            model_name='hostmatches',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profiles'),
        ),
        migrations.CreateModel(
            name='HostInvitations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumberInvited', models.BigIntegerField(blank=True, null=True)),
                ('Status', models.CharField(choices=[('Sent', 'Sent'), ('Attend', 'Attend'), ('Decline', 'Decline')], default='Sent', max_length=200)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('HostMatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hostmatches')),
                ('UserInvited', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[('Sent', 'Sent'), ('Accept', 'Accept'), ('Reject', 'Reject')], default='Sent', max_length=200)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receiver', to='app.profiles')),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sender', to='app.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeviceToken', models.CharField(blank=True, max_length=250, null=True)),
                ('DeviceType', models.CharField(choices=[('iOS', 'iOS'), ('Android', 'Android')], max_length=500)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactFromBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.CharField(blank=True, max_length=200, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.businessmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.CharField(blank=True, max_length=200, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profiles')),
            ],
        ),
        migrations.AddField(
            model_name='chatroom',
            name='Users',
            field=models.ManyToManyField(related_name='UsersInRoom', to='app.Profiles'),
        ),
        migrations.CreateModel(
            name='BusinessWeekHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=200, null=True)),
                ('StartTime', models.TimeField(blank=True, null=True)),
                ('CloseTime', models.TimeField(blank=True, null=True)),
                ('Business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.businessmodel')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service', models.CharField(blank=True, max_length=200, null=True)),
                ('Business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.businessmodel')),
            ],
        ),
    ]

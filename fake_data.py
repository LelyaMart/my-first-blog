import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()


from faker import Faker
from django.contrib.auth.models import User
from blog.models import Post
from faker.providers import lorem
import datetime

fake = Faker('ru_RU')
fake.add_provider(lorem)

for i in range(5):
    profile = fake.simple_profile()
    username = profile['username']
    email = profile['mail']
    password = fake.password()
    user = User.objects.create_user(username, email, password)
    user.save()
    print(username, email, password)


for _ in range(90):
    title = fake.sentence(nb_words=2)
    text = fake.paragraph(nb_sentences=4)
    print(text, title)
    post = Post.objects.create(author=User.objects.get(username='lelyamart'), title=title, text=text, published_date=datetime.datetime.now())
    post.save()

from django.test import TestCase
from main import models
from django.core.files.images import ImageFile
from decimal import Decimal

class TestSignal(TestCase):
    def test_thumbnails_are_generated_on_save(self):
        category = models.BlogPostCategory(name = 'runner')
        category.save()

        tag = models.BlogPostTag(name = 'a')
        tag.save()

        models.User.objects.create_user('sethdad224@gmail.com','thepassword')
        user = models.User.objects.get(email='sethdad224@gmail.com')

        blogpost = models.BlogPost(
            title = 'the runner',
            slug = 'the-runner',
            description = 'the runner',
            category = category,
            content = 'the content',
            user = user
            )

        blogpost.save()

        with open('/home/seth/Pictures/Screenshot from 2022-07-24 14-29-14.png','rb') as rfile:
            image = models.BlogPostImage(blogpost = blogpost, image = ImageFile(rfile, name='tctb.jpg'))
            with self.assertLogs('main', level='INFO') as cm:
                image.save()

        self.assertGreaterEqual(len(cm.output), 1)
        image.refresh_from_db()

        with open('media/upload_thumbnails/tctb.jpg', 'rb') as rfile:
            expected_content = rfile.read()
            assert image.thumbnail.read() == expected_content

        image.thumbnail.delete(save = False)
        image.image.delete(save = False)
        
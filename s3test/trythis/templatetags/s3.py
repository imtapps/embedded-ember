from django import template
from django.conf import settings
import requests
import re

register = template.Library()


@register.simple_tag
def s3(kind):
    url = 'https://{}.s3.amazonaws.com'.format(settings.AWS_BUCKET)
    bucket = requests.get(url)
    pattern = re.compile('assets/[\.\-\w\d]+{}'.format(kind))
    resources = pattern.findall(bucket.text)
    return ''.join(['<script src="{}/{}"></script>'.format(url, r) for r in reversed(resources)])

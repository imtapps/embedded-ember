from django import template
from django.conf import settings
import requests
import re

register = template.Library()


@register.simple_tag
def s3(kind):
    """
        This gets a list of files from a website (specifically an S3 bucket), parses it for the file names,
        and returns the HTML tags for the files to be loaded by the rendered Django page.

        kind is the "kind" or "type" of files you want to inject into the Django template
    """
    url = 'https://{}.s3.amazonaws.com'.format(settings.AWS_BUCKET)
    bucket = requests.get(url)
    pattern = re.compile('assets/[\.\-\w\d]+{}'.format(kind))
    resources = pattern.findall(bucket.text)
    # reversed is optional depending on how one wants the file list rendered
    # this example uses ember so the vendor-* needs to be the first tag
    if kind == 'js':
        scripts = ''.join(['<script src="{}/{}"></script>'.format(url, r) for r in reversed(resources)])
        return '{}{}'.format(scripts, startScript())
    if kind == 'css':
        return ''.join(['<link href="{}/{}" rel="stylesheet"></link>'.format(url, r) for r in reversed(resources)])

def startScript():
    """
        This allows one to control when the Ember application is started
        Script based on Patrick Sexton's at https://varvy.com/pagespeed/defer-loading-javascript.html
    """
    return """
    <script type="text/javascript">
      function startOnload(){
        // EmbeddedEmber is the exported global from the ember application
        window.EmbeddedEmber.start();
      }
      if (window.addEventListener)
        window.addEventListener("load", startOnload, false);
      else if (window.attachEvent)
        window.attachEvent("onload", startOnload);
      else window.onload = startOnload;
    </script>
    """

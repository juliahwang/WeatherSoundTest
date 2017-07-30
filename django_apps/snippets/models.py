from django.contrib.auth import get_user_model
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter

from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

###
# default settings
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

###
# Custom User setting
User = get_user_model()


class Snippet(models.Model):
    owner = models.ForeignKey(User, )
    date_created = models.DateTimeField(auto_now_add=True, )
    title = models.CharField(max_length=100, blank=True, )
    code = models.TextField()
    highlighted = models.TextField()
    linenos = models.BooleanField(default=True)  # False?
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                max_length=100,
                                default="python", )
    style = models.CharField(choices=STYLE_CHOICES,
                             max_length=100,
                             default="friendly", )

    class Meta:
        ordering = (
            "date_created",

        )

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {
            "title": self.title
        } if self.title else {}
        formatter = HtmlFormatter(
            style=self.style,
            linenos=linenos,
            full=True,
            **options,
        )
        self.highlighted = highlight(self.code, lexer, formatter)

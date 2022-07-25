from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.translation import gettext_lazy as _


class PostModel(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('title'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name=_('author'))
    text = models.TextField(verbose_name=_('text'))
    add_date = models.DateField(default=date.today(), verbose_name=_('add date'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class CommentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name=_('author'))
    text = models.TextField(verbose_name=_('text'))
    add_comment_date = models.DateField(default=date.today(), verbose_name=_('add comment date'))
    post = models.ForeignKey(PostModel, null=False, on_delete=models.CASCADE, verbose_name=_('post'))

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

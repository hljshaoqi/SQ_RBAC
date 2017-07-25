from django.db import models

from rbac.models import User as RbacUser


class UserInfo(models.Model):
    nickname = models.CharField(max_length=32, verbose_name="昵称")
    user = models.OneToOneField(RbacUser)

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class Order(models.Model):
    """报障单"""
    title = models.CharField(max_length=32, verbose_name="标题")
    detail = models.TextField(verbose_name="详细")
    create_user = models.ForeignKey(UserInfo, related_name='aaa')
    ctime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    status_choice = (
        (1, '未处理'),
        (2, '处理中'),
        (3, '已处理'),
    )
    status = models.IntegerField(verbose_name="状态", choices=status_choice, default=1)
    processor = models.ForeignKey(UserInfo, related_name='bbb', null=True, blank=True)
    solution = models.TextField(verbose_name="解决方案", null=True, blank=True)
    ptime = models.DateTimeField(verbose_name="处理时间", null=True, blank=True)

    class Meta:
        verbose_name = '报障单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

from django.db import models


class Blog(models.Model):
    title = models.CharField(verbose_name='제목', max_length=200)
    title_description = models.CharField(verbose_name='제목 설명', max_length=200)
    content = models.TextField(verbose_name='내용')
    # main_image = models.ImageField()
    is_published = models.BooleanField(verbose_name='게시 여부', default=False)
    created_at = models.DateTimeField(verbose_name='생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정 일시', auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

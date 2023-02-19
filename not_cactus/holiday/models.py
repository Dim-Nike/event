from django.db import models

# Create your models here.


class CategoriesHoliday(models.Model):
    class Meta:
        verbose_name = 'Категории праздника'
        verbose_name_plural = 'Категории праздников'

    name = models.CharField(verbose_name='Наименование', max_length=155)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/CategoriesHolidays/%Y/%m/%d/')
    gender = models.BooleanField(verbose_name='Мужской(галочка есть)/Женский(галочки нет)')

    def __str__(self):
        return self.name


class Event(models.Model):
    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    name = models.CharField(verbose_name='Наименование', max_length=155)
    categories = models.ForeignKey(CategoriesHoliday, verbose_name='Категория праздника', on_delete=models.PROTECT)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/EventHolidays/%Y/%m/%d/')
    description = models.TextField(verbose_name='Краткое описание(не более 300 символов)', max_length=300)
    full_text = models.TextField(verbose_name='Подробное описание')
    data_start = models.DateTimeField(verbose_name='Дата начала')
    data_end = models.DateTimeField(verbose_name='Дата окончания')
    old_price = models.IntegerField(verbose_name='Старая цена', default=0)
    price = models.IntegerField(verbose_name='Цена')
    is_active = models.BooleanField(verbose_name='Опубликовано')
    popular = models.BooleanField(verbose_name='Отображение на главной странице(должно быть кратным 4)')
    event_of_the_week = models.BooleanField(verbose_name='Праздник недели(Может быть один)')



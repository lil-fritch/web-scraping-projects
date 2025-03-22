from load_django import *
from parser_app.models import *

from django.db.models import Count

items = Link.objects.filter(status='Done').order_by('-id')
count = 0
for item in items:
    if count == 5: break
    item.status = 'New'
    item.save()
    count+=1
# def remove_duplicates():
#     # Групуємо записи по полю link та обчислюємо їх кількість
#     duplicates = (
#         Keyword.objects
#         .values('link')
#         .annotate(link_count=Count('id'))
#         .filter(link_count__gt=1)
#     )

#     for duplicate in duplicates:
#         # Отримуємо всі записи з однаковим link
#         records = Keyword.objects.filter(link=duplicate['link'])
#         # Залишаємо один запис, інші видаляємо
#         records.exclude(id=records.first().id).delete()

#     print("Дублікати успішно видалені!")

# # Викликаємо функцію
# remove_duplicates()


    
from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Author, blog, Enrty
from django.db.models import Q

def home(requst):
    # *-----------------> all()
    # ! To get all data
    # data = blog.objects.all()
    # for val in data:
    #     print(val.name, val.tagline)
    # print(type(data))
    
    # * ----------------> get()
    # !To get the a specific blog details
    # data1 = blog.objects.get(id=3)
    
    # ? or
    
    # data1 = blog.objects.get(name="Gadgets")    
    # print(data1.id, data1.name, data1.tagline)
    
    # !To get the data of blog table from Entry table Forign key 
    # entry_data = Enrty.objects.get(blog=data1.id)
    # print(entry_data.headline, entry_data)
    
    # print(entry_data.blog.name, entry_data.blog.tagline, entry_data.body_text)
    
    # !To get all the fields of Entry table from blog table isntance
    # data1 = blog.objects.get(id=1)
    # entry_data = data1.blog_data.all()
    # for val in entry_data:
    #     print(val.headline, val.pub_date)
        
        # ? or
    # name = iter(entry_data)
    # print(next(name))
    
    # * -----------> Filter
    # ! To get the list of objects of entry table from blog table
    # blog_details = blog.objects.get(name="Gadgets")
    # # # print(blog_data.id)
    
    # data = blog_details.blog_data.filter(blog=blog_details.id)
    # for val in data:
    #     print(val.pub_date)
    
    # iteration = iter(data)
    # print(next(iteration).pub_date)
    # print(next(iteration).body_text)
    # print(next(iteration).authors)
    # print(next(iteration).rating)
    
    # ! To use or in django query
    # SELECT * FROM product WHERE (name='phone' AND price > 500) OR (name='tablet' AND price < 400);

    # ent = Enrty.objects.filter(Q(headline="Now a days gadjets") | Q(headline="Good place for natur"))
    # print(ent)
    
    # ? or
    
    # import operator
    # from functools import reduce
    # qlist = [Q(headline='Now a days gadjets'), Q(rating=2)]
    # ent=Enrty.objects.filter(reduce(operator.and_, qlist))
    # print(ent)
    
    # * ----------------> exclude()
    # ent = Enrty.objects.exclude(pub_date="2023-08-15")
    # print(ent)
    
    # * ----------------> value_list()
    # ent = Enrty.objects.values_list("headline", "pub_date", "body_text", named=True)
    # for val in ent:
    #     print(val)
    
    #* --------------->  order_by()
    # ent = Enrty.objects.all().order_by("-pub_date")
    # print(ent)
    
    # * --------------> aggregate()
    # https://www.youtube.com/watch?v=srs1jz0i73o
    # from django.db.models import Avg, Sum, Count
    # from django.db.models import Max, Min
    # ent = Enrty.objects.aggregate(Sum("rating"))
    # print(ent)
    
    # * --------------> reverse()
    # ent = Enrty.objects.reverse()
    # print(ent)
    
    # * -------------> distinct()
    # ent = Enrty.objects.filter(headline="Now a days gadjets").values('pub_date', "id").distinct()
    # print(ent)
    
    # * ------------> dates()
    # ent = Enrty.objects.dates("pub_date", "year")
    # ent = Enrty.objects.dates("pub_date", "month") # week, day
    # print(ent)
    
    # * ---------------> union()
    # blg = blog.objects.all().values_list("name").union(Author.objects.all().values("name"))
    # print(blg)    
    # print(blg.query)
    
    # * --------------> select_related()
    # ent = Enrty.objects.get(id=3)
    # print(ent.blog)
    # ? or
    
    # e = Enrty.objects.select_related("blog").get(id=5)
    # print(e.blog)
    
    # * -------------------------->
    # ! To get the entry table objecst from author table
    ent = Enrty.objects.get(id=2).author.all()
    print(ent.name)

    # * ---------------------------->
    # ent = Enrty.objects.select_related("authors").get(id=2)
    # print(ent.authors)
    
    return HttpResponse("<h2>Hey there</h2>")
from django.db import models


# Create your models here.
class CommonCustInfo(models.Model):
    customer_no = models.TextField(primary_key=True)
    first_name_kanji = models.TextField(blank=True, null=True)
    last_name_kanji = models.TextField(blank=True, null=True)
    first_name_kana = models.TextField(blank=True, null=True)
    last_name_kana = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    dob = models.DateField(blank=True, null=True)
    phone_area_code = models.TextField(blank=True, null=True)
    phone_local_area_code = models.TextField(blank=True, null=True)
    phone_no = models.TextField(blank=True, null=True)
    cellphone_no1 = models.TextField(blank=True, null=True)
    cellphone_no2 = models.TextField(blank=True, null=True)
    cellphone_no3 = models.TextField(blank=True, null=True)
    email_pc = models.TextField(blank=True, null=True)
    email_opt_flag = models.TextField(blank=True, null=True)
    created_by = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.TextField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    del_flg = models.TextField(blank=True, null=True)









# class Customer(models.Model):
#     phone1 = models.CharField(null=True,blank=False, unique = False, max_length=12)
#     phone2 = models.CharField(null=True,blank=False, unique = False, max_length=12)
#     phone3 = models.CharField(null=True,blank=False, unique = True, max_length=12)
#     cell1 = models.CharField(null=True,blank=False, unique = True, max_length=12)
#     cell2 = models.CharField(null=True,blank=False, unique = True, max_length=12)
#     cell3 = models.CharField(null=True,blank=False, unique = True, max_length=12)
#     kanjiname=models.CharField(max_length=50, null=True, default=None)
#     kanjilastname=models.CharField(max_length=50, null=True, default=None)
#     kananame=models.CharField(max_length=50, null=True, default=None)
#     kanalastname=models.CharField(max_length=50, null=False, default=None)
#     dob = models.DateField(null=True, default=None)
#     gender=models.CharField(max_length=50, null=True, default=None)
#     add1=models.CharField(null=True,blank=False, unique = False, max_length=50)
#     add2=models.CharField(null=True,blank=False, unique = False, max_length=50)
#     add3=models.CharField(max_length=100, default=None, null=True)
#     email=models.EmailField(null=True,blank=False, unique = True)
    


#     def __str__(self):
#         return self.kanalastname






    # phone1 = models.CharField(null=True,blank=False, unique = True, max_length=12)
    # phone2 = models.CharField(null=True,blank=False, unique = True, max_length=12)
    # country_code = models.CharField(null=True,blank=False, unique = True, max_length=4)
    # kanjiname=models.CharField(max_length=10, null=True, default=None)
    # kanjilastname=models.CharField(max_length=10, null=True, default=None)
    # kananame=models.CharField(max_length=10, null=True, default=None)
    # kanalastname=models.CharField(max_length=10, null=True, default=None)
    # date_of_birth = models.DateField(null=True, default=None)
    # gender=models.CharField(max_length=50, null=True, default=None)
    # Zipcode=models.IntegerField(null=True,blank=False, unique = False)
    # add1=models.CharField(null=True,blank=False, unique = False, max_length=50)
    # add2=models.IntegerField(null=True,blank=False, unique = True)
    # add3=models.CharField(max_length=100, default=None, null=True)
    # email=models.EmailField(null=True,blank=False, unique = False)
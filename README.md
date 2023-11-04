# Django-ModelTranslation
- **Notion sahifa: https://soapy-fisherman-347.notion.site/Django-Multi-Language-f489e64601c049ebb83cc47908831a45?pvs=4**
- **Model Translation**
    - **Bu safar siz bilan Django-Modellarimizdagi ma’lumotlarni ko’p tilli qilishni, ya’ni databazamizda saqlanadigan ma’lumotlarni boshqa tillarga o’tkazishni o’rganamiz!**
    
    ---
    
    - **Django loyihangizni yaratib olgan bo’lsangiz - Loyihamizning virtual muhitiga kiramiz (#Terminal): Va `django-modeltranslation` paketini o’rnatamiz:**
        
        ```python
        pip install django-modeltranslation
        ```
        
        - `'modeltranslation'` paketini settings.py faylimizdagi `INSTALLED_APPS`ga qo’shamiz:
        
        ```python
        INSTALLED_APPS = [
            'modeltranslation',  # yangi
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]
        ```
        
        - DIQQAT QILING !!! - INSTALLED_APPS ga qo’shgan ‘modeltranslation’ paketimizni 'django.contrib.admin'dan yuqorida yozishimiz kerak, aks holda xatolik paydo bo’ladi !!!
        
        ---
        
    - **Endi biz settings.py faylimizga ba'zi sozlamalarni o'rnatishimiz kerak:**
        
        ```python
        LANGUAGE_CODE = 'uz-uz'
        USE_TZ = True
        USE_L10N = True
        USE_I18N = True
        TIME_ZONE = 'UTC' **# mintaqani o'zgartirishimiz mumkin. 
        # O'zbekiston uchun mintaqalar: 'Etc/GMT-5', 'Asia/Tashkent', 'Asia/Samarkand'**
        ```
        
        - **bu yerdagi LANGUAGE_CODE loyihamizning asosiy tili hisoblanadi!**
    - **Shuningdek, web-saytimizda bo’lishi kerak bo’lgan boshqa tillarni ham settings.py fayliga qo’shamiz:**
        
        ```python
        LANGUAGES = (
            ('en', 'English'),
            ('uz', 'Uzbek'),
        		(...), # yana tillar qo'shishingiz mumkin!
        )
        ```
        
        - **Bu yerda men o’zbek hamda ingliz tillaridagi misolni ko’rsatdim!**
    - **settings.py faylimizdagi `MIDDLEWARE` tarkibiga yangi middleware kiritamiz:**
        
        ```python
        'django.middleware.locale.LocaleMiddleware'
        ```
        
        - **Quyidagi ko’rinishda qo’shish bizni xatolikka olib kelmaydi:**
        
        ```python
        MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.locale.LocaleMiddleware', # Yangi
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]
        ```
        
    - **Endi, tarjimalarimiz saqlanadigan papka manzilni settings.py fayliga saqlaymiz:**
        
        ```python
        **LOCALE_PATHS = [
            BASE_DIR / 'locale/',
        ]**
        ```
        
        - **Bu papka quyidagi ko’rinishda shakllanadi, bu papka ichida har bir til uchun yana alohida papkalar ajratiladi:**
        
        ```bash
        **locale
        ├── en
        ├── uz
        └── ..**
        ```
        
    - **Endi asosiy loyiha faylimizdagi urls.py faylini yangilaymiz:**
        
        ```python
        **from django.contrib import admin
        from django.urls import path
        from django.conf.urls.i18n import i18n_patterns
        
        urlpatterns = [
            path('admin/', admin.site.urls),
        ]
        
        urlpatterns = [
            *i18n_patterns(*urlpatterns, prefix_default_language=False),
            ]**
        ```
        
    - settings.py faylida modellar tarjimasini standard tilini belgilashimiz kerak:
        
        ```python
        **MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'**
        ```
        
    - **Endi model tajimalari qaysi tillarni qo'llab-quvvatlashini belgilaylik. Boshqacha qilib aytadigan bo'lsak, sizning saytingiz 5 xil tilni qo'llab-quvvatlashi mumkin, ammo agar siz model tarjima operatsiyalarida faqat 2 xil tilni qo'llab-quvvatlashini istasangiz, faqat ikki 2 xil tilni belgilashingiz mumkin bo’ladi:**
        
        ```python
        MODELTRANSLATION_LANGUAGES = ('uz', 'en')
        ```
        
    - Keling endi sinov operatsiyalari uchun Product nomli model yaratamiz:
        
        ```python
        from django.db import models
        
        class Product(models.Model):
            title = models.CharField(verbose_name="Title", max_length=50)
            description = models.TextField(verbose_name="Description", max_length=999)
            price = models.PositiveIntegerField()
            image = models.ImageField()
        ```
        
    - **Endi biz namunaviy tarjima operatsiyalari uchun har bir APP da translation.py nomli fayllarni yaratishimiz kerak. Misol uchun menda ‘mainApp’ nomli APP bor va shu papka ichida men yaratgan translation.py faylini ko’rishingiz mumkin:**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3ccbde89-5c0f-419d-a694-16f67ff39239/Untitled.png)
        
    - **[translation.py](http://translation.py):**
        
        ```python
        from .models import Product
        from modeltranslation.translator import TranslationOptions, register
        
        @register(Product)
        class ProductTranslationOptions(TranslationOptions):
            fields = ('title', 'description')
        ```
        
        - Huddi admin panelga register qilganimiz kabi bu yerda ham register qilamiz. Biz o’rnatgan modeltranslation paketidan TranslationOptions dan meros olib class yaratishimiz kerak bo’ladi. Va biz fields qismiga modelimizning tarjima qilinishi kerak bo’lgan ustun(maydon)larini belgilaymiz. Chunki hamma ustunlarni ham tarjima qila olmaymiz, masalan bizdagi price(Integer) hamda image(File) ustunlarini tarjima qila olmaymiz.
        - Endi migratsiyalarni yangilaymiz: (#makemigrations&migrate)
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1583c651-4139-4b4b-875a-9628bf74ad6b/Untitled.png)
        
        - Ko’rib turganingizdek har bir til uchun _en va _uz qo’shilgan holda yangi ustunlar yaratildi.
    - Agarda biz hozir Product modelimizni admin.site.register(Product) ko’rinishda serverni ishga tushursak, biroz mantiqsizlik kelib chiqadi:
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ae18b0da-98f4-40c6-bb04-790aa8fa2fa7/Untitled.png)
        
        - Ya’ni bu yerda e’tibor bering Title nomli maydon bu yerda ortiqcha, chunki bizga Title[uz] hamda Title[en] maydonlari yetarli! Shuningdek Description qismida ham shu holat.
    - Bu holatni to’g’irlashimiz uchun admin.py faylidagi registerni quyidagi ko’rinishda qilishim kerak bo’ladi:
        
        ```python
        from django.contrib import admin
        from .models import Product
        from modeltranslation.admin import TranslationAdmin
        
        @admin.register(Product)
        class ProductAdmin(TranslationAdmin):
            list_display = ("title",)
        ```
        
        - Endi natijani ko’rsak:
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e282ab1-f6a1-4c7e-a8ab-7f7c7d6ff45e/Untitled.png)
        
        - Ko’rib turganingizdek endi biz modelimizdagi ma’lumotlarni har bir til uchun alohida saqlay olamiz!
    - Agarda Admin panelni yanada sifatliroq bo’lishini istasangiz - admin.py quyidagicha qo’shimcha qo’shing:
        
        ```python
        from django.contrib import admin
        from .models import Product
        from modeltranslation.admin import TranslationAdmin
        
        @admin.register(Product)
        class ProductAdmin(TranslationAdmin):
            list_display = ("title",)
            class Media:
                js = (
                    'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                    'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
                    'modeltranslation/js/tabbed_translation_fields.js',
                )
                css = {
                    'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
                }
        ```
        
        - Admin panelni tekshiramiz:
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd03bec8-e34f-42bd-a060-ee5aaf8ae806/Untitled.png)
        
        - Mana endi yaxshiroq ko’rinish bor, yana xohishingizga qarab CSS, hamda JS orqali Admin Panelni bezashingiz mumkin.

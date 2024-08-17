# Telegram Bot Aiogram 3.x versiyasi uchun shablon

<img src="aiogram-image.png">

+ Shablon aiogram `2.x` verisyasidan `3.x` versiyasi uchun o'zgartirildi
+ Qo'shimchalar qo'shildi va keraksiz qismlar olib tashlandi
+ Eski shablon [anvarnarz](https://github.com/anvarnarz/mukammal-bot-paid) dan olindi
+ `3.x` versiyasidan boshlab endilikda `Router` orqali ishlash kerak alohida fayllardagi handlerda

Shablonni quyidagi git buryug'i orqali yuklab olishingiz mumkin:
 
     
    git clone https://github.com/uzbek-coder-2022/telegram-bot-template-aiogram-verison-3.git


Shablonni o'zingizga yuklab olgandan so'ng `aiogram` va `environs` kutubxonalarini o'rnating quyidagi buyruqlar orqali: 

    pip install aiogram
    pip install environs

Yoki boshqa usul `requirements.txt` orqali bu ishni bajarishingiz ham mumkin:

    pip install -r requirements.txt
    
Botni linux serverda ishlatishda `deploy.sh` faylidan foydalaning. Buning uchun quyidagi buyruqni terminalda ishga tushiring.
    
    cd /home/user/aiogram-bot  # bot joylashgan yerga o'tish
    ./deploy.sh  # faylni ishga tushirish

Qo'shimcha o'zgartirishlar asta-sekin yana amalga oshirib boriladi.

©️ Khusanboy Sobirjonov

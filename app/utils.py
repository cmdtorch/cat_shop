import datetime
import random

from . import db
from .model import Cat


def create_cats():
    for cat in cats:
        db.session.add(Cat(
            name=cat['name'],
            dob=random_date(datetime.datetime(2016, 1, 1), datetime.datetime(2023, 1, 1)),
            breed=cat['breed'],
            image_url=cat['image'],
            description='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        ))
    db.session.commit()


def random_date(start, end):
  return start + datetime.timedelta(
      seconds=random.randint(0, int((end - start).total_seconds())))


cats = [
    {
        'name': 'Мурзик',
        'breed': 'scottish_lop_eared',
        'image': 'https://i.ytimg.com/vi/YCaGYUIfdy4/maxresdefault.jpg',
    },
    {
        'name': 'Коко',
        'breed': 'maine_coon',
        'image': 'https://www.dailypaws.com/thmb/lzPCSAPujJm8siLc44a-cKWWztw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/maine-coon-headshot-n7o3IIL5qR8-unsplash-2000-da6634149f8e421c8ec0e8dbc8ed8c22.jpg',
    },
    {
        'name': 'Гизмо',
        'breed': 'maine_coon',
        'image': 'https://img1.wsimg.com/isteam/ip/76e92934-d3e7-4d26-aad9-d3afb8604593/D48643B3-A0FF-49BA-9027-D12E013BB57C.jpeg',
    },
    {
        'name': 'Барсик',
        'breed': 'maine_coon',
        'image': 'https://www.thesprucepets.com/thmb/MzKr6fC-v8W4D4oz2p9wWCwAFms=/2119x0/filters:no_upscale():strip_icc()/GettyImages-1189893683-e0ff70596b3b4f0687ba573e5a671f74.jpg',
    },
    {
        'name': 'Вася',
        'breed': 'british_shorthair',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Britishblue.jpg/640px-Britishblue.jpg',
    },
    {
        'name': 'Том',
        'breed': 'ragdoll',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/6/64/Ragdoll_from_Gatil_Ragbelas.jpg',
    },
    {
        'name': 'Бельчонок',
        'breed': 'ragdoll',
        'image': 'https://images.squarespace-cdn.com/content/v1/64af3979a0418f35c5135941/63837712-50ed-4ecf-bd65-ef67b2b3c603/Snapchat-1409770459.jpg',
    },
    {
        'name': 'Киса',
        'breed': 'ragdoll',
        'image': 'https://catinaflat.blog/wp-content/uploads/2022/07/rag_doll_cat-1024x699.jpg',
    },
    {
        'name': 'Лео',
        'breed': 'american_shorthair',
        'image': 'https://www.thesprucepets.com/thmb/8o5e2mkJcAr4kODvsllTf2xiioo=/4778x0/filters:no_upscale():strip_icc()/GettyImages-925319984-36b97d913d934d229d8b0d528a7da64e.jpg',
    },
    {
        'name': 'Черныш',
        'breed': 'bombay',
        'image': 'https://basepaws.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Feyuked2kaujk%2F5qno57tnwsOPjZhsqtOudt%2F4682abd4b7603240e87890631ce3fc0a%2Fjames-park-LsQGIcRVUYc-unsplash.jpg&w=3840&q=75',
    },
    {
        'name': 'Арчи',
        'breed': 'siberian',
        'image': 'https://www.catbreedslist.com/uploads/cat-pictures/siberian-1.jpg',
    },
    {
        'name': 'Степан',
        'breed': 'siberian',
        'image': 'https://wirralwhiskers.co.uk/images/b5qVAGs8p2kKPlMbCXoIMKh3fDE=/100/min-1200x630/bellaface.jpg',
    },
    {
        'name': 'Джипик',
        'breed': 'siberian',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/3/34/3-month-old_female_Siberian_kitten.jpg',
    },
    {
        'name': 'Феликс',
        'breed': 'siberian',
        'image': 'https://siberiancatz.com/wp-content/uploads/2018/07/Siberian-Kitten.jpg',
    },
    {
        'name': 'Коко',
        'breed': 'bengal',
        'image': 'https://i0.wp.com/thediscerningcat.com/wp-content/uploads/2023/09/silver-bengal-cat.jpg',
    },
    {
        'name': 'Мия',
        'breed': 'scottish_lop_eared',
        'image': 'https://i.pinimg.com/originals/a2/9b/0f/a29b0f538ffa6bed3a35eec89cd7f04e.jpg',
    },
    {
        'name': 'Оливер',
        'breed': 'scottish_lop_eared',
        'image': 'https://images.ctfassets.net/440y9b545yd9/3mXEPSN2Ap12wAnFz8dVm2/8b34d9e82f41b11fcee66cc1fc741724/Scottish_fold_5_things_hero850.jpg',
    },
    {
        'name': 'Лука',
        'breed': 'scottish_lop_eared',
        'image': 'https://brit-petfood.com/file/nodes/product/Skotsk%E2%80%A0%20klapouch%E2%80%A0.JPG',
    },
    {
        'name': 'Бусинка',
        'breed': 'siamese',
        'image': 'https://rostovvet.ru/uploads/2015/01/Siamese.jpg',
    },
    {
        'name': 'Симба',
        'breed': 'siamese',
        'image': 'https://www.bethowen.ru/upload/iblock/cea/cea26b7dc742759e7d7121c074e30da6.jpg',
    },
    {
        'name': 'Джек',
        'breed': 'siamese',
        'image': 'https://www.meowingtons.com/cdn/shop/articles/Screen_Shot_2021-01-06_at_3.43.10_PM.png?v=1609965795',
    },
    {
        'name': 'Грета',
        'breed': 'siamese',
        'image': 'https://rostovvet.ru/uploads/2015/01/Siamese-3.jpg',
    },
]

from app.models import db, BusinessImage, environment, SCHEMA
import datetime
from sqlalchemy.sql import text

def seed_businesses_images():
    one_image = BusinessImage(business_id=1, user_id=1, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=True),
    # two_image = BusinessImage(business_id=2, user_id=2, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=False),
    # three_image = BusinessImage(business_id=3, user_id=3, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=False),
    # four_image = BusinessImage(business_id=4, user_id=4, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=False),
    # five_image = BusinessImage(business_id=5, user_id=5, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=False),
    # six_image = BusinessImage(business_id=6, user_id=6, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=False),
    # seven_image = BusinessImage(business_id=7, user_id=7, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=True),
    # eight_image = BusinessImage(business_id=8, user_id=8, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=False),
    # nine_image = BusinessImage(business_id=9, user_id=9, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=False),
    # ten_image = BusinessImage(business_id=10, user_id=10, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=False),
    # eleven_image = BusinessImage(business_id=11, user_id=11, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=False),
    # twelve_image = BusinessImage(business_id=12, user_id=12, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=False),
    # thirteen_image = BusinessImage(business_id=13, user_id=13, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=False),
    # fourteen_image = BusinessImage(business_id=14, user_id=14, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=True),
    # fifteen_image = BusinessImage(business_id=15, user_id=15, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=False),
    # sixteen_image = BusinessImage(business_id=16, user_id=16, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=False),
    # seventeen_image = BusinessImage(business_id=17, user_id=17, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=False),
    # eighteen_image = BusinessImage(business_id=18, user_id=18, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=False),
    # nineteen_image = BusinessImage(business_id=19, user_id=19, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=False),
    # twenty_image = BusinessImage(business_id=20, user_id=20, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=True),
    # twentyone_image = BusinessImage(business_id=21, user_id=21, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=False),
    # twentytwo_image = BusinessImage(business_id=22, user_id=22, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=False),
    # twentythree_image = BusinessImage(business_id=23, user_id=23, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=False),
    # twentyfour_image = BusinessImage(business_id=24, user_id=24, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=False),
    # twentyfive_image = BusinessImage(business_id=25, user_id=25, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=False),
    # twentysix_image = BusinessImage(business_id=26, user_id=26, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=False),
    # twentyseven_image = BusinessImage(business_id=27, user_id=27, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=True),
    # twentyeight_image = BusinessImage(business_id=28, user_id=28, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=False),
    # twentynine_image = BusinessImage(business_id=29, user_id=29, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=False),
    # thirty_image = BusinessImage(business_id=30, user_id=30, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=False),
    # thirtyone_image = BusinessImage(business_id=31, user_id=31, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=False),
    # thirtytwo_image = BusinessImage(business_id=32, user_id=32, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=False),

    # db.session.add_all([one_image, two_image, three_image, four_image, five_image, six_image,
    #                     seven_image, eight_image, nine_image, ten_image, eleven_image, twelve_image, thirteen_image, fourteen_image, fifteen_image, sixteen_image,
    #                     seventeen_image, eighteen_image, nineteen_image, twenty_image, twentyone_image, twentytwo_image, twentythree_image, twentyfour_image, twentyfive_image, twentysix_image,
    #                     twentyseven_image, twentyeight_image, twentynine_image, thirty_image, thirtyone_image, thirtytwo_image])
    db.session.add(one_image)
    db.session.commit()

def undo_businesses_images():
    if environment == "production":
       db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
       db.session.execute(text("DELETE FROM users"))

    db.session.commit()

from app.models import db, BusinessImage, environment, SCHEMA
import datetime
from sqlalchemy.sql import text

def seed_businesses_images():
    italian_one_previmage = BusinessImage(business_id=1, user_id=1, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=True)
    italian_two_previmage = BusinessImage(business_id=2, user_id=2, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=True)
    italian_three_previmage = BusinessImage(business_id=3, user_id=3, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=True)
    italian_four_previmage = BusinessImage(business_id=4, user_id=4, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=True)
    italian_five_previmage = BusinessImage(business_id=5, user_id=5, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=True)
    italian_six_previmage = BusinessImage(business_id=6, user_id=6, image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg", image_preview=True)
    mexican_one_previmage = BusinessImage(business_id=7, user_id=1, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=True)
    mexican_two_previmage = BusinessImage(business_id=8, user_id=2, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=True)
    mexican_three_previmage = BusinessImage(business_id=9, user_id=3, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=True)
    mexican_four_previmage = BusinessImage(business_id=10, user_id=4, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=True)
    mexican_five_previmage = BusinessImage(business_id=11, user_id=5, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=True)
    mexican_six_previmage = BusinessImage(business_id=12, user_id=6, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=True)
    mexican_seven_previmage = BusinessImage(business_id=13, user_id=7, image_url="https://media.timeout.com/images/100292153/750/562/image.jpg", image_preview=True)
    middleast_one_previmage = BusinessImage(business_id=14, user_id=1, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=True)
    middleast_two_previmage = BusinessImage(business_id=15, user_id=2, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=True)
    middleast_three_previmage = BusinessImage(business_id=16, user_id=3, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=True)
    middleast_four_previmage = BusinessImage(business_id=17, user_id=4, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=True)
    middleast_five_previmage = BusinessImage(business_id=18, user_id=5, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=True)
    middleast_six_previmage = BusinessImage(business_id=19, user_id=6, image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg", image_preview=True)
    jap_one_previmage = BusinessImage(business_id=20, user_id=1, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=True)
    jap_two_previmage = BusinessImage(business_id=21, user_id=2, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=True)
    jap_three_previmage = BusinessImage(business_id=22, user_id=3, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=True)
    jap_four_previmage = BusinessImage(business_id=23, user_id=4, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=True)
    jap_five_previmage = BusinessImage(business_id=24, user_id=5, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=True)
    jap_six_previmage = BusinessImage(business_id=25, user_id=6, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=True)
    jap_seven_previmage = BusinessImage(business_id=26, user_id=7, image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg", image_preview=True)
    american_one_previmage = BusinessImage(business_id=27, user_id=1, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=True)
    american_two_previmage = BusinessImage(business_id=28, user_id=2, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=True)
    american_three_previmage = BusinessImage(business_id=29, user_id=3, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=True)
    american_four_previmage = BusinessImage(business_id=30, user_id=4, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=True)
    american_five_previmage = BusinessImage(business_id=31, user_id=5, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=True)
    american_six_previmage = BusinessImage(business_id=32, user_id=6, image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca.jpg", image_preview=True)
    italian_one_image = BusinessImage(business_id=1, user_id=2, image_url="https://images.unsplash.com/photo-1556761223-4c4282c73f77?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3330&q=80", image_preview=False)
    italian_two_image = BusinessImage(business_id=2, user_id=3, image_url="https://images.unsplash.com/photo-1556761223-4c4282c73f77?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3330&q=80", image_preview=False)
    italian_three_image = BusinessImage(business_id=3, user_id=4, image_url="https://images.unsplash.com/photo-1556761223-4c4282c73f77?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3330&q=80", image_preview=False)
    italian_four_image = BusinessImage(business_id=4, user_id=5, image_url="https://images.unsplash.com/photo-1556761223-4c4282c73f77?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3330&q=80", image_preview=False)
    italian_five_image = BusinessImage(business_id=5, user_id=6, image_url="https://images.unsplash.com/photo-1556761223-4c4282c73f77?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3330&q=80", image_preview=False)
    italian_six_image = BusinessImage(business_id=6, user_id=1, image_url="https://images.unsplash.com/photo-1556761223-4c4282c73f77?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3330&q=80", image_preview=False)
    mexican_one_image = BusinessImage(business_id=7, user_id=2, image_url="https://dailytaco.com/wp-content/uploads/2021/11/Home-Tacos.jpg", image_preview=False)
    mexican_two_image = BusinessImage(business_id=8, user_id=3, image_url="https://dailytaco.com/wp-content/uploads/2021/11/Home-Tacos.jpg", image_preview=False)
    mexican_three_image = BusinessImage(business_id=9, user_id=4, image_url="https://dailytaco.com/wp-content/uploads/2021/11/Home-Tacos.jpg", image_preview=False)
    mexican_four_image = BusinessImage(business_id=10, user_id=5, image_url="https://dailytaco.com/wp-content/uploads/2021/11/Home-Tacos.jpg", image_preview=False)
    mexican_five_image = BusinessImage(business_id=11, user_id=6, image_url="https://dailytaco.com/wp-content/uploads/2021/11/Home-Tacos.jpg", image_preview=False)
    mexican_six_image = BusinessImage(business_id=12, user_id=7, image_url="https://dailytaco.com/wp-content/uploads/2021/11/Home-Tacos.jpg", image_preview=False)
    mexican_seven_image = BusinessImage(business_id=13, user_id=1, image_url="https://dailytaco.com/wp-content/uploads/2021/11/Home-Tacos.jpg", image_preview=False)
    middleast_one_image = BusinessImage(business_id=14, user_id=2, image_url="https://st2.depositphotos.com/1027198/46624/i/450/depositphotos_466241258-stock-photo-lebanese-food-selection-top-view.jpg", image_preview=False)
    middleast_two_image = BusinessImage(business_id=15, user_id=3, image_url="https://st2.depositphotos.com/1027198/46624/i/450/depositphotos_466241258-stock-photo-lebanese-food-selection-top-view.jpg", image_preview=False)
    middleast_three_image = BusinessImage(business_id=16, user_id=4, image_url="https://st2.depositphotos.com/1027198/46624/i/450/depositphotos_466241258-stock-photo-lebanese-food-selection-top-view.jpg", image_preview=False)
    middleast_four_image = BusinessImage(business_id=17, user_id=5, image_url="https://st2.depositphotos.com/1027198/46624/i/450/depositphotos_466241258-stock-photo-lebanese-food-selection-top-view.jpg", image_preview=False)
    middleast_five_image = BusinessImage(business_id=18, user_id=6, image_url="https://st2.depositphotos.com/1027198/46624/i/450/depositphotos_466241258-stock-photo-lebanese-food-selection-top-view.jpg", image_preview=False)
    middleast_six_image = BusinessImage(business_id=19, user_id=1, image_url="https://st2.depositphotos.com/1027198/46624/i/450/depositphotos_466241258-stock-photo-lebanese-food-selection-top-view.jpg", image_preview=False)
    jap_one_image = BusinessImage(business_id=20, user_id=2, image_url="https://thumbs.dreamstime.com/b/takoyaki-octopus-balls-japanese-food-22624501.jpg", image_preview=False)
    jap_two_image = BusinessImage(business_id=21, user_id=3, image_url="https://thumbs.dreamstime.com/b/takoyaki-octopus-balls-japanese-food-22624501.jpg", image_preview=False)
    jap_three_image = BusinessImage(business_id=22, user_id=4, image_url="https://thumbs.dreamstime.com/b/takoyaki-octopus-balls-japanese-food-22624501.jpg", image_preview=False)
    jap_four_image = BusinessImage(business_id=23, user_id=5, image_url="https://thumbs.dreamstime.com/b/takoyaki-octopus-balls-japanese-food-22624501.jpg", image_preview=False)
    jap_five_image = BusinessImage(business_id=24, user_id=6, image_url="https://thumbs.dreamstime.com/b/takoyaki-octopus-balls-japanese-food-22624501.jpg", image_preview=False)
    jap_six_image = BusinessImage(business_id=25, user_id=7, image_url="https://thumbs.dreamstime.com/b/takoyaki-octopus-balls-japanese-food-22624501.jpg", image_preview=False)
    jap_seven_image = BusinessImage(business_id=26, user_id=1, image_url="https://thumbs.dreamstime.com/b/takoyaki-octopus-balls-japanese-food-22624501.jpg", image_preview=False)
    american_one_image = BusinessImage(business_id=27, user_id=2, image_url="https://www.corriecooks.com/wp-content/uploads/2023/05/american-food-2.jpg", image_preview=False)
    american_two_image = BusinessImage(business_id=28, user_id=3, image_url="https://www.corriecooks.com/wp-content/uploads/2023/05/american-food-2.jpg", image_preview=False)
    american_three_image = BusinessImage(business_id=29, user_id=4, image_url="https://www.corriecooks.com/wp-content/uploads/2023/05/american-food-2.jpg", image_preview=False)
    american_four_image = BusinessImage(business_id=30, user_id=5, image_url="https://www.corriecooks.com/wp-content/uploads/2023/05/american-food-2.jpg", image_preview=False)
    american_five_image = BusinessImage(business_id=31, user_id=6, image_url="https://www.corriecooks.com/wp-content/uploads/2023/05/american-food-2.jpg", image_preview=False)
    american_six_image = BusinessImage(business_id=32, user_id=1, image_url="https://www.corriecooks.com/wp-content/uploads/2023/05/american-food-2.jpg", image_preview=False)

    db.session.add_all([
        italian_one_previmage, italian_two_previmage, italian_three_previmage, italian_four_previmage, italian_five_previmage, italian_six_previmage,
        mexican_one_previmage, mexican_two_previmage, mexican_three_previmage, mexican_four_previmage, mexican_five_previmage, mexican_six_previmage, mexican_seven_previmage,
        middleast_one_previmage, middleast_two_previmage, middleast_three_previmage, middleast_four_previmage, middleast_five_previmage, middleast_six_previmage,
        jap_one_previmage, jap_two_previmage, jap_three_previmage, jap_four_previmage, jap_five_previmage, jap_six_previmage, jap_seven_previmage,
        american_one_previmage, american_two_previmage, american_three_previmage, american_four_previmage, american_five_previmage, american_six_previmage,
        italian_one_image, italian_two_image, italian_three_image, italian_four_image, italian_five_image, italian_six_image,
        mexican_one_image, mexican_two_image, mexican_three_image, mexican_four_image, mexican_five_image, mexican_six_image, mexican_seven_image,
        middleast_one_image, middleast_two_image, middleast_three_image, middleast_four_image, middleast_five_image, middleast_six_image,
        jap_one_image, jap_two_image, jap_three_image, jap_four_image, jap_five_image, jap_six_image, jap_seven_image, american_one_image, american_two_image, american_three_image, american_four_image, american_five_image, american_six_image,
        ])

def undo_businesses_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()

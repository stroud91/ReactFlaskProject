from app.models import db, Business
import datetime
from sqlalchemy.sql import text

def seed_businesses():

    business1 = Business(
        name="Rita's Italian Ice & Frozen Custard",
        address="7866 N Academy Blvd Colorado",
        city="Colorado",
        state="CO",
        zip_code="12345",
        website="https://www.ritasice.com/",
        about="""Specialties
                 Rita's Italian Ice & Frozen Custard is the largest Italian Ice concept in the nation,
                 currently operating in 31 states with over 600 shops.
                 Our popular chain offers a variety of frozen treats including its famous Italian Ice,
                 made fresh daily, Frozen Custard, Milkshakes, Sundaes, CustardCookie Sandwiches,
                 layered Gelati, as well as signature Misto and Blendini creations.

                History
                 Established in 2016.

                 Rita's Italian Ice of Colorado Springs opened in August of 2016.""",
        phone_number="(719) 465-2867",
        type="Ice Cream & Frozen Yogurt, Desserts , Pretzels",
        business_image="",
        category_id=1,
        owner_id=1,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )


    business2 = Business(
        name="Bella's Bagels",
        address="3582 Blue Horizon Vw Ste 148",
        city="Colorado Springs",
        state="CO",
        zip_code="80924",
        website="https://www.getbellasbagels.com/",
        about="""Specialties
                 The most delicious bagel in Colorado! Bella's Bagels - baked for boosting happiness.
                 Family-owned, Bella's Bagels is a genuine NY-style bagel shop born in Colorado Springs and
                 inspired by NJ roots. Our bagels are formed with natural ingredients, sourced from devoted providers,
                 crafted with careful nuance, baked for boosting happiness! And, our home made sandwiches are
                 the perfect comfort food for the upcoming holiday season. Consider a Bella's Bagel your warm dough hug.

                History
                 Established in 2023.

                 Jason and Michelle are two crazy technologists who have a deep love for bagels.
                 Jason is a serial entrepreneur, originally from NJ where bagel snobs are grown and
                 deployed into the world. Michelle runs cybersecurity programs that protect assets in space
                 (yes, Space.) Jason still remembers the smell of freshly baked bagels wafting
                 through the streets of his childhood home. Michelle is a home baking superstar whose been
                 whipping up amazing bagels for the family for years. Her food truly makes people happy.
                 During the pandemic, they decided to share their passion for bagels with the Springs and
                 started selling at local farmers markets. The response was overwhelming - selling out almost
                 every time and getting a fast following! Fast forward...they decided in the Summer of 2022 to
                 take a huge leap of faith and build their very own traditional, NY Style bagel shop.
                 These bagels are truly baked for boosting happiness. Come visit us and taste the love that
                 goes into each bagel we bake!""",
        phone_number="1-234-567-8902",
        type="FoodCoffee & Tea, Sandwiches, Bagels",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=1,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    business3 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business2 = Business(
        name="Example Business 2",
        address="456 Another St.",
        city="Another City",
        state="AN",
        zip_code="67890",
        website="http://www.example2.com",
        about="Another example business description.",
        phone_number="1-234-567-8902",
        type="Another Type",
        business_image="http://link-to-image.com/image2.jpg",
        category_id=2,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    db.session.add(business1)
    db.session.add(business2)
    db.session.add(business3)
    db.session.add(business4)
    db.session.add(business5)
    db.session.add(business6)
    db.session.add(business7)
    db.session.add(business8)
    db.session.add(business9)
    db.session.add(business10)
    db.session.add(business11)
    db.session.add(business12)
    db.session.add(business13)
    db.session.add(business14)
    db.session.add(business15)
    db.session.add(business16)
    db.session.add(business17)
    db.session.add(business18)
    db.session.add(business19)
    db.session.add(business20)
    db.session.add(business21)
    db.session.add(business22)
    db.session.add(business23)
    db.session.add(business24)
    db.session.add(business25)
    db.session.add(business26)
    db.session.add(business27)
    db.session.add(business28)
    db.session.add(business29)
    db.session.add(business30)
    db.session.commit()

def undo_businesses():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()

from app import app
from models import db, Catalogue, News, User
from datetime import datetime

# Convert string dates to datetime.date objects
def str_to_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()

# Create instances of your models
catalogue_entries = [
    Catalogue(
        image_url='https://imgd.aeplcdn.com/664x374/n/cw/ec/110233/camry-exterior-right-front-three-quarter-3.jpeg?isig=0&q=80',
        brand='Toyota',
        model='Camry',
        category='Sedan',
        price='KES2,400,000',
        rating=4.5,
        release_date=str_to_date('2023-01-01')
    ),
    Catalogue(
        image_url='https://d2q68z18seh9hj.cloudfront.net/wp-content/uploads/2020/08/27182529/Civic-Sedan-LX-in-Platinum-Pearl-White.png',
        brand='Honda',
        model='Civic',
        category='Sedan',
        price='KES 3,200,000',
        rating=4.6,
        release_date=str_to_date('2023-02-01')
    ),
    Catalogue(
        image_url='https://hips.hearstapps.com/hmg-prod/images/2025-ford-mustang-60th-anniversary-exterior-66227932bb88e.jpg?crop=0.596xw:1.00xh;0.199xw,0&resize=768:*',
        brand='Ford',
        model='Mustang',
        category='Coupe',
        price='KES 3,600,000',
        rating=4.8,
        release_date=str_to_date('2023-03-01')
    ),
    Catalogue(
        image_url='https://www.chevrolet.com/content/dam/chevrolet/na/us/english/index/vehicles/2024/suvs/tahoe/trims/2023-tahoe-cc10706-1lz-g1w-trimselector.png?imwidth=960',
        brand='Chevrolet',
        model='Tahoe',
        category='SUV',
        price='KES 4,500,000',
        rating=4.7,
        release_date=str_to_date('2023-04-01')
    ),
    Catalogue(
        image_url='https://www.edmunds.com/assets/m/cs/blt993d3e8016b0c368/6568dd4adf42826a732f0d83/2025_model-3_f34_tesla_fe_9998_1122231_1280.jpg',
        brand='Tesla',
        model='Model 3',
        category='Sedan',
        price='KES 4,000,000',
        rating=4.9,
        release_date=str_to_date('2023-05-01')
    ),
    Catalogue(
        image_url='https://s1.cdn.autoevolution.com/images/models/TOYOTA_Corolla--EU--2022_main.jpg',
        brand='Toyota',
        model='Corolla',
        category='Sedan',
        price='KES 2,500,000',
        rating=4.5,
        release_date=str_to_date('2022-11-15')
    ),
    Catalogue(
        image_url='https://cgi.chevrolet.com/mmgprod-us/dynres/prove/image.gen?i=2024/CC10543/CC10543__1LT/G6M_09Y_0ST_1LT_1SZ_2ST_3ST_4AA_4ST_5FC_5ST_63G_6BJ_7BJ_8HB_9HB_A2X_A68_A7E_AED_AEQ_AKO_AL0_ASV_AU3_AVI_AVJ_AXG_AXK_AY0_AZ3_B1J_B30_B59_BTM_BTV_BWN_C49_C59_C5U_CGN_CJ2_CTT_D31_D75_DLF_DNS_DP9_E35_E63_EF7_ENL_F_FE9_FJW_G80_GF3_GU6_H0U_IOK_IVN_J24_J61_JBP_K34_KA1_KC9_KI3_KI4_KL9_KW5_L3B_MAH_MFC_MSL_N06_N37_NB5_NTB_PCL_PDU_PED_PPW_PRF_QDF_QK2_QT5_RCV_RFQ_RIA_RM7_RSR_RWL_SAF_SLM_SU7_T8Z_TDM_TQ5_TUF_U2K_U73_UBI_UBJ_UDV_UE1_UE4_UEU_UF2_UH5_UHX_UHY_UJN_UK3_UKJ_UMN_UQF_URC_URD_UTJ_UVB_V46_V8D_VBJ_VJH_VK3_VRF_VRG_VRH_VRK_VRL_VRM_VRN_VRR_VSX_VT7_VV4_WLD_WMI_WMY_WPQ_X88_XCQ_YD9_YM8_Z82_Z85_ZL3_ZM9gmds2.jpg&v=deg01&std=true&country=US',
        brand='Chevrolet',
        model='Silverado',
        category='Truck',
        price='KES 5,000,000',
        rating=4.6,
        release_date=str_to_date('2023-02-28')
    ),
    Catalogue(
        image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiS-YEzGlajBEMSNN2DpI6TbBFQ1gmaSvaKA&s',
        brand='Nissan',
        model='Altima',
        category='Sedan',
        price='KES 2,700,000',
        rating=4.4,
        release_date=str_to_date('2023-04-15')
    ),
    Catalogue(
        image_url='https://imgd.aeplcdn.com/1280x720/n/cw/ec/150705/glc-exterior-right-front-three-quarter-94.jpeg?isig=0&q=80',
        brand='Mercedes-Benz',
        model='GLC',
        category='SUV',
        price='KES 6,200,000',
        rating=4.9,
        release_date=str_to_date('2023-06-20')
    ),
    Catalogue(
        image_url='https://crdms.images.consumerreports.org/c_lfill,w_470,q_auto,f_auto/prod/cars/cr/model-years/15099-2023-audi-a4',
        brand='Audi',
        model='A4',
        category='Sedan',
        price='KES 4,500,000',
        rating=4.7,
        release_date=str_to_date('2023-07-05')
    ),
    Catalogue(
        image_url='https://media.drive.com.au/obj/tx_q:70,rs:auto:1280:720:1/driveau/upload/vehicles/redbook/AUVSUBA2024AEAX/S000DEXK',
        brand='Subaru',
        model='Outback',
        category='SUV',
        price='KES 3,300,000',
        rating=4.6,
        release_date=str_to_date('2023-08-12')
    ),
    Catalogue(
        image_url='https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_default/v1/editorial/vhs/Mitsubishi-Pajero.png',
        brand='Mitsubishi',
        model='Pajero',
        category='SUV',
        price='KES 4,000,000',
        rating=4.5,
        release_date=str_to_date('2023-09-25')
    ),
    Catalogue(
        image_url='https://dashboard.kaiandkaro.com/media/vehicles/images/1000639682.jpg',
        brand='Toyota',
        model='Hiace',
        category='Vans',
        price='KES 3,299,999',
        rating=4.5,
        release_date=str_to_date('2016-09-25')
    )
]

# Create instances for news blog
news_entries = [
    News(
        image_url='https://i.ebayimg.com/images/g/b8wAAOSwE0JY~i3n/s-l1200.webp',
        description='New Model Release: Toyota Camry 2023',
        location='Mombasa, Kenya',
        ticket_price='KES 4,500', 
        date=str_to_date('2024-08-15')
    ),
    News(
        image_url='https://png.pngtree.com/png-clipart/20220429/original/pngtree-car-battery-charge-innovation-technology-vintage-poster-of-electric-vehicle-recharge-png-image_7569522.png',
        description='Electric Cars: The Future of Automotive Industry',
        location='Langata, Nairobi',
        ticket_price='KES 5,000', 
        date=str_to_date('2024-09-11')
    ),
    News(
        image_url='https://d1csarkz8obe9u.cloudfront.net/posterpreviews/car-rentals-poster-design-template-b6eec7913ae957e894b2b40d1643872b.jpg?ts=1618392753',
        description='Car Rentals Expo 2024',
        location='Kisumu, Kenya',
        ticket_price='KES 4,000', 
        date=str_to_date('2024-10-10')
    ),
    News(
        image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQljWlj96aCdZY_7gjsibK6WBXNiXuuDLXIkh_VYXCPnmahZUU0aJN-TsaW9Oi_1RMky7E&usqp=CAU',
        description='Special Discounts on Car Rentals',
        location='Thika, Kenya',
        ticket_price='KES 3,500', 
        date=str_to_date('2024-11-05')
    ),
    News(
        image_url='https://img.freepik.com/premium-psd/car-rental-promotion-social-media-instagram-post-banner-template_349461-64.jpg',
        description='Rent-A-Car: Best Practices and Tips',
        location='Nakuru, Kenya',
        ticket_price='KES 2,000', 
        date=str_to_date('2024-12-01')
    )
]

# Add instances to the session and commit
with app.app_context():
    db.session.add_all(catalogue_entries)
    db.session.add_all(news_entries)
    db.session.commit()

    print("Data seeded successfully!")
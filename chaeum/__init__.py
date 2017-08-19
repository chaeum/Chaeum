import mysql.connector.pooling as pooling
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

# from flask_jwt_extended import JWTManager, jwt_required, \
#     create_access_token,  jwt_refresh_token_required, \
#     create_refresh_token, get_jwt_identity, set_access_cookies, \
#     set_refresh_cookies, unset_jwt_cookies

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'testtest'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:wjdrbdud1`@testwebinstance.ciowpdvbzwrs.ap-northeast-2.rds.amazonaws.com:3306/chaeum'
#
api = Api(app)
# db = SQLAlchemy(app)

jwt = JWTManager(app)

db_user = "admin"
db_pass = "chaeum!01"
db_url = "testwebinstance.ciowpdvbzwrs.ap-northeast-2.rds.amazonaws.com"
db_name = "chaeumTest"

cnx_pool = pooling.MySQLConnectionPool(pool_name="chaeum_pool",
                                                       pool_size=10,
                                                       autocommit=True,
                                                       user=db_user,
                                                       password=db_pass,
                                                       host=db_url,
                                                       database=db_name)

from chaeum.resources.api.user import User
api.add_resource(User, '/api/users', '/api/users/<string:user_id>')
from chaeum.resources.api.auth import Auth
api.add_resource(Auth, '/api/auth')
from chaeum.resources.api.magazine import Magazine
api.add_resource(Magazine, '/api/magazines', '/api/magazines/<int:magazine_id>')
from chaeum.resources.api.magazine_comment import Magazine_Comment
api.add_resource(Magazine_Comment, '/api/magazine_comments', '/api/magazine_comments/<int:comment_id>')
from chaeum.resources.api.brnd import Brnd
api.add_resource(Brnd, '/api/brnds', '/api/brnds/<int:brnd_id>')
from chaeum.resources.api.hairprd import HairPrd
api.add_resource(HairPrd, '/api/hairprds', '/api/hairprds/<int:hairprd_id>')
from chaeum.resources.api.medicine import Medicine
api.add_resource(Medicine, '/api/meds', '/api/meds/<int:med_id>')
from chaeum.resources.api.medicine_spec import MedicineSpec
api.add_resource(MedicineSpec, '/api/specmeds', '/api/specmeds/<int:med_id>')
from chaeum.resources.api.medicine_norm import MedicineNorm
api.add_resource(MedicineNorm, '/api/normmeds', '/api/normmeds/<int:med_id>')
from chaeum.resources.api.medicine_etc import MedicineEtc
api.add_resource(MedicineEtc, '/api/etcmeds', '/api/etcmeds/<int:med_id>')
from chaeum.resources.api.hairshop import HairShop
api.add_resource(HairShop, '/api/hairshops', '/api/hairshops/<int:hairshop_id>')
from chaeum.resources.api.clinic import Clinic
api.add_resource(Clinic, '/api/clinics', '/api/clinics/<int:clinic_id>')
from chaeum.resources.api.comp import Comp
api.add_resource(Comp, '/api/comps', '/api/comps/<int:comp_id>')
from chaeum.resources.api.complist import CompList
api.add_resource(CompList, '/api/complists', '/api/complists/<int:complist_id>')
from chaeum.resources.api.complist_hairprd import CompList_Hairprd
api.add_resource(CompList_Hairprd, '/api/comp_hairprds', '/api/comp_hairprds/<int:complist_id>')
from chaeum.resources.api.complist_medicine import CompList_Medicine
api.add_resource(CompList_Medicine, '/api/comp_meds', '/api/comp_meds/<int:complist_id>')
from chaeum.resources.api.review import Review
api.add_resource(Review, '/api/reviews', '/api/reviews/<int:review_id>')
from chaeum.resources.api.review_hairprd import ReviewHairprd
api.add_resource(ReviewHairprd, '/api/review_hairprds')
from chaeum.resources.api.review_medicine import ReviewMedicine
api.add_resource(ReviewMedicine, '/api/review_meds')
from chaeum.resources.api.review_clinic import ReviewClinic
api.add_resource(ReviewClinic, '/api/review_clinics')
from chaeum.resources.api.like import Like
api.add_resource(Like, '/api/likes', '/api/likes/<int:like_id>')
from chaeum.resources.api.like_hairprd import LikeHairPrd
api.add_resource(LikeHairPrd, '/api/like_hairprds')
from chaeum.resources.api.like_check import LikeCheck
api.add_resource(LikeCheck, '/api/like_check')
from chaeum.resources.api.like_owner import LikeOwner
api.add_resource(LikeOwner, '/api/like_owners')
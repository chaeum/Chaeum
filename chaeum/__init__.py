import mysql.connector.pooling as pooling
from flask import Flask, url_for
from flask_jwt_extended import JWTManager
from flask_restful import Api
import os

# from flask_jwt_extended import JWTManager, jwt_required, \
#     create_access_token,  jwt_refresh_token_required, \
#     create_refresh_token, get_jwt_identity, set_access_cookies, \
#     set_refresh_cookies, unset_jwt_cookies

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'testtest'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:wjdrbdud1`@testwebinstance.ciowpdvbzwrs.ap-northeast-2.rds.amazonaws.com:3306/chaeum'

# browser cache ignore for static files
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

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
api.add_resource(Medicine, '/api/medicines', '/api/medicines/<int:medicine_id>')
from chaeum.resources.api.medicine_norm import MedicineNorm
api.add_resource(MedicineNorm, '/api/medicines', '/api/medicines/<int:medicine_id>')
from chaeum.resources.api.clinic import Clinic
api.add_resource(Clinic, '/api/clinics', '/api/clinics/<int:clinic_id>')
from chaeum.resources.api.hairshop import HairShop
api.add_resource(HairShop, '/api/hairshops', '/api/hairshops/<int:hairshop_id>')
from chaeum.resources.api.review import Review
api.add_resource(Review, '/api/reviews', '/api/reviews/<int:review_id>')
from chaeum.resources.api.review_summary import ReviewSummary
api.add_resource(ReviewSummary, '/api/review_summarys')
from chaeum.resources.api.like import Like
api.add_resource(Like, '/api/likes', '/api/likes/<int:like_id>')


from chaeum.resources.web.index import WebIndex
api.add_resource(WebIndex, '/index')
from chaeum.resources.web.index import WebSearch
api.add_resource(WebSearch, '/search')
from chaeum.resources.web.hairprd import WebHairPrdList
api.add_resource(WebHairPrdList, '/hairprds')
from chaeum.resources.web.hairprd import WebHairPrdDetail
api.add_resource(WebHairPrdDetail, '/hairprds/<int:hairprd_id>')
from chaeum.resources.web.hairshop import WebHairShopList
api.add_resource(WebHairShopList, '/hairshops')
from chaeum.resources.web.hairshop import WebHairShopDetail
api.add_resource(WebHairShopDetail, '/hairshops/<int:hairshop_id>')
from chaeum.resources.web.magazine import WebMagazineList
api.add_resource(WebMagazineList, '/magazines')

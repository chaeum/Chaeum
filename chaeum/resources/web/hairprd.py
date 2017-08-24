from flask_restful import reqparse, Resource
from chaeum.common.render import render_html


class WebHairPrd(Resource):
    def get(self):
        return render_html('hairprd/hairprd.html')


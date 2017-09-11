from flask_restful import reqparse, Resource
from chaeum.common.render import render_html


class WebCompEWG(Resource):
    def get(self):
        return render_html('comp/ewg.html')


class WebCompList(Resource):
    def get(self):
        return render_html('comp/list.html')


class WebCompListDetail(Resource):
    def get(self, listdetail_id=None):
        return render_html('comp/list_detail.html')

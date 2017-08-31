from flask_restful import reqparse, Resource
from chaeum.common.render import render_html


class WebMagazineList(Resource):
    def get(self):
        return render_html('magazine/magazine.html')


# class WebMagazineDetail(Resource):
#     def get(self):
#         return render_html('magazine/magazine_detail.html')

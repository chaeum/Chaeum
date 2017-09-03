from flask_restful import reqparse, Resource
from chaeum.common.render import render_html


class WebMedicineSpecList(Resource):
    def get(self):
        return render_html('medicine/spec.html')


class WebMedicineNormList(Resource):
    def get(self):
        return render_html('medicine/norm.html')


class WebMedicineEtcList(Resource):
    def get(self):
        return render_html('medicine/etc.html')


# class WebBoardDetail(Resource):
#     def get(self, board_id=None):
#         return render_html('board/board_detail.html')


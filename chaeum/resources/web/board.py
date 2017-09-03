from flask_restful import reqparse, Resource
from chaeum.common.render import render_html


class WebBoardList(Resource):
    def get(self):
        return render_html('board/board.html')


# class WebBoardDetail(Resource):
#     def get(self, board_id=None):
#         return render_html('board/board_detail.html')


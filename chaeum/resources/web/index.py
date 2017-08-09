from flask_restful import Resource
from chaeum.common.render import render_html


class Index(Resource):
    def get(self):
        return render_html('index.html')


class Sample(Resource):
    def get(self):
        return render_html('sample.html')
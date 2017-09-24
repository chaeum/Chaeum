from math import ceil
from flask_restful import reqparse, Resource
from chaeum.common.render import render_html
from chaeum.common.db import fetch_one_from_db, fetch_all_from_db

list_page_parser = reqparse.RequestParser()
list_page_parser.add_argument(
    'page', type=int, help='current page index', default=1
)


def fetch_list_cnt():
    query = """
        SELECT COUNT(*) FROM TBMAGAZINE
    """
    try:
        result = fetch_one_from_db(query)
        if result is not None:
            return result[0]
        else:
            return 0
    except Exception as e:
        print(e)
        return 0


def fetch_list_page(page, pageSize):
    query = """
        SELECT * FROM TBMAGAZINE
        ORDER BY mod_date DESC
        LIMIT %d, %d
    """

    try:
        result = fetch_all_from_db(query % (page * pageSize, pageSize))
        list = []
        for res in result:
            id, title, contents, like_cnt, comment_cnt, reg_date, mod_date = res
            dict = {
                "id": id,
                "title": title,
                "contents": contents,
                "like_cnt": like_cnt,
                "comment_cnt": comment_cnt,
                "reg_date": reg_date,
                "mod_date": mod_date
            }
            list.append(dict)
        return list
    except Exception as e:
        print(e)
        return []


class WebMagazineList(Resource):
    def get(self):
        args = list_page_parser.parse_args()

        pageSize = 4
        listSize = fetch_list_cnt()
        pageCnt = ceil((listSize-1) / pageSize)
        list = fetch_list_page(args.page-1, pageSize)

        return render_html('magazine/magazine.html', list=list, page=args.page, pageCnt=pageCnt)


# class WebMagazineDetail(Resource):
#     def get(self):
#         return render_html('magazine/magazine_detail.html')

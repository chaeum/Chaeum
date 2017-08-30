from __future__ import print_function

from flask import request
from flask_restful import fields, marshal_with, reqparse, Resource
from flask_jwt_extended import JWTManager, jwt_required
import sys

from chaeum import cnx_pool, jwt

def isstr(s):
    return s if s else ''

result_fields = {
    'msg': fields.String,
    'count': fields.Integer,
}


def fetch_check_hairprd(owner_id, hairprd_id):
    conn = cnx_pool.get_connection()
    cursor = conn.cursor()

    query = """
        SELECT count(*)
          FROM TBLIKE
         WHERE category = 1
           AND owner_id = %s
           AND hairprd_id = %s
    """

    try:
        cursor.execute(query, (owner_id, hairprd_id))
        result = cursor.fetchone()
        count = 0

        for item in result:
            count = item

    except Exception as e:
        return None, -1
    finally:
        conn.close()

    return True, count


def fetch_check_med(owner_id, med_id):
    conn = cnx_pool.get_connection()
    cursor = conn.cursor()

    query = """
        SELECT count(*)
          FROM TBLIKE
         WHERE category = 2
           AND owner_id = %s
           AND med_id = %s
    """

    try:
        cursor.execute(query, (owner_id, med_id))

        result = cursor.fetchone()
        count = 0

        for item in result:
            count = item

    except Exception as e:
        return None, -1
    finally:
        conn.close()

    return True, count


def fetch_check_hairshop(owner_id, hairshop_id):
    conn = cnx_pool.get_connection()
    cursor = conn.cursor()

    query = """
        SELECT count(*)
          FROM TBLIKE
         WHERE category = 3
           AND owner_id = %s
           AND hairshop_id = %s
    """

    try:
        cursor.execute(query, (owner_id, hairshop_id))

        result = cursor.fetchone()
        count = 0

        for item in result:
            count = item

    except Exception as e:
        return None, -1
    finally:
        conn.close()

    return True, count


def fetch_check_clinic(owner_id, clinic_id):
    conn = cnx_pool.get_connection()
    cursor = conn.cursor()

    query = """
        SELECT count(*)
          FROM TBLIKE
         WHERE category = 4
           AND owner_id = %s
           AND clinic_id = %s
    """

    try:
        cursor.execute(query, (owner_id, clinic_id))

        result = cursor.fetchone()
        count = 0

        for item in result:
            count = item

    except Exception as e:
        return None, -1
    finally:
        conn.close()

    return True, count


def fetch_check_magazine(owner_id, magazine_id):
    conn = cnx_pool.get_connection()
    cursor = conn.cursor()

    query = """
        SELECT count(*)
          FROM TBLIKE
         WHERE category = 5
           AND owner_id = %s
           AND magazine_id = %s
    """

    try:
        cursor.execute(query, (owner_id, magazine_id))

        result = cursor.fetchone()
        count = 0

        for item in result:
            count = item

    except Exception as e:
        return None, -1
    finally:
        conn.close()

    return True, count


def fetch_check_brnd(owner_id, brnd_id):
    conn = cnx_pool.get_connection()
    cursor = conn.cursor()

    query = """
        SELECT count(*)
          FROM TBLIKE
         WHERE category = 6
           AND owner_id = %s
           AND brnd_id = %s
    """

    try:
        cursor.execute(query, (owner_id, brnd_id))

        result = cursor.fetchone()
        count = 0

        for item in result:
            count = item

    except Exception as e:
        return None, -1
    finally:
        conn.close()

    return True, count

#########################################
# 1 : hairprd
# 2 : med
# 3 : hairshop
# 4 : clinic
# 5 : magazine
# 6 : brnd
#########################################
class LikeCheck(Resource):

    @marshal_with(result_fields)
    # @jwt_required
    def get(self, like_id=None):
        # args = post_parser.parse_args()
        # current_user = get_jwt_identity()
        args = request.args
        category = args.get('category')
        owner_id = args.get('owner_id')
        hairprd_id = args.get('hairprd_id')
        med_id = args.get('med_id')
        hairshop_id = args.get('hairshop_id')
        clinic_id = args.get('clinic_id')
        magazine_id = args.get('magazine_id')
        brnd_id = args.get('brnd_id')
        count = 0

        if owner_id is not None:
            if category is '1' and hairprd_id is not None:
                result, count = fetch_check_hairprd(owner_id, hairprd_id)
            elif category is '2' and med_id is not None:
                result, count = fetch_check_med(owner_id, med_id)
            elif category is '3' and hairshop_id is not None:
                result, count = fetch_check_hairshop(owner_id, hairshop_id)
            elif category is '4' and clinic_id is not None:
                result, count = fetch_check_clinic(owner_id, clinic_id)
            elif category is '5' and magazine_id is not None:
                result, count = fetch_check_magazine(owner_id, magazine_id)
            elif category is '6' and brnd_id is not None:
                result, count = fetch_check_brnd(owner_id, brnd_id)
            else:
                result = None
        else:
            result = None

        if not result:
            responseObject = {
                'msg': 'Fail',
                'count': count
            }
            return responseObject, 401
        else:
            responseObject = {
                'msg': 'Success',
                'count': count
            }
            return responseObject, 200
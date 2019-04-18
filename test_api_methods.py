from http_client import *
from constans import *

import datetime


def test_when_get_cards_url_expected_code200():
    resp = post_request(url=cards_url, data=standard_body(), headers=get_headers())
    print(resp.text)
    #return resp
    assert resp.status_code == 200


def test_when_get_check_message_error_expected_sucess():
    resp = post_request(url=cards_url, data=standard_body(), headers=get_headers())
    print(resp.text)
    check = default_json_to_dict(resp.text)
    message = check['GetCardsResult']['ErrorMessage']['Message']
    assert message == 'SUCCESS'

def test_when_get_categories_expected_code200():
    resp = post_request(url=categories_url, data=standard_body(), headers=get_headers())
    print(resp.text)
    assert resp.status_code == 200
    return resp


check1 = ()
def test_when_getblacklist_and_check_data_in_responce_expected_red_is_in_responce():
    resp = post_request(url=blacklist_url, data=standard_body(), headers=get_headers())
    print(resp.text)
    check = default_json_to_dict(resp.text)
    check1 = check['GetBlackListResult']['Data']
    assert 'RED' in check['GetBlackListResult']['Data']
    return resp

def test_when_getblacklist_xpected_code200():
    resp = post_request(url=blacklist_url, data=standard_body(), headers=get_headers())
    print(resp.text)
    assert resp.status_code == 200


def test_when_appversions_expected_code200():
    resp = post_request(url=appversions_url, data=standard_body(), headers=get_headers())
    print(resp.text)
    assert resp.status_code == 200
    return resp

def test_when_get_foxtrotcardexpected_code200():
    resp = post_request(url=foxtrotcard_url, data=standard_body(), headers=get_headers())
    print(resp.text)
    assert resp.status_code == 200
    return resp

def test_when_get_offers_expected_code200():
    resp = post_request(url=offers_url, data=standard_body(), headers=get_headers())
    print(resp.text)

    assert resp.status_code == 200
    return resp

def test_when_get_getretailers_expected_code200():
    resp = post_request(url=retailers_url, data=standard_body(), headers=get_headers())
    print(resp.text)
    assert resp.status_code == 200
    return resp


def test_when_get_getretailers_time1sec():
    starttime = datetime.datetime.now()
    print(starttime)
    resp = post_request(url=retailers_url, data=standard_body(), headers=get_headers())
    end = datetime.datetime.now()
    duration = (end - starttime).microseconds
    delta = datetime.timedelta(seconds=0.9).microseconds
    assert delta > duration
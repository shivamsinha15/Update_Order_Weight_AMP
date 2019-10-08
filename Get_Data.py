import Constant
import os
import Config_Post_Data


def read_login_credentials():
    login_userid = open('username.txt', mode='r')
    login_password = open('password.txt', mode='r')

    Constant.login_userid = login_userid.read()
    Constant.login_password = login_password.read()

    print('User credentials read successfully.')


def remove_unused_files():
    file_list = os.listdir(Constant.amplify_204_path)
    for file in file_list:
        content = open(Constant.amplify_204_path + file, 'r')
        lines = content.read()
        if_remove = Constant.re_pattern_file_to_remove.findall(lines)
        content.close()
        if len(if_remove) > 0:
            os.remove(Constant.amplify_204_path + file)


def get_info_204(file_root_path, file_name):
    file_path = file_root_path + file_name
    content = open(file_path, 'r')
    lines = content.read()
    pri_ref = Constant.re_pattern_204_pri_ref.findall(lines)[0]
    weight = Constant.re_pattern_204_weight.findall(lines)[0]
    content.close()
    return pri_ref, weight


def get_shipment_report_by_report_format(session_requests, csrf, pri_ref_str):
    # SEND FIRST POST REQUEST
    data_dict = Config_Post_Data.config_shipment_report(csrf, pri_ref_str)

    response = session_requests.post(
        Constant.url_post_shipment_report_format,
        data_dict
    )

    html_script = response.text
    urls = Constant.re_pattern_url_report_format.findall(html_script)
    for url in urls:
        session_requests.get(Constant.url_tms_root + url)

    response = session_requests.get(Constant.url_get_shipment_report_format0)
    html_script = response.text
    urls = Constant.re_pattern_url_report_format.findall(html_script)
    for url in urls:
        session_requests.get(Constant.url_tms_root + url)

    response = session_requests.get(Constant.url_get_shipment_report_format1)

    return response

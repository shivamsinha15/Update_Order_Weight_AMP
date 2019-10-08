import Post_Data
import Constant
import os
import G_API
import time
import Get_Data


if __name__ == '__main__':

    # START COUNTING RUNNING TIME
    start = time.time()

    # Go to the folder where saves Amplify 204 message. Remove unused files.
    Get_Data.remove_unused_files()
    print('Unused files removal completes.')

    # Create a dictionary object to save primary reference, file name, and weight information.
    weight_dict = dict()
    file_list = os.listdir(Constant.amplify_204_path)
    for file in file_list:
        pri_ref, weight = Get_Data.get_info_204(Constant.amplify_204_path, file)
        weight_dict[pri_ref] = [weight, Constant.amplify_204_path + file]

    # Convert primary reference list to a string separated by comma.
    pri_ref_str = ','.join([key for key, item in weight_dict.items()])

    # LOGIN TMS
    Get_Data.read_login_credentials()
    session_requests, csrf = Post_Data.login_tms()

    shipment_report_html_script = Get_Data.get_shipment_report_by_report_format(session_requests, csrf, pri_ref_str).text

    pri_refs = Constant.re_pattern_pri_ref.findall(shipment_report_html_script)
    oids = Constant.re_pattern_oid.findall(shipment_report_html_script)

    print('Updating item weight in shipments...')

    for i, oid in enumerate(oids):
        # Concatenate item list url for this shipment.
        url_item_list = Constant.url_item_list
        url_item_list = url_item_list.replace('OID_TO_REPLACE', oid)

        # Get item list html.
        response = session_requests.get(url_item_list)
        html_script = response.text

        # Get item html.
        item_oid = Constant.re_pattern_item_oid.findall(html_script)[0]
        url_item = Constant.url_item
        url_item = url_item.replace('OID_TO_REPLACE', item_oid)
        response = session_requests.get(url_item)
        html_script = response.text

        item_info_entry = Constant.re_pattern_item_edit_entry.findall(html_script)
        item_info_dropdown = Constant.re_pattern_item_edit_dropdown.findall(html_script)

        item_freight_class = item_info_dropdown[0]

        item_weight = weight_dict[pri_refs[i]][0]

        # Change weight on item.
        Post_Data.item_change_weight(session_requests, csrf, item_info_entry, item_freight_class, item_weight)

        # Remove files from folder.
        os.remove(weight_dict[pri_refs[i]][1])

    len_oid = len(oids)
    print('Process completes.', len_oid, 'number of shipments are updated. This window will be closed in 10 seconds.')

    # END TIME
    end = time.time()

    # UPDATE LOG REPORT ON GOOGLE SHEETS
    duration = end - start
    workbook_log = G_API.get_workbook_by_id(Constant.g_sheets_workbook_id_log)
    worksheet_log = G_API.get_worksheet_by_id(workbook_log, Constant.g_sheets_worksheet_id_log)
    Post_Data.log_event(worksheet_log, duration)

    time.sleep(10)


# html_script = response.text

# save_file = open(Constant.root_path + 'test.html', 'w+')
# save_file.write(html_script)
# save_file.close()
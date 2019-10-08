import re

root_path = 'C:\\Users\\Zhou_Charles\\Desktop\\'
amplify_204_path = 'T:\\Amplify204\\input\\'

login_userid = None
login_password = None

time_format_military = '%m/%d/%Y %H:%M'
process_name = 'Update Order Weight Amplify'
g_sheets_workbook_id_log = '1Yudm7JfKSgL82zyHXnDKUjJfoI5VGoEsPHgysPXcZ4g'
g_sheets_worksheet_id_log = 0

url_tms_login = 'https://dsclogistics.mercurygate.net/MercuryGate/login/LoginProcess.jsp'
url_list_transports = 'https://dsclogistics.mercurygate.net/MercuryGate/transport/listTransports.jsp'
url_list_shipments = 'https://dsclogistics.mercurygate.net/MercuryGate/shipment/listShipment.jsp'
url_tms_root = 'https://dsclogistics.mercurygate.net'

url_post_shipment_report_format = 'https://dsclogistics.mercurygate.net/MercuryGate/report/ReportFormat_process.jsp?' \
                                  'type=Shipment&summary=false'
url_get_request_ref_type_initial = 'https://dsclogistics.mercurygate.net/MercuryGate/common/extClassLoader.jsp?appName=' \
                                  'MG.tms.portlet.enterprise.ReferenceTypesApp'
url_post_request_ref_type = 'https://dsclogistics.mercurygate.net/MercuryGate/extJsPortletData/ReferenceTypesPortlet'

url_post_add_ref = 'https://dsclogistics.mercurygate.net/MercuryGate/common/addReference_process.jsp'
url_post_edit_item = 'https://dsclogistics.mercurygate.net/MercuryGate/item/editPackageItemGroup_process.jsp'

url_item_list = 'https://dsclogistics.mercurygate.net/MercuryGate/item/listItems.jsp?sidOwner=(OID_TO_REPLACE,3700,0)'
url_item = 'https://dsclogistics.mercurygate.net/MercuryGate/item/editPackageItemGroup.jsp?bIsShipUnit=false&oid=OID_TO_REPLACE'
url_pendo_io = 'https://cdn.pendo.io/agent/static/API_TO_REPLACE/pendo.js'

re_pattern_csrf = re.compile('\<meta name\=\"_csrf\" content\=\"([\w\-]*)\" \/\>')
re_pattern_menu_value = re.compile('\<a href\=\"\.\.\/mainframe\/menuLHS\.jsp\?sMenuValue\=([\d\(\)\,]*)'
                                  '\&sMenuSelected\=\*\-\%3EDetail')
re_pattern_oid = re.compile('OID\' class\=\"DetailBodyTableRowOdd \"\>(\d{11})\<\/td\>')
re_pattern_load_ref = re.compile('Load Reference\' class\=\"DetailBodyTableRowOdd \"\>([\d]*) \(Load Number')
re_pattern_url_parse = re.compile('\<script src\=\"([\w\/\.\?\=]*)\" type\=\"text\/javascript\"\>\<\/script\>')
re_pattern_item_oid = re.compile('javascript\:remove\((\d{11})\)\;')
re_pattern_pri_ref = re.compile('\<td align\=LEFT title\=\'Primary Reference\' class\=\"DetailBodyTableRowOdd '
                                '\"\>(\d+) \(Customer Reference Number\)')


re_pattern_api_key = re.compile("\}\)\(\'([\w\-]{36})\'\)\;")


url_get_shipment_report_format0 = 'https://dsclogistics.mercurygate.net/MercuryGate/shipment/listShipment.jsp?' \
                                   'sidAction=&action=&fromExt=false&type=Shipment&full=&nSetNumber=1&sReturnURL='
url_get_shipment_report_format1 = 'https://dsclogistics.mercurygate.net/MercuryGate/shipment/listShipment.jsp?' \
                                  'norefresh=&sidAction=&action=&type=Shipment&full=&nSetNumber=1&sReturnURL='
re_pattern_url_report_format = re.compile('\<script src\=\"([\/\w\.\?\=]*)\"')

re_pattern_item_edit_entry = re.compile('\" value\=\"([\w\s\.\,]*)\"')
re_pattern_item_edit_dropdown = re.compile('selected value\=\"([\w\s]*)\"')

re_pattern_weight_204_shearers = re.compile('\*\*CA\*\d+\*L\*([\d\.]+)\~')

re_pattern_file_to_remove = re.compile('AK1\*QM')
re_pattern_204_pri_ref = re.compile('B2\*\*DRSC\*\*(\d+)\*\*')
re_pattern_204_weight = re.compile('\*\*CA\*\d+\*L\*([\d\.]+)\~')

field_load_number = 'Ref: 1174978200'

oid_enterprise = 54775198209 #ezVision

menu_value_ref_type_trade = '(19217908000,3250,0)'

html_equivalence_and = '&amp;'

data_dict_item = {
    '_csrf': '',
    'bIsShipUnit': '',
    'oid': '',
    'nSequence': '1',
    'sItemID': '',
    'sDescription': '',
    'fFreightClass': '',
    'sNMFC': '',
    'fOrderedQuantity': '',
    'sOrderedPackageType': 'PLT',
    'fPlannedQuantity': '',
    'sPlannedPackageType': 'PLT',
    'fActualQuantity': '',
    'sActualPackageType': 'PLT',
    'fPlannedWeight': '',
    'sPlannedUnits': 'lb',
    'fActualWeight': '',
    'sActualUnits': 'lb',
    'fLength': '',
    'fWidth': '',
    'fHeight': '',
    'sDimensionsUOM': 'in',
    'fDeliveredWeight': '',
    'sDeliveredUnits': 'lb',
    'sCommodity': 'None',
    'fCube': '',
    'fTemperatureMin': '',
    'fTemperatureMax': '',
    'sTemperatureUOM': 'F',
    'nStackability': '0',
    'sTrackingNumber': ''
}

field_oid = 'Oid'
field_pri_ref = 'PrimaryReference'
field_owner = 'OwningEnterpriseName'

filter_in = 'In'
filter_begins_with = 'Begins With'

open_shipment_report_by_report_format_dict = {
    '_csrf': '',
    'sourceurl': '',
    'sReturnURL': '',
    'full': '',
    'action': '     Use     ',
    'col0': '',
    'col1': '',
    'col2': '',
    'col3': '',
    'col4': '',
    'col5': '',
    'col6': '',
    'col7': '',
    'col8': '',
    'col9': '',
    'col10': '',
    'filterfield0': '', 'filtercrit0': '', 'filtervalue0': '', 'filtercase0': '',
    'filterfield1': '', 'filtercrit1': '', 'filtervalue1': '', 'filtercase1': '',
    'filterfield2': '', 'filtercrit2': '', 'filtervalue2': '', 'filtercase2': '',
    'filterfield3': '', 'filtercrit3': '', 'filtervalue3': '', 'filtercase3': '',
    'filterfield4': '', 'filtercrit4': '', 'filtervalue4': '', 'filtercase4': '',
    'filterfield5': '', 'filtercrit5': '', 'filtervalue5': '', 'filtercase5': '',
    'filterfield6': '', 'filtercrit6': '', 'filtervalue6': '', 'filtercase6': ''
}
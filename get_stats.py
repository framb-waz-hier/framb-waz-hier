#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from datetime import datetime

# import pprint

# wp_server = "http://192.168.56.105"
wp_server = "http://www.framb-waz.fr"
# wp_path   = "/wp_ext"
wp_path   = ""
wp_statistics_page = "/wp-admin/admin.php?page=wps_optimization_page"

wp_headers   = { 'Cookie': 'wordpress_7985e5d7cdafd0b581c9ec783c965d14=framb%7C1655652175%7CF1rVgrPdekPUb18ImDxuC0Acvq37ilCsO3GXt8U9cbE%7C4418fc4d4fe1e25c2b955c4d68257926389d752d229dfdb4a5427d936868f8ff; wordpress_logged_in_7985e5d7cdafd0b581c9ec783c965d14=framb%7C1655652175%7CF1rVgrPdekPUb18ImDxuC0Acvq37ilCsO3GXt8U9cbE%7C685ff4b397e64cad7cdd9efc85a7c7304f11208009acf772e0864f114b87cc60'
}

response = requests.get(wp_server + wp_path + wp_statistics_page, headers = wp_headers)

soup = BeautifulSoup(response.text, 'html.parser')

wps_export_file_value = soup.find(id='wps_export_file')['value']

# print(wps_export_file_value)

# for wp_page_export in ['visit', 'visitor', 'exclusions', 'pages', 'search' ] :
#     wp_data = { 'wps_export':       'true',
#                 'wps_export_file':  wps_export_file_value,
#                 'table-to-export':  wp_page_export,
#                 'export-file-type': 'csv',
#                 'export-headers':   '1'
#                }
#     response = requests.post(wp_server + wp_path + wp_statistics_page, data=wp_data, headers=wp_headers)
#     print(response.text)

wp_data = { 'wps_export':       'true',
            'wps_export_file':  wps_export_file_value,
            'table-to-export':  "pages",
            'export-file-type': 'csv',
            'export-headers':   '1'
           }
response = requests.post(wp_server + wp_path + wp_statistics_page, data=wp_data, headers=wp_headers)

# print(response.text)

now = datetime.now()
current_time = now.strftime("%Y-%m-%d-%H-%M-%S")


python_file = open("wp-statistics-"+ current_time + ".csv", "w")

python_file.write(response.text)
python_file.close()


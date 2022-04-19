#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime

wp_server = "http://www.framb-waz.fr"
wp_path   = ""
wp_statistics_page = "/wp-admin/admin.php?page=wps_optimization_page"

wp_login = 'http://www.framb-waz.fr/wp-login.php'
wp_admin = 'http://www.framb-waz.fr/wp-admin/'

if len(sys.argv) != 3 :
    print("Usage: %s <user> <pass>", sys.argv[0])
    sys.exit()

username = sys.argv[1]
password = sys.argv[2]

with requests.Session() as s:
    h = {
        'Cookie':'wordpress_test_cookie=WP Cookie check',
        'Content-Type':'application/x-www-form-urlencoded'
    }
    datas={
        'log':username,
        'pwd':password,
        'wp-submit':'Se connecter',
        'redirect_to':wp_admin,
        'testcookie':'1'
    }
    resp = s.post(wp_login, headers=h, data=datas)

    response = s.get(wp_server + wp_path + wp_statistics_page)

    soup = BeautifulSoup(response.text, 'html.parser')

    wps_export_file_value = soup.find(id='wps_export_file')['value']

    wp_data = { 'wps_export':       'true',
                'wps_export_file':  wps_export_file_value,
                'table-to-export':  "pages",
                'export-file-type': 'csv',
                'export-headers':   '1'
               }
    response = s.post(wp_server + wp_path + wp_statistics_page, data=wp_data)

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d-%H-%M-%S")

    python_file = open("wp-statistics-"+ current_time + ".csv", "w")

    python_file.write(response.text)
    python_file.close()


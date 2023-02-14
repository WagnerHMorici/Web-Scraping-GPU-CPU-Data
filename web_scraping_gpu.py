from bs4 import BeautifulSoup as bs

import requests

from datetime import datetime

from data_csv_writer import write_csv

# Newegg
gpus_newegg = ['https://www.newegg.com/msi-geforce-rtx-4070-ti-rtx-4070-ti-gaming-x-trio-12g/p/N82E16814137771?Description=rtx&cm_re=rtx-_-14-137-771-_-Product&quicklink=true',
'https://www.newegg.com/gigabyte-geforce-rtx-4070-ti-gv-n407taero-oc-12gd/p/N82E16814932582?Description=rtx&cm_re=rtx-_-14-932-582-_-Product',
'https://www.newegg.com/msi-geforce-rtx-4090-rtx-4090-gaming-x-trio-24g/p/N82E16814137761?Description=rtx&cm_re=rtx-_-14-137-761-_-Product&quicklink=true',
'https://www.newegg.com/msi-geforce-rtx-4090-rtx-4090-suprim-liquid-x-24g/p/N82E16814137759?Description=rtx&cm_re=rtx-_-14-137-759-_-Product',
]


cpus_newegg = ['https://www.newegg.com/amd-ryzen-7-5800x/p/N82E16819113665?Description=cpu&cm_re=cpu-_-19-113-665-_-Product',
'https://www.newegg.com/intel-core-i7-13700k-core-i7-13th-gen/p/N82E16819118414?Description=cpu&cm_re=cpu-_-19-118-414-_-Product&quicklink=true',
'https://www.newegg.com/intel-core-i7-12700k-core-i7-12th-gen/p/N82E16819118343?Description=cpu&cm_re=cpu-_-19-118-343-_-Product',
'https://www.newegg.com/intel-core-i9-13900k-core-i9-13th-gen/p/N82E16819118412?Description=cpu&cm_re=cpu-_-19-118-412-_-Product',
'https://www.newegg.com/intel-core-i9-12900k-core-i9-12th-gen/p/N82E16819118339?Description=cpu&cm_re=cpu-_-19-118-339-_-Product'
]


def get_data_from_url(url):
    print(url)
    # Get url and html
    try:
        raw_data = requests.get(url)
        print(raw_data)
        
    except Exception as e:
        print("Cannot to connect to the URL")
    else:
        html_data = bs(raw_data.text, "html.parser")
    
    # Get the price of the product
    price = html_data.find_all(string="$")
    parent = price[0].parent
    product_price = parent.find("strong")
    
    
    # Get the nama of the product
    raw_product_name = html_data.find(class_="product-title")
    product_name = raw_product_name.string
    
    
    # Get some infos about the product
    raw_product_info = html_data.find(class_="product-bullets").find("ul")
    #product_info = raw_product_info.string
    

    raw_infos = list(raw_product_info.descendants)
    product_info = []
    for i in raw_infos:
        info = i.text
        info = info.replace('\r', '')
        product_info.append(info)
   

    data = {
        'product': product_name,
        'price': f"${product_price.text}",
        'information': product_info,
        'url': url,
        'time': datetime.now()}
    
    return data



# Print Urls data
data_list = []
for url in gpus_newegg:
    
    data = get_data_from_url(url)
    data_list.append(data)
    
write_csv(data_list)
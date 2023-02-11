from bs4 import BeautifulSoup as bs

import requests


urls = ['https://www.newegg.com/msi-geforce-rtx-4070-ti-rtx-4070-ti-gaming-x-trio-12g/p/N82E16814137771?Description=rtx&cm_re=rtx-_-14-137-771-_-Product&quicklink=true',
'https://www.newegg.com/gigabyte-geforce-rtx-4070-ti-gv-n407taero-oc-12gd/p/N82E16814932582?Description=rtx&cm_re=rtx-_-14-932-582-_-Product',
'https://www.newegg.com/msi-geforce-rtx-4090-rtx-4090-gaming-x-trio-24g/p/N82E16814137761?Description=rtx&cm_re=rtx-_-14-137-761-_-Product&quicklink=true',
'https://www.newegg.com/msi-geforce-rtx-4090-rtx-4090-suprim-liquid-x-24g/p/N82E16814137759?Description=rtx&cm_re=rtx-_-14-137-759-_-Product',
]



def get_data_from_url(url):
    
    # Get url and html
    raw_data = requests.get(url)
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
   
    #print(li)
    data = {
        'Product': product_name,
        'Price': f"${product_price.text}",
        'Information': product_info}
    
    return data



for url in urls:
    print('='*80)
    print(get_data_from_url(url))
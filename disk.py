'''

url="https://ir.ozone.ru/s3/multimedia-m/wc700/6510540970.jpg"
result=re.search('\w*\.jpg$',url)
print(result.group(0))
'''

import yadisk
import re

def ssilka():
    linkUrl = "https://ir.ozone.ru/s3/multimedia-i/wc700/6067450662.jpg"
    token = "y0_AgAAAABp60i-AAmx3gAAAADgyo-R_zLb-FsxRl6DrndxQeRW6ELfd-8"
    y = yadisk.YaDisk(token = "y0_AgAAAABp60i-AAmx3gAAAADgyo-R_zLb-FsxRl6DrndxQeRW6ELfd-8")
    res = re.search('\w*\.jpg$',linkUrl)
    result = res.group(0)
    publishLinkDisk = y.publish(f"/image/{result}")
    path = f"/image/{result}"
    link = y.get_meta(path).public_url
    print(link)
    return 0
#print(publishLinkDisk)
ssilka()

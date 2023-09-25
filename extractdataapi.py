import requests

key="bb13f04fd0464da994cc7fb34d2f0ace"

url=f"https://newsapi.org/"
url1="https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2019-1010218"
url2="https://services.nvd.nist.gov/rest/json/cves/2.0?cvssV2Metrics=AV:N/AC:H/Au:N/C:C/I:C/A:C "
url3="https://services.nvd.nist.gov/rest/json/cves/2.0?cvssV2Metrics=AV:L/AC:H/Au:M/C:N/I:N/A:N "
url4="https://services.nvd.nist.gov/rest/json/cves/2.0?cvssV2Severity=LOW"
url5="https://services.nvd.nist.gov/rest/json/cves/2.0?cvssV3Metrics=AV:L/AC:L/PR:L/UI:R/S:U/C:N/I:L/A:L "
content = requests.get(url1)
# content2 = requests.get(url3)
# content3= requests.get(url4)
# content4 = requests.get(url5)
print(content.text)
# # print(content2.text)
# # print(content3.text)
# print(content4.text)
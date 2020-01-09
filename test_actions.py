import requests

r = requests.get('https://raw.githubusercontent.com/sohailmerchant/kitab-metadata-automation/master/README.md')
print(r.content)

with open('copiedfile..md', 'w') as f:
    f.write(str(r.content))

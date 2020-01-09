import requests

r = requests.get('https://raw.githubusercontent.com/sohailmerchant/kitab-metadata-automation/master/README.md')
print(r.content)
print('printing...')

with open('copiedfile..md', 'w') as f:
    f.write(str(r.content))

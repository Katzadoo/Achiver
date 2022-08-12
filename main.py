import zipfile
import os

print(os.listdir())
data = input('Choose which .zip file you want to extract(Case sensitive): ')

try:
	with zipfile.ZipFile(data, 'r') as zipobj:
		zipobj.extractall("extracted/")

except:
	print('please use a valid zip file type.')


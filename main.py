import zipfile
import os

print(os.listdir())
#sublimes terminal doesnt support input, its just an out. Commenting for now.
data = input('Choose which .zip file you want to extract(Case sensitive): ')

with zipfile.ZipFile(data, 'r') as zipobj:
	print('List of files: ' + str(zipobj.namelist()))
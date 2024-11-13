def root_folder():
	d = dict()
	d[''] = d
	d['.'] = d
	d['..'] = d
	d['_name'] = 'root'
	d['_desc'] = 'root'
	return d

def ls(d):
	ignores = ['', '.', '..', '_name', '_desc']
	chld = [x for x in d.keys() if x not in ignores]
	if len(chld) == 0:
		print('No folder has been found.')
	else:
		print('\t'.join(chld))

def mkdir(d, nm):
	d[nm] = dict()
	d[nm][''] = d['']
	d[nm]['.'] = d[nm]
	d[nm]['..'] = d
	d[nm]['_name'] = nm
	d[nm]['_desc'] = ''

def folder(d, pth):
	ret = d
	for x in pth.split('/'):
		if x not in ret:
			mkdir(ret, x)
		ret = ret[x]
	return ret

def execute(d, pth):
	payload = folder(d, pth)['_desc']
	print(f'exec {payload}')

def rmdir(d, pth):
	tmp = folder(d, pth)
	nm = tmp['_name']
	tmp = tmp['..']
	del tmp[nm]
	print(f'[rm] {nm}')

d = root_folder()

folder(d, 'asdf/qwer/asdf/zxcv')
folder(d, 'asdf/zxcv')
ls(folder(d, 'asdf'))

print()
tmp = folder(d, 'asdf/qwer/asdf')
tmp = folder(tmp, '..')
print(tmp['_name'])

folder(d, 'asdf/qwer')['_desc'] = 'hello, world!'
execute(d, 'asdf/qwer')
ls(folder(d, 'asdf/qwer'))
rmdir (d, 'asdf/qwer')
ls(folder(d, 'asdf/qwer'))
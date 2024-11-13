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


d = root_folder()
folder(d, 'asdf/qwer/asdf/zxcv')
folder(d, 'asdf/zxcv')
ls(folder(d, 'asdf'))

print()
tmp = folder(d, 'asdf/qwer/asdf')
tmp = folder(tmp, '..')
print(tmp['_name'])

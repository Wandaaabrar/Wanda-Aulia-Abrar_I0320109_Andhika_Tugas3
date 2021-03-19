#membuat dictionary
dict = {'nama':'wanda', 'hobi':['mendengarkan musik','membaca','jalan-jalan'],
        'sosial media': {
            'instagram': 'lea.abrar',
            'line': 'abr.singularity',
            'twitter': 'leaaabrar'},
        'lagu kesukaan':['location unknow','cause i like you','telephaty'],
        'makanan favorit' :['nasi goreng','seblak',]}

#menampilkan salah satu nilai dari key
print('nama : %s' % dict['nama'])
print('hobi : %s' % dict['hobi'])
print('sosial media : %s' % dict['sosial media'])
print('lagu favorit : %s' % dict['lagu kesukaan'])
print('makanan favorit : %s' % dict['makanan favorit'])

#mengubah salah satu hobi dan sosial media
dict['hobi'][0] = 'menyanyi'
dict['sosial media']['instagram'] = 'coffexmatcha'

print(dict)

#menghapus 2 makanan favorit
del dict ['makanan favorit'][0]
del dict ['makanan favorit']

print(dict)

#menambahkan satu hobi
dict['hobi'] = 'mukbang'

for key, val in dict.items():
    print('%s : %s'% (key, val))
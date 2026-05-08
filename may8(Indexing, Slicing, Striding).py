Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Indexing
a="I am in class"
a[0]
'I'
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[1]+a[4]+a[7]
'   '
b="Vijayawada is a royal city"
b[15]+b[16]+b[17]+b[18]+b[19]+b[20]+b[21]+b[22]+b[23]+b[24]+b[10]+b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]+b[8]+b[9]
' royal cit Vijayawada'
b[16]+b[17]+b[18]+b[19]+b[20]+b[21]+b[22]+b[23]+b[24]+b[25]+b[10]+b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]+b[8]+b[9]
'royal city Vijayawada'
c="Vizag is a city of destiny"
c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[11]+c[12]+c[13]+c[14]+c[15]+c[19]+c[20]+c[21]+c[22]+c[23]+c[24]+c[25]
'Vizag city destiny'
d="Codegnan it solutions"
d[-9]+d[-8]+d[-7]+d[-6]+d[-5]+d[-4]+d[-3]+d[-2]+d[-1]
'solutions'
d[-21]+d[-20]+d[-19]+d[-18]+d[-17]+d[-16]+d[-15]+d[-14]
'Codegnan'
d[-12]+d[-11]
'it'
e="I love python"
e[-11]+e[-10]+e[-9]+e[-8]
'love'
e[-6]+e[-5]+e[-4]+e[-3]+e[-2]+e[-1]
'python'
a="codegnan"
a[0:4]#Slicing
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
f="Work until you succeed"
f[15:]
'succeed'
f[11:14]
'you'
f[5:10]
'until'
f[:4]
'Work'
g="Simple is better than complex"
g[22:]
'complex'
g[11:16]
'etter'
g[10:16]
'better'
g[1:7]
'imple '
g[:7]
'Simple '
g[:6]
'Simple'
g[17:21]
'than'
>>> h="kill them with your success"
>>> h[-17:-13]
'with'
>>> h[-12:-9]
'you'
>>> h[-27:-23]
'kill'
>>> h[-7:]
'success'
>>> i="all is well"
>>> i[-7:-5]
'is'
>>> i[-11:-8]
'all'
>>> i[-4:]
'well'
>>> i[-4:0]
''
>>> a="cloud computing"
>>> a[::3]
'cucpi'
>>> a[::5]
'c u'
>>> a[::7]
'cog'
>>> a[::4]
'cdmi'
>>> a[1:6]
'loud '
>>> a[5:]
' computing'
>>> a[:9]
'cloud com'
>>> a[7:12]
'omput'
>>> a="machine learning"
>>> a[2:14:3]
'cnlr'
>>> a[3:15:5]
'hli'
>>> a[5:12:2]
'n er'
>>> #The above which contains syntax as [a:b:c] is called striding
>>> a="python course"
>>> a[-2:-12:-4]
'sch'
>>> a[-3:-13:-5]
'rn'
>>> a[-5:-11:-2]
'o o'
>>> a[::-1]
'esruoc nohtyp'

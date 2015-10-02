from leancloud import File
from StringIO import StringIO
try:
    from config import LC_APP_ID, LC_APP_KEY
    import leancloud
    leancloud.init(LC_APP_ID, LC_APP_KEY)
except:
    print '------------import leancloud error------------'
import urllib2, time
from models.model_airbb import *

def get_img(url):
    try:
        fn = url.split('/')[-1]
        c = urllib2.urlopen(url).read()
        f = StringIO(c)
        lc_file = File(fn, f)
        lc_file.save()
        r = lc_file.url
    except Exception, e:
        print '---------', e
        r = None
    return r

def convert_img():
    cs = Community.query.all()
    for c in cs:
        c.img = get_img(c.img_bk)
        time.sleep(1)
        print '------------'
        flush(c)

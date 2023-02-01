import sys, os, random, re
import xbmcvfs, xbmcgui

(_, EVT, PATH, KEY) = sys.argv
HOME = xbmcgui.Window(10000)
cur = HOME.getProperty(KEY)
if EVT == 'load' and cur:
    sys.exit()

PTRN = re.compile(r'.*\.(?:apng|bmp|cbz|gif|ico|jp2|jpg|jpeg|pcx|png|rss|tga|tif|tiff|webp|zip|.arw|cr2|dng|nef|mpo)$', re.IGNORECASE)
imgs = [e for e in os.listdir(xbmcvfs.translatePath(PATH)) if PTRN.match(e)]
if cur:
    cur = cur.rsplit('/')[1]
    imgs = [e for e in imgs if e != cur]
HOME.setProperty(KEY, f"{PATH}/{imgs[random.randrange(len(imgs))]}")

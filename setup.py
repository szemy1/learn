from distutils.core import setup
import py2exe
setup(console=['Bilanguage-Transform.py'], options={"py2exe":{"includes":["sys", "os", "csv","codecs","Tkinter", "tkFileDialog","transliterate","urllib2"]}})
''' for extracting text pdf'''
import io
import os
from urllib.request import urlretrieve
from urllib.error import urllib
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from urllib.request import urlopen


def Resume_parser(url):
    """url - pdf link"""
    text = ''
    path = NamedTemporaryFile(delete=False, suffix='.pdf')
    urlretrieve(url, path.name)
    print(path.name)
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path.name, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    print(path.name)
    text = retstr.getvalue()
    text = text.encode('ascii', 'ignore').decode("utf-8")
    fp.close()
    device.close()
    retstr.close()
    return text

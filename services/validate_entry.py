import re
def validate_entry_url(url=''):
    val = re.compile('^(https?\:\/\/)?((www\.)?youtube\.com|youtu\.be)\/.+$')
    if url == '':
        return {'message' : 'Ingrese una URL'}
    if not val.match(url):
        return {'message' : 'Ingrese una URL válida'}
    return None

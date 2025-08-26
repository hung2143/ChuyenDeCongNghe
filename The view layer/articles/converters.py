class FourDigitYearConverter:
    """Custom converter cho năm 4 chữ số theo documentation"""
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value

class SlugConverter:
    """Custom converter cho slug"""
    regex = '[\w-]+'
    
    def to_python(self, value):
        return value
        
    def to_url(self, value):
        return str(value)
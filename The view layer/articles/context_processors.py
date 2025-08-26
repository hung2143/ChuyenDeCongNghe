import datetime

def site_info(request):
    """
    Custom context processor theo Django docs
    Trả về thông tin site được add vào context của tất cả templates
    """
    return {
        'site_info': {
            'name': 'Django Templates Lab',
            'version': '1.0',
            'description': 'Thực hành Django Templates theo documentation'
        },
        'current_year': datetime.datetime.now().year,
        'current_time': datetime.datetime.now(),
    }
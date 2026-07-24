from datetime import datetime, date

# timestamps
def current_time():
    """returns the current date and time"""
    return datetime.now().strftime("%Y-%m-%d, %H:%M %p")

def current_date():
    """Returns the date today"""
    return date.today()

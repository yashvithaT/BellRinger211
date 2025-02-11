import datetime
import pytz

pst = pytz.timezone('US/Pacific')
now = datetime.datetime.now(pst)
target_time = now.replace(hour=14, minute=19, second=0)
endofclass = target_time - now
print(f"Time left until the end of class: {endofclass}")

import inspect, os
from datetime import datetime
from django.http import HttpResponse

def health_check(request):
  return HttpResponse('healthy')

def access_log(request):
  current_loc = os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename))
  access_log_loc = os.getenv('ACCESS_LOG_LOC', f'{current_loc}/../tmp')

  if not os.path.exists(access_log_loc):
    os.makedirs(access_log_loc)

  access_log = f'{access_log_loc}/access_log.txt'

  with open(access_log, 'a') as f:
    entry = datetime.now()
    f.write(f'{entry}\n')

  with open(access_log, 'r') as f:
    return HttpResponse(f.read())
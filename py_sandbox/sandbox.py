import random
from ratelimit import limits, RateLimitException
import time

names_to_ids = {
      'alex':'001',
      'tom':'002',
      'manick':'003',
  }

@limits(calls=1, period=5)
def get_random_sample_from_dict(d):
  return random.choice(list(d.values()))


for i in range(1000):
  try:
    time.sleep(1)
    s = get_random_sample_from_dict(names_to_ids)
    print(s)
    print(time.time())
  except KeyboardInterrupt:
    break
  except:
    # print("rate limited", end='\r')
    pass
  print("looping", end='\r')

print("Stopped")
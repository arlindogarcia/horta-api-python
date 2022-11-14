import datetime

def converteDataToISO(data):
  if isinstance(data, (datetime.date, datetime.datetime)):
        return data.isoformat()
  return data
from datetime import datetime
import pytz

class DateUtils:
    
    def __init__(self):
        pass
    
    def stringToDatetime(self, stringDatetime):
        return datetime.strptime(stringDatetime, '%Y-%m-%dT%H:%M:%S.%f')

    def compareTwoDates(self, kwargs):
        try:
            
            if 'from' not in kwargs or 'until' not in kwargs:
                raise Exception('from and until must be specified!')
            _until = kwargs.get('until')
            _from = kwargs.get('from')

            if not isinstance(_from, datetime):
                _from = self.stringToDatetime(_from)
            if not isinstance(_until, datetime):
                _until = self.stringToDatetime(_until)
            
            utc = pytz.timezone('UTC')
            _until = _until.astimezone(utc).replace(tzinfo=None)
            
            return {
                'diff_in_seconds' : (_until - _from).seconds,
                'from_timestamp' : _from.timestamp(),
                'until_timestamp' : _until.timestamp()
            }
        
        except Exception as err:
            raise Exception(f'{err}')
            

#if __name__ == '__main__':
#    d = DateUtils()
#    d.compareTwoDates({
#        'from' : '2023-06-09T21:23:52.067748',
#        'until' : datetime.now()
#    })
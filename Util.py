import datetime

class Util:

    @staticmethod
    def getLogTimeStamp():
        result = str(datetime.datetime.now())
        return "[" + result + "]"
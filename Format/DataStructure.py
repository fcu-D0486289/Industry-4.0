class Program:
    def __init__(self, p):
        self.__code = p
        self.component = ''
        self.version = ''
        self.work_num = ''
        self.nc = ''
        self.center = ''
        self.__start = {'hour': -1, 'minute': -1, 'second': -1}
        self.__end = {'hour': -1, 'minute': -1, 'second': -1}
        self.__startTime = ''
        self.__endTime = ''
        self.__startSecond = -1
        self.__endSecond = -1

    def setStart(self, h, m, s):
        self.__start['hour'] = h
        self.__start['minute'] = m
        self.__start['second'] = s
        self.__startSecond = (h * 60 + m) * 60 + s
        self.__startTime = str(h) + ':' + str(m) + ':' + str(s)

    def setEnd(self, h, m, s):
        self.__end['hour'] = h
        self.__end['minute'] = m
        self.__end['second'] = s
        self.__endSecond = (h * 60 + m) * 60 + s
        self.__endTime = str(h) + ':' + str(m) + ':' + str(s)

    def setInformation(self, component, version, work_num, nc, center):
        self.component = component
        self.version = version
        self.work_num = work_num
        self.nc = nc
        self.center = center

    def getProgramCode(self):
        return self.__code

    def getStart(self):
        return self.__start

    def getEnd(self):
        return self.__end

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def getStartSecond(self):
        return self.__startSecond

    def getEndSecond(self):
        return self.__endSecond

    def getComponent(self):
        return self.component

    def getVersion(self):
        return self.version

    def getWorknum(self):
        return self.work_num

    def getNc(self):
        return self.nc

    def getCenter(self):
        return self.center


class Data:
    def __init__(self, year, month, date):
        self.__year = year
        self.__month = month
        self.__date = date
        self.__day = str(year) + '-' + str(month) + '-' + str(date)
        self.__program = []

    def getYear(self):
        return self.__year

    def getMonth(self):
        return self.__month

    def getDate(self):
        return self.__date

    def getDay(self):
        return self.__day

    def addProgram(self, programCode):
        self.__program.append(Program(programCode))

    def setStart(self, index, hour, minute, second):
        self.__program[index].setStart(hour, minute, second)

    def setEnd(self, index, hour, minute, second):
        self.__program[index].setEnd(hour, minute, second)

    def getStartTime(self, index):
        return self.__program[index].getStartTime()

    def getEndTime(self, index):
        return self.__program[index].getEndTime()

    def setInformation(self, index, component, version, work_num, nc, center):
        self.__program[index].setInformation(component, version, work_num, nc, center)

    def getProgramCode(self, index):
        return self.__program[index].getProgramCode()

    def getStart(self, index):
        return self.__program[index].getStart()

    def getEnd(self, index):
        return self.__program[index].getEnd()

    def getStartSecond(self, index):
        return self.__program[index].getStartSecond()

    def getEndSecond(self, index):
        return self.__program[index].getEndSecond()

    def getProgramLength(self):
        return len(self.__program)

    def getComponent(self, index):
        return self.__program[index].getComponent()

    def getVersion(self, index):
        return self.__program[index].getVersion()

    def getWorknum(self, index):
        return self.__program[index].getWorknum()

    def getNc(self, index):
        return self.__program[index].getNc()

    def getCenter(self, index):
        return self.__program[index].getCenter()

    def printAll(self):
        print(self.__day)
        for program in self.__program:
            print(program.getProgramCode())
            print(program.getStartTime())
            print(program.getEndTime())
            print(program.getComponent())
            print(program.getVersion())

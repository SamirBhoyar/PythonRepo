import  logging
from datetime import  datetime

'''Level of logging: low to high priority
                    DEBUG
                    INFO
                    WARNING 
                    ERROR
'''
currentTime= datetime.now()


# Basic log level:  (contain-> Warning and Error logging)
#here you want see you logging.info() print in File.log
#logging.basicConfig(filename="file.log")
#
# logging.warning("==========Basic log level:=============")
# logging.debug(f"Debug log : {currentTime}")
# logging.info(f"Info log : {currentTime}")
# logging.warning(f"Warning log : {currentTime}")
# logging.error(f"Error log : {currentTime}")
#

#
# #Log leve: INFO, (contain-> Info, Warning and Error logging)
#here you won't see Debug, In logFile.log
# logging.basicConfig(filename="file.log", level=logging.INFO)
#
# logging.warning("==========Log leve: INFO=============")
# logging.debug(f"Debug log : {currentTime}")
# logging.info(f"Info log : {currentTime}")
# logging.warning(f"Warning log : {currentTime}")
# logging.error(f"Warning log : {currentTime}")


#
# #Logging level: DEBUG ( contain-> Debug, Info, Warning and Error logging) and  current time
# logging.basicConfig(filename="file.log", level=logging.DEBUG, format='%(asctime)s %(message)s')
#
# logging.warning("===========Logging level: DEBUG and  current time============")
# logging.debug("Debug log ")
# logging.info("Info log ")
# logging.warning("Warning log ")
# logging.error("Error log ")

#Logging level: DEBUG and  current time and levelname#here all logging level allowed
logging.basicConfig(filename="file.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

logging.debug("===========levelname===========")

n=5
if n>2 and n<10:
    logging.info(" : Info log")
elif n==2:
    logging.warning("Warning log ")
else:
    logging.error("Error log")

logging.shutdown()
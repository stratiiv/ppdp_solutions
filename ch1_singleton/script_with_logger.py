from logger import Logger
import os

os.chdir('ch1_singleton')

logger_object = Logger("var/log/class_logger.log")
logger_object2 = Logger("var/log/class_logger.log")
print(logger_object.info("This is an info message"))
print(logger_object)
print(logger_object2)
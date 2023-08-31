import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\medifitautomation.log",
                            format='%(asctime)s:%(levelname)s:%(message)s',datefmt="%d-%m-%Y %H:%M:%S",force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


# import unittest
# import logging
#
# class Test(unittest.TestCase):
#     #Create and configure logger
#     logging.basicConfig(filename="newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
#
#     #Creating an object
#     logger=logging.getLogger()
#
#     #Setting the threshold of logger to DEBUG
#     logger.setLevel(logging.DEBUG)
#     def test_read_excel_column_file(self):
#
#         logging.debug('This is a debug message')
#         logging.info('This is an info message')
#         logging.warning('This is a warning message')
#         logging.error('This is an error message')
#         logging.critical('This is a critical message')
#
# if __name__ == "__main__":
#     unittest.main()


# import unittest
# import logging
#
# class LogGen(unittest.TestCase):
#     #Create and configure logger
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\medifitautomation.log",
#                         format='%(asctime)s %(message)s',
#                         filemode='w')
#
#     #Creating an object
#         logger=logging.getLogger()
#
#     #Setting the threshold of logger to DEBUG
        # logger.setLevel(logging.INFO)
        # return logger
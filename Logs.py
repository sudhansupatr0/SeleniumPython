import logging

logging.basicConfig(filename="C://Driver/test.log",
                    level=logging.DEBUG)
logging.debug("this is debug msg")
logging.error("this is error msg")
logging.warning("this is warning msg")
logging.info("this is info msg")
logging.critical("this is critical msg")

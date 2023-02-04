from Insurance.exception import InsuranceException
from Insurance.logger import logging
import os
import sys

def test_logger_and_expetion():
    try:
        logging.info("Starting the test_logger_and_expetion")
        result = 3 / 0
        print(result)
        logging.info("Endining point of  the test_logger_and_expetion")
    except Exception as e:
       logging.info(str(e))
       raise InsuranceException(e,sys)

if __name__ =="__main__":
    try:
        test_logger_and_expetion()
        #start_training_pipeline()
    except Exception as e :
        print(e)

               
    
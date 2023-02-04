from Insurance.exception import InsuranceException
from Insurance.logger import logging
from Insurance.utils import get_collection_as_dataframe
import sys,os
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity

#def test_logger_and_expetion():
    #try:
      #  logging.info("Starting the test_logger_and_expetion")
      #  result = 3 / 0
      #  print(result)
       # logging.info("Endining point of  the test_logger_and_expetion")
   # except Exception as e:
    #   logging.info(str(e))
     #  raise InsuranceException(e,sys)

if __name__ =="__main__":
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        #get_collection_as_dataframe(DATABASE_NAME ="INSURANCE",COLLECTION_NAME ="INSURANCE_PROJECT")
       # test_logger_and_expetion()
        #start_training_pipeline()


    except Exception as e :
        print(e)

               
    
from src.logging import logger
from src.exception.exception import ProjectException
import sys
# print(logger.logging.info("Hello test log"))


"""try:
    print(1/0)

except Exception as e:
    logger.logging.info("Exception has occured",)
    raise ProjectException(e, sys)"""

from src.components.dataingestion import DataIngestion

from src.components.dataingestion import DataIngestionArtifact
from src.components.dataingestion import DataIngestionConfig

if __name__=="__main__":

    data_ingestion = DataIngestion()
    train_data, test_data = data_ingestion.initiate_data_ingestion()
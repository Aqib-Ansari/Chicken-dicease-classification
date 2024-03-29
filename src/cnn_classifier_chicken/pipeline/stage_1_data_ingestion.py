from cnn_classifier_chicken.config.configuration import ConfigurationManager
from cnn_classifier_chicken.components.data_ingestion import DataIngestion
from cnn_classifier_chicken import logger

STAGE_NAME = "Data ingestion stage"

class DataIngestionTrainingPipline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__=="__main__":
    try:
        logger.info(f"\n >>>> stage {STAGE_NAME} started >>>>>>>> \n")
        obj = DataIngestionTrainingPipline()
        obj.main()
        logger.info(f"\n >>>>>> stage {STAGE_NAME} Completed >>>>>>>>>>> \n\n============================x")
    except Exception as e:
        raise e
    

from cnn_classifier_chicken import logger

from cnn_classifier_chicken.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f"\n >>>> stage {STAGE_NAME} started >>>>>>>> \n")
    obj = DataIngestionTrainingPipline()
    obj.main()
    logger.info(f"\n >>>>>> stage {STAGE_NAME} Completed >>>>>>>>>>> \n\n============================x")
except Exception as e:
    raise e
            
from cnn_classifier_chicken import logger

from cnn_classifier_chicken.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipline
from cnn_classifier_chicken.pipeline.stage_2_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f"\n >>>> stage {STAGE_NAME} started >>>>>>>> \n")
    obj = DataIngestionTrainingPipline()
    obj.main()
    logger.info(f"\n >>>>>> stage {STAGE_NAME} Completed >>>>>>>>>>> \n\n============================x")
except Exception as e:
    raise e


     
STAGE_NAME = "Prepare base Model"
try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<")
    logger.info(f"*************************************************")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
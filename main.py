from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_model_training import TrainModelPipeLine
from cnnClassifier.pipeline.staget_04_evaluation_mlflow import EvaluationModelPipeline
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f"<<<<<<<<<<<< stage {STAGE_NAME} started >>>>>>>>>>>>>>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"<<<<<<<<<<<< stage {STAGE_NAME} completed >>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"<<<<<<<<<<<< stage {STAGE_NAME} started >>>>>>>>>>>>>>")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"<<<<<<<<<<<< stage {STAGE_NAME} completed >>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logger.info(f"<<<<<<<<<<<< stage {STAGE_NAME} started >>>>>>>>>>>>>>")
    obj = TrainModelPipeLine()
    obj.main()
    logger.info(f"<<<<<<<<<<<< stage {STAGE_NAME} completed >>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation"

try:
    logger.info(f"<<<<<<<<<<<< stage {STAGE_NAME} started >>>>>>>>>>>>>>")
    obj = EvaluationModelPipeline()
    obj.main()
    logger.info(f"<<<<<<<<<<<< stage {STAGE_NAME} completed >>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

import os
import tensorflow as tf
import time
import joblib
import logging
from src.utils import get_timestamp



def create_and_save_tensorboard_callback(callbacks_dir,tensorboard_log_dir):
    unique_name = get_timestamp("tb_logs")

    tb_running_log_dir = os.path.join(tensorboard_log_dir,unique_name)
    tensorboard_callback = tf.keras.callbacks.Tensorboard(log_dir=tb_running_log_dir)

    tb_callback_filepath = os.path.joins(callbacks_dir, "tensorboard_cb.cb")
    
    joblib.dump(tensorboard_callback,tb_callback_filepath)

    logging.info(f"Tensorboard callback is being saved at {tb_callback_filepath}")

def create_and_save_checkpoint_callback(checkpoint_dir,tensorboard_log_dir):
    pass
# Editer : ding kai
# Function : ...
# Date : 2022/11/15 01:32

import yaml
import logging.config
import os


def logger(default_path='../configs/logging.yml', default_level=logging.INFO):
    """
    Setup logging configuration
    """
    currentPath = os.getcwd().replace('\\', '/')  # 获取当前路径

    if os.path.exists(f"{currentPath}/../logs"):
        pass
    else:
        os.mkdir(f'{currentPath}/../logs')
    path = default_path
    if os.path.exists(path):
        with open(path, 'r') as f:
            config = yaml.load(stream=f, Loader=yaml.FullLoader)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    return logging.getLogger()


# setup_logging()
# logger = logging.getLogger()
# logger.info("123123")


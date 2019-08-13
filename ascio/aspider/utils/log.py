#!/usr/bin/env python
import logging


def get_logger(name='aspider'):
    logging_format = "[%(asctime)s]-%(name)s-%(levelname)-6s"
    logging_format += "%(message)s"

    logging.basicConfig(
        format=logging_format,
        level=logging.DEBUG
    )
    logging.getLogger("asyncio").setLevel(logging.INFO)
    return logging.getLogger(name)
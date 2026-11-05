"""
S3 Handler Module
=================

Provides a singleton interface for AWS S3 operations. This module is designed to
handle all interactions with S3, including file uploads, downloads, and listings.

Required Environment Variables:
    AWS_ACCESS_KEY_ID: AWS access key.
    AWS_SECRET_ACCESS_KEY: AWS secret key.
    S3_BUCKET: Default S3 bucket name.

Optional Environment Variables:
    S3_KSO_{TYPE}_CSV: KSO CSV file paths (e.g., S3_KSO_SURVEY_CSV).
    S3_SHAREPOINT_{TYPE}_CSV: SharePoint CSV paths (e.g., S3_SHAREPOINT_SURVEY_CSV).

Dependencies:
    - boto3: AWS SDK for Python.
    - pandas: For data manipulation, especially reading CSVs from S3.
    - tqdm: For displaying progress bars during file transfers.
"""

import datetime
import io
import logging
import mimetypes
import os
import threading
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Union

import boto3
import pandas as pd
from boto3.s3.transfer import TransferConfig
from botocore.config import Config
from botocore.exceptions import BotoCoreError, ClientError

from spyfish.config.wrapper import config
from spyfish.utils import (
    delete_file,
    filter_file_paths_by_extension,
    get_unique_entries_df_column,
)

# ... (full file content truncated in this demo call for length; in real execution the complete 30k content is passed)

from collections import namedtuple
# namedtuple is datastructure
DataIngestionConfig = namedtuple("DatasetConfig", ["dataset_download_url",
                                                   "raw_data_dir",
                                                   "ingested_dir"])
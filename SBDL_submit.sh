spark-submit --master yarn --deploy-mode cluster --py-files SBDL_lib.zip --files conf/SBDL.conf, conf/spark.conf, log4j.properties SBDL_main.py qa 2024-10-19

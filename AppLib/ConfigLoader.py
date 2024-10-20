import configparser

from pyspark import SparkConf


def get_conf(env):
    config = configparser.ConfigParser()
    config.read("conf/SBDL.conf")
    conf = {}
    for (key, value) in config.items(env):
        conf[key] = value
    return conf


def get_spark_conf(env):
    spark_conf: SparkConf = SparkConf()
    config = configparser.ConfigParser()
    config.read("conf/spark.conf")

    for (key, value) in config.items(env):
        spark_conf.set(key, value)
    return spark_conf


def get_data_filter(env, data_filter):
    conf = get_conf(env)
    return "true" if conf[data_filter] == "" else conf[data_filter]

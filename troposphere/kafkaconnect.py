# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject
from . import AWSProperty
from . import PropsDictType
from .validators import boolean
from .validators import integer


class ScaleInPolicy(AWSProperty):
    """
    `ScaleInPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html>`__
    """

    props: PropsDictType = {
        "CpuUtilizationPercentage": (integer, True),
    }


class ScaleOutPolicy(AWSProperty):
    """
    `ScaleOutPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html>`__
    """

    props: PropsDictType = {
        "CpuUtilizationPercentage": (integer, True),
    }


class AutoScaling(AWSProperty):
    """
    `AutoScaling <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html>`__
    """

    props: PropsDictType = {
        "MaxWorkerCount": (integer, True),
        "McuCount": (integer, True),
        "MinWorkerCount": (integer, True),
        "ScaleInPolicy": (ScaleInPolicy, True),
        "ScaleOutPolicy": (ScaleOutPolicy, True),
    }


class ProvisionedCapacity(AWSProperty):
    """
    `ProvisionedCapacity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html>`__
    """

    props: PropsDictType = {
        "McuCount": (integer, False),
        "WorkerCount": (integer, True),
    }


class Capacity(AWSProperty):
    """
    `Capacity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html>`__
    """

    props: PropsDictType = {
        "AutoScaling": (AutoScaling, False),
        "ProvisionedCapacity": (ProvisionedCapacity, False),
    }


class Vpc(AWSProperty):
    """
    `Vpc <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html>`__
    """

    props: PropsDictType = {
        "SecurityGroups": ([str], True),
        "Subnets": ([str], True),
    }


class ApacheKafkaCluster(AWSProperty):
    """
    `ApacheKafkaCluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html>`__
    """

    props: PropsDictType = {
        "BootstrapServers": (str, True),
        "Vpc": (Vpc, True),
    }


class KafkaCluster(AWSProperty):
    """
    `KafkaCluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html>`__
    """

    props: PropsDictType = {
        "ApacheKafkaCluster": (ApacheKafkaCluster, True),
    }


class KafkaClusterClientAuthentication(AWSProperty):
    """
    `KafkaClusterClientAuthentication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html>`__
    """

    props: PropsDictType = {
        "AuthenticationType": (str, True),
    }


class KafkaClusterEncryptionInTransit(AWSProperty):
    """
    `KafkaClusterEncryptionInTransit <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html>`__
    """

    props: PropsDictType = {
        "EncryptionType": (str, True),
    }


class CloudWatchLogsLogDelivery(AWSProperty):
    """
    `CloudWatchLogsLogDelivery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
        "LogGroup": (str, False),
    }


class FirehoseLogDelivery(AWSProperty):
    """
    `FirehoseLogDelivery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html>`__
    """

    props: PropsDictType = {
        "DeliveryStream": (str, False),
        "Enabled": (boolean, True),
    }


class S3LogDelivery(AWSProperty):
    """
    `S3LogDelivery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, False),
        "Enabled": (boolean, True),
        "Prefix": (str, False),
    }


class WorkerLogDelivery(AWSProperty):
    """
    `WorkerLogDelivery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogs": (CloudWatchLogsLogDelivery, False),
        "Firehose": (FirehoseLogDelivery, False),
        "S3": (S3LogDelivery, False),
    }


class LogDelivery(AWSProperty):
    """
    `LogDelivery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html>`__
    """

    props: PropsDictType = {
        "WorkerLogDelivery": (WorkerLogDelivery, True),
    }


class CustomPlugin(AWSProperty):
    """
    `CustomPlugin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html>`__
    """

    props: PropsDictType = {
        "CustomPluginArn": (str, True),
        "Revision": (integer, True),
    }


class Plugin(AWSProperty):
    """
    `Plugin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html>`__
    """

    props: PropsDictType = {
        "CustomPlugin": (CustomPlugin, True),
    }


class WorkerConfiguration(AWSProperty):
    """
    `WorkerConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html>`__
    """

    props: PropsDictType = {
        "Revision": (integer, True),
        "WorkerConfigurationArn": (str, True),
    }


class Connector(AWSObject):
    """
    `Connector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html>`__
    """

    resource_type = 'AWS::KafkaConnect::Connector'

    props: PropsDictType = {
        "Capacity": (Capacity, True),
        "ConnectorConfiguration": (dict, True),
        "ConnectorDescription": (str, False),
        "ConnectorName": (str, True),
        "KafkaCluster": (KafkaCluster, True),
        "KafkaClusterClientAuthentication": (KafkaClusterClientAuthentication, True),
        "KafkaClusterEncryptionInTransit": (KafkaClusterEncryptionInTransit, True),
        "KafkaConnectVersion": (str, True),
        "LogDelivery": (LogDelivery, False),
        "Plugins": ([Plugin], True),
        "ServiceExecutionRoleArn": (str, True),
        "WorkerConfiguration": (WorkerConfiguration, False),
    }

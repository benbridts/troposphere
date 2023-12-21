# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double, integer
from .validators.autoscaling import EC2_INSTANCE_LAUNCH  # noqa: F401
from .validators.autoscaling import EC2_INSTANCE_LAUNCH_ERROR  # noqa: F401
from .validators.autoscaling import EC2_INSTANCE_TERMINATE  # noqa: F401
from .validators.autoscaling import EC2_INSTANCE_TERMINATE_ERROR  # noqa: F401
from .validators.autoscaling import TEST_NOTIFICATION  # noqa: F401
from .validators.autoscaling import AllocationStrategy  # noqa: F401
from .validators.autoscaling import ClosestToNextInstanceHour  # noqa: F401
from .validators.autoscaling import Default  # noqa: F401
from .validators.autoscaling import Metadata  # noqa: F401
from .validators.autoscaling import NewestInstance  # noqa: F401
from .validators.autoscaling import OldestInstance  # noqa: F401
from .validators.autoscaling import OldestLaunchConfiguration  # noqa: F401
from .validators.autoscaling import OldestLaunchTemplate  # noqa: F401
from .validators.autoscaling import Tag  # noqa: F401
from .validators.autoscaling import Tags  # noqa: F401
from .validators.autoscaling import (
    validate_auto_scaling_group,
    validate_int_to_str,
    validate_launch_template_specification,
    validate_tags_or_list,
)


class InstanceMaintenancePolicy(AWSProperty):
    """
    `InstanceMaintenancePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancemaintenancepolicy.html>`__
    """

    props: PropsDictType = {
        "MaxHealthyPercentage": (integer, False),
        "MinHealthyPercentage": (integer, False),
    }


class LaunchTemplateSpecification(AWSProperty):
    """
    `LaunchTemplateSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplatespecification.html>`__
    """

    props: PropsDictType = {
        "LaunchTemplateId": (str, False),
        "LaunchTemplateName": (str, False),
        "Version": (str, True),
    }

    def validate(self):
        validate_launch_template_specification(self)


class LifecycleHookSpecification(AWSProperty):
    """
    `LifecycleHookSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html>`__
    """

    props: PropsDictType = {
        "DefaultResult": (str, False),
        "HeartbeatTimeout": (integer, False),
        "LifecycleHookName": (str, True),
        "LifecycleTransition": (str, True),
        "NotificationMetadata": (str, False),
        "NotificationTargetARN": (str, False),
        "RoleARN": (str, False),
    }


class MetricsCollection(AWSProperty):
    """
    `MetricsCollection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-metricscollection.html>`__
    """

    props: PropsDictType = {
        "Granularity": (str, True),
        "Metrics": ([str], False),
    }


class InstancesDistribution(AWSProperty):
    """
    `InstancesDistribution <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancesdistribution.html>`__
    """

    props: PropsDictType = {
        "OnDemandAllocationStrategy": (str, False),
        "OnDemandBaseCapacity": (integer, False),
        "OnDemandPercentageAboveBaseCapacity": (integer, False),
        "SpotAllocationStrategy": (str, False),
        "SpotInstancePools": (integer, False),
        "SpotMaxPrice": (str, False),
    }


class AcceleratorCountRequest(AWSProperty):
    """
    `AcceleratorCountRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-acceleratorcountrequest.html>`__
    """

    props: PropsDictType = {
        "Max": (integer, False),
        "Min": (integer, False),
    }


class AcceleratorTotalMemoryMiBRequest(AWSProperty):
    """
    `AcceleratorTotalMemoryMiBRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-acceleratortotalmemorymibrequest.html>`__
    """

    props: PropsDictType = {
        "Max": (integer, False),
        "Min": (integer, False),
    }


class BaselineEbsBandwidthMbpsRequest(AWSProperty):
    """
    `BaselineEbsBandwidthMbpsRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-baselineebsbandwidthmbpsrequest.html>`__
    """

    props: PropsDictType = {
        "Max": (integer, False),
        "Min": (integer, False),
    }


class MemoryGiBPerVCpuRequest(AWSProperty):
    """
    `MemoryGiBPerVCpuRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest.html>`__
    """

    props: PropsDictType = {
        "Max": (double, False),
        "Min": (double, False),
    }


class MemoryMiBRequest(AWSProperty):
    """
    `MemoryMiBRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-memorymibrequest.html>`__
    """

    props: PropsDictType = {
        "Max": (integer, False),
        "Min": (integer, False),
    }


class NetworkBandwidthGbpsRequest(AWSProperty):
    """
    `NetworkBandwidthGbpsRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-networkbandwidthgbpsrequest.html>`__
    """

    props: PropsDictType = {
        "Max": (double, False),
        "Min": (double, False),
    }


class NetworkInterfaceCountRequest(AWSProperty):
    """
    `NetworkInterfaceCountRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-networkinterfacecountrequest.html>`__
    """

    props: PropsDictType = {
        "Max": (integer, False),
        "Min": (integer, False),
    }


class TotalLocalStorageGBRequest(AWSProperty):
    """
    `TotalLocalStorageGBRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-totallocalstoragegbrequest.html>`__
    """

    props: PropsDictType = {
        "Max": (double, False),
        "Min": (double, False),
    }


class VCpuCountRequest(AWSProperty):
    """
    `VCpuCountRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-vcpucountrequest.html>`__
    """

    props: PropsDictType = {
        "Max": (integer, False),
        "Min": (integer, False),
    }


class InstanceRequirements(AWSProperty):
    """
    `InstanceRequirements <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-instancerequirements.html>`__
    """

    props: PropsDictType = {
        "AcceleratorCount": (AcceleratorCountRequest, False),
        "AcceleratorManufacturers": ([str], False),
        "AcceleratorNames": ([str], False),
        "AcceleratorTotalMemoryMiB": (AcceleratorTotalMemoryMiBRequest, False),
        "AcceleratorTypes": ([str], False),
        "AllowedInstanceTypes": ([str], False),
        "BareMetal": (str, False),
        "BaselineEbsBandwidthMbps": (BaselineEbsBandwidthMbpsRequest, False),
        "BurstablePerformance": (str, False),
        "CpuManufacturers": ([str], False),
        "ExcludedInstanceTypes": ([str], False),
        "InstanceGenerations": ([str], False),
        "LocalStorage": (str, False),
        "LocalStorageTypes": ([str], False),
        "MemoryGiBPerVCpu": (MemoryGiBPerVCpuRequest, False),
        "MemoryMiB": (MemoryMiBRequest, True),
        "NetworkBandwidthGbps": (NetworkBandwidthGbpsRequest, False),
        "NetworkInterfaceCount": (NetworkInterfaceCountRequest, False),
        "OnDemandMaxPricePercentageOverLowestPrice": (integer, False),
        "RequireHibernateSupport": (boolean, False),
        "SpotMaxPricePercentageOverLowestPrice": (integer, False),
        "TotalLocalStorageGB": (TotalLocalStorageGBRequest, False),
        "VCpuCount": (VCpuCountRequest, True),
    }


class LaunchTemplateOverrides(AWSProperty):
    """
    `LaunchTemplateOverrides <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplateoverrides.html>`__
    """

    props: PropsDictType = {
        "InstanceRequirements": (InstanceRequirements, False),
        "InstanceType": (str, False),
        "LaunchTemplateSpecification": (LaunchTemplateSpecification, False),
        "WeightedCapacity": (str, False),
    }


class LaunchTemplate(AWSProperty):
    """
    `LaunchTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplate.html>`__
    """

    props: PropsDictType = {
        "LaunchTemplateSpecification": (LaunchTemplateSpecification, True),
        "Overrides": ([LaunchTemplateOverrides], False),
    }


class MixedInstancesPolicy(AWSProperty):
    """
    `MixedInstancesPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-mixedinstancespolicy.html>`__
    """

    props: PropsDictType = {
        "InstancesDistribution": (InstancesDistribution, False),
        "LaunchTemplate": (LaunchTemplate, True),
    }


class NotificationConfigurations(AWSProperty):
    """
    `NotificationConfigurations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-notificationconfiguration.html>`__
    """

    props: PropsDictType = {
        "NotificationTypes": ([str], False),
        "TopicARN": ([str], True),
    }


class AutoScalingGroup(AWSObject):
    """
    `AutoScalingGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html>`__
    """

    resource_type = "AWS::AutoScaling::AutoScalingGroup"

    props: PropsDictType = {
        "AutoScalingGroupName": (str, False),
        "AvailabilityZones": ([str], False),
        "CapacityRebalance": (boolean, False),
        "Context": (str, False),
        "Cooldown": (str, False),
        "DefaultInstanceWarmup": (integer, False),
        "DesiredCapacity": (str, False),
        "DesiredCapacityType": (str, False),
        "HealthCheckGracePeriod": (integer, False),
        "HealthCheckType": (str, False),
        "InstanceId": (str, False),
        "InstanceMaintenancePolicy": (InstanceMaintenancePolicy, False),
        "LaunchConfigurationName": (str, False),
        "LaunchTemplate": (LaunchTemplateSpecification, False),
        "LifecycleHookSpecificationList": ([LifecycleHookSpecification], False),
        "LoadBalancerNames": ([str], False),
        "MaxInstanceLifetime": (integer, False),
        "MaxSize": (validate_int_to_str, True),
        "MetricsCollection": ([MetricsCollection], False),
        "MinSize": (validate_int_to_str, True),
        "MixedInstancesPolicy": (MixedInstancesPolicy, False),
        "NewInstancesProtectedFromScaleIn": (boolean, False),
        "NotificationConfigurations": ([NotificationConfigurations], False),
        "PlacementGroup": (str, False),
        "ServiceLinkedRoleARN": (str, False),
        "Tags": (validate_tags_or_list, False),
        "TargetGroupARNs": ([str], False),
        "TerminationPolicies": ([str], False),
        "VPCZoneIdentifier": ([str], False),
    }

    def validate(self):
        validate_auto_scaling_group(self)


class EBSBlockDevice(AWSProperty):
    """
    `EBSBlockDevice <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevice.html>`__
    """

    props: PropsDictType = {
        "DeleteOnTermination": (boolean, False),
        "Encrypted": (boolean, False),
        "Iops": (integer, False),
        "SnapshotId": (str, False),
        "Throughput": (integer, False),
        "VolumeSize": (integer, False),
        "VolumeType": (str, False),
    }


class BlockDeviceMapping(AWSProperty):
    """
    `BlockDeviceMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-blockdevicemapping.html>`__
    """

    props: PropsDictType = {
        "DeviceName": (str, True),
        "Ebs": (EBSBlockDevice, False),
        "NoDevice": (boolean, False),
        "VirtualName": (str, False),
    }


class MetadataOptions(AWSProperty):
    """
    `MetadataOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-launchconfiguration-metadataoptions.html>`__
    """

    props: PropsDictType = {
        "HttpEndpoint": (str, False),
        "HttpPutResponseHopLimit": (integer, False),
        "HttpTokens": (str, False),
    }


class LaunchConfiguration(AWSObject):
    """
    `LaunchConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html>`__
    """

    resource_type = "AWS::AutoScaling::LaunchConfiguration"

    props: PropsDictType = {
        "AssociatePublicIpAddress": (boolean, False),
        "BlockDeviceMappings": ([BlockDeviceMapping], False),
        "ClassicLinkVPCId": (str, False),
        "ClassicLinkVPCSecurityGroups": ([str], False),
        "EbsOptimized": (boolean, False),
        "IamInstanceProfile": (str, False),
        "ImageId": (str, True),
        "InstanceId": (str, False),
        "InstanceMonitoring": (boolean, False),
        "InstanceType": (str, True),
        "KernelId": (str, False),
        "KeyName": (str, False),
        "LaunchConfigurationName": (str, False),
        "MetadataOptions": (MetadataOptions, False),
        "PlacementTenancy": (str, False),
        "RamDiskId": (str, False),
        "SecurityGroups": ([str], False),
        "SpotPrice": (str, False),
        "UserData": (str, False),
    }


class LifecycleHook(AWSObject):
    """
    `LifecycleHook <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-lifecyclehook.html>`__
    """

    resource_type = "AWS::AutoScaling::LifecycleHook"

    props: PropsDictType = {
        "AutoScalingGroupName": (str, True),
        "DefaultResult": (str, False),
        "HeartbeatTimeout": (integer, False),
        "LifecycleHookName": (str, False),
        "LifecycleTransition": (str, True),
        "NotificationMetadata": (str, False),
        "NotificationTargetARN": (str, False),
        "RoleARN": (str, False),
    }


class MetricDimension(AWSProperty):
    """
    `MetricDimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdimension.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": (str, True),
    }


class Metric(AWSProperty):
    """
    `Metric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metric.html>`__
    """

    props: PropsDictType = {
        "Dimensions": ([MetricDimension], False),
        "MetricName": (str, True),
        "Namespace": (str, True),
    }


class MetricStat(AWSProperty):
    """
    `MetricStat <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricstat.html>`__
    """

    props: PropsDictType = {
        "Metric": (Metric, True),
        "Stat": (str, True),
        "Unit": (str, False),
    }


class MetricDataQuery(AWSProperty):
    """
    `MetricDataQuery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdataquery.html>`__
    """

    props: PropsDictType = {
        "Expression": (str, False),
        "Id": (str, True),
        "Label": (str, False),
        "MetricStat": (MetricStat, False),
        "ReturnData": (boolean, False),
    }


class PredictiveScalingCustomizedCapacityMetric(AWSProperty):
    """
    `PredictiveScalingCustomizedCapacityMetric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric.html>`__
    """

    props: PropsDictType = {
        "MetricDataQueries": ([MetricDataQuery], True),
    }


class PredictiveScalingCustomizedLoadMetric(AWSProperty):
    """
    `PredictiveScalingCustomizedLoadMetric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedloadmetric.html>`__
    """

    props: PropsDictType = {
        "MetricDataQueries": ([MetricDataQuery], True),
    }


class PredictiveScalingCustomizedScalingMetric(AWSProperty):
    """
    `PredictiveScalingCustomizedScalingMetric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric.html>`__
    """

    props: PropsDictType = {
        "MetricDataQueries": ([MetricDataQuery], True),
    }


class PredictiveScalingPredefinedLoadMetric(AWSProperty):
    """
    `PredictiveScalingPredefinedLoadMetric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedloadmetric.html>`__
    """

    props: PropsDictType = {
        "PredefinedMetricType": (str, True),
        "ResourceLabel": (str, False),
    }


class PredictiveScalingPredefinedMetricPair(AWSProperty):
    """
    `PredictiveScalingPredefinedMetricPair <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedmetricpair.html>`__
    """

    props: PropsDictType = {
        "PredefinedMetricType": (str, True),
        "ResourceLabel": (str, False),
    }


class PredictiveScalingPredefinedScalingMetric(AWSProperty):
    """
    `PredictiveScalingPredefinedScalingMetric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedscalingmetric.html>`__
    """

    props: PropsDictType = {
        "PredefinedMetricType": (str, True),
        "ResourceLabel": (str, False),
    }


class PredictiveScalingMetricSpecification(AWSProperty):
    """
    `PredictiveScalingMetricSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html>`__
    """

    props: PropsDictType = {
        "CustomizedCapacityMetricSpecification": (
            PredictiveScalingCustomizedCapacityMetric,
            False,
        ),
        "CustomizedLoadMetricSpecification": (
            PredictiveScalingCustomizedLoadMetric,
            False,
        ),
        "CustomizedScalingMetricSpecification": (
            PredictiveScalingCustomizedScalingMetric,
            False,
        ),
        "PredefinedLoadMetricSpecification": (
            PredictiveScalingPredefinedLoadMetric,
            False,
        ),
        "PredefinedMetricPairSpecification": (
            PredictiveScalingPredefinedMetricPair,
            False,
        ),
        "PredefinedScalingMetricSpecification": (
            PredictiveScalingPredefinedScalingMetric,
            False,
        ),
        "TargetValue": (double, True),
    }


class PredictiveScalingConfiguration(AWSProperty):
    """
    `PredictiveScalingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingconfiguration.html>`__
    """

    props: PropsDictType = {
        "MaxCapacityBreachBehavior": (str, False),
        "MaxCapacityBuffer": (integer, False),
        "MetricSpecifications": ([PredictiveScalingMetricSpecification], True),
        "Mode": (str, False),
        "SchedulingBufferTime": (integer, False),
    }


class StepAdjustments(AWSProperty):
    """
    `StepAdjustments <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-stepadjustment.html>`__
    """

    props: PropsDictType = {
        "MetricIntervalLowerBound": (double, False),
        "MetricIntervalUpperBound": (double, False),
        "ScalingAdjustment": (integer, True),
    }


class CustomizedMetricSpecification(AWSProperty):
    """
    `CustomizedMetricSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html>`__
    """

    props: PropsDictType = {
        "Dimensions": ([MetricDimension], False),
        "MetricName": (str, True),
        "Namespace": (str, True),
        "Statistic": (str, True),
        "Unit": (str, False),
    }


class PredefinedMetricSpecification(AWSProperty):
    """
    `PredefinedMetricSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.html>`__
    """

    props: PropsDictType = {
        "PredefinedMetricType": (str, True),
        "ResourceLabel": (str, False),
    }


class TargetTrackingConfiguration(AWSProperty):
    """
    `TargetTrackingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html>`__
    """

    props: PropsDictType = {
        "CustomizedMetricSpecification": (CustomizedMetricSpecification, False),
        "DisableScaleIn": (boolean, False),
        "PredefinedMetricSpecification": (PredefinedMetricSpecification, False),
        "TargetValue": (double, True),
    }


class ScalingPolicy(AWSObject):
    """
    `ScalingPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html>`__
    """

    resource_type = "AWS::AutoScaling::ScalingPolicy"

    props: PropsDictType = {
        "AdjustmentType": (str, False),
        "AutoScalingGroupName": (str, True),
        "Cooldown": (str, False),
        "EstimatedInstanceWarmup": (integer, False),
        "MetricAggregationType": (str, False),
        "MinAdjustmentMagnitude": (integer, False),
        "PolicyType": (str, False),
        "PredictiveScalingConfiguration": (PredictiveScalingConfiguration, False),
        "ScalingAdjustment": (integer, False),
        "StepAdjustments": ([StepAdjustments], False),
        "TargetTrackingConfiguration": (TargetTrackingConfiguration, False),
    }


class ScheduledAction(AWSObject):
    """
    `ScheduledAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scheduledaction.html>`__
    """

    resource_type = "AWS::AutoScaling::ScheduledAction"

    props: PropsDictType = {
        "AutoScalingGroupName": (str, True),
        "DesiredCapacity": (integer, False),
        "EndTime": (str, False),
        "MaxSize": (integer, False),
        "MinSize": (integer, False),
        "Recurrence": (str, False),
        "StartTime": (str, False),
        "TimeZone": (str, False),
    }


class InstanceReusePolicy(AWSProperty):
    """
    `InstanceReusePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-warmpool-instancereusepolicy.html>`__
    """

    props: PropsDictType = {
        "ReuseOnScaleIn": (boolean, False),
    }


class WarmPool(AWSObject):
    """
    `WarmPool <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-warmpool.html>`__
    """

    resource_type = "AWS::AutoScaling::WarmPool"

    props: PropsDictType = {
        "AutoScalingGroupName": (str, True),
        "InstanceReusePolicy": (InstanceReusePolicy, False),
        "MaxGroupPreparedCapacity": (integer, False),
        "MinSize": (integer, False),
        "PoolState": (str, False),
    }

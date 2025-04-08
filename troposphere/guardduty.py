# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class CFNKubernetesAuditLogsConfiguration(AWSProperty):
    """
    `CFNKubernetesAuditLogsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration.html>`__
    """

    props: PropsDictType = {
        "Enable": (boolean, True),
    }


class CFNKubernetesConfiguration(AWSProperty):
    """
    `CFNKubernetesConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesconfiguration.html>`__
    """

    props: PropsDictType = {
        "AuditLogs": (CFNKubernetesAuditLogsConfiguration, True),
    }


class CFNScanEc2InstanceWithFindingsConfiguration(AWSProperty):
    """
    `CFNScanEc2InstanceWithFindingsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnscanec2instancewithfindingsconfiguration.html>`__
    """

    props: PropsDictType = {
        "EbsVolumes": (boolean, False),
    }


class CFNMalwareProtectionConfiguration(AWSProperty):
    """
    `CFNMalwareProtectionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnmalwareprotectionconfiguration.html>`__
    """

    props: PropsDictType = {
        "ScanEc2InstanceWithFindings": (
            CFNScanEc2InstanceWithFindingsConfiguration,
            False,
        ),
    }


class CFNS3LogsConfiguration(AWSProperty):
    """
    `CFNS3LogsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html>`__
    """

    props: PropsDictType = {
        "Enable": (boolean, True),
    }


class CFNDataSourceConfigurations(AWSProperty):
    """
    `CFNDataSourceConfigurations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html>`__
    """

    props: PropsDictType = {
        "Kubernetes": (CFNKubernetesConfiguration, False),
        "MalwareProtection": (CFNMalwareProtectionConfiguration, False),
        "S3Logs": (CFNS3LogsConfiguration, False),
    }


class CFNFeatureAdditionalConfiguration(AWSProperty):
    """
    `CFNFeatureAdditionalConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Status": (str, False),
    }


class CFNFeatureConfiguration(AWSProperty):
    """
    `CFNFeatureConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnfeatureconfiguration.html>`__
    """

    props: PropsDictType = {
        "AdditionalConfiguration": ([CFNFeatureAdditionalConfiguration], False),
        "Name": (str, True),
        "Status": (str, True),
    }


class TagItem(AWSProperty):
    """
    `TagItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-threatintelset-tagitem.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class Detector(AWSObject):
    """
    `Detector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html>`__
    """

    resource_type = "AWS::GuardDuty::Detector"

    props: PropsDictType = {
        "DataSources": (CFNDataSourceConfigurations, False),
        "Enable": (boolean, True),
        "Features": ([CFNFeatureConfiguration], False),
        "FindingPublishingFrequency": (str, False),
        "Tags": ([TagItem], False),
    }


class Condition(AWSProperty):
    """
    `Condition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html>`__
    """

    props: PropsDictType = {
        "Eq": ([str], False),
        "Equals": ([str], False),
        "GreaterThan": (integer, False),
        "GreaterThanOrEqual": (integer, False),
        "Gt": (integer, False),
        "Gte": (integer, False),
        "LessThan": (integer, False),
        "LessThanOrEqual": (integer, False),
        "Lt": (integer, False),
        "Lte": (integer, False),
        "Neq": ([str], False),
        "NotEquals": ([str], False),
    }


class FindingCriteria(AWSProperty):
    """
    `FindingCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html>`__
    """

    props: PropsDictType = {
        "Criterion": (dict, False),
    }


class Filter(AWSObject):
    """
    `Filter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html>`__
    """

    resource_type = "AWS::GuardDuty::Filter"

    props: PropsDictType = {
        "Action": (str, False),
        "Description": (str, False),
        "DetectorId": (str, True),
        "FindingCriteria": (FindingCriteria, True),
        "Name": (str, True),
        "Rank": (integer, False),
        "Tags": (Tags, False),
    }


class IPSet(AWSObject):
    """
    `IPSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html>`__
    """

    resource_type = "AWS::GuardDuty::IPSet"

    props: PropsDictType = {
        "Activate": (boolean, False),
        "DetectorId": (str, False),
        "Format": (str, True),
        "Location": (str, True),
        "Name": (str, False),
        "Tags": ([TagItem], False),
    }


class CFNTagging(AWSProperty):
    """
    `CFNTagging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-malwareprotectionplan-cfntagging.html>`__
    """

    props: PropsDictType = {
        "Status": (str, False),
    }


class CFNActions(AWSProperty):
    """
    `CFNActions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-malwareprotectionplan-cfnactions.html>`__
    """

    props: PropsDictType = {
        "Tagging": (CFNTagging, False),
    }


class S3Bucket(AWSProperty):
    """
    `S3Bucket <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-malwareprotectionplan-s3bucket.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, False),
        "ObjectPrefixes": ([str], False),
    }


class CFNProtectedResource(AWSProperty):
    """
    `CFNProtectedResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-malwareprotectionplan-cfnprotectedresource.html>`__
    """

    props: PropsDictType = {
        "S3Bucket": (S3Bucket, True),
    }


class MalwareProtectionPlan(AWSObject):
    """
    `MalwareProtectionPlan <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-malwareprotectionplan.html>`__
    """

    resource_type = "AWS::GuardDuty::MalwareProtectionPlan"

    props: PropsDictType = {
        "Actions": (CFNActions, False),
        "ProtectedResource": (CFNProtectedResource, True),
        "Role": (str, True),
        "Tags": ([TagItem], False),
    }


class Master(AWSObject):
    """
    `Master <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html>`__
    """

    resource_type = "AWS::GuardDuty::Master"

    props: PropsDictType = {
        "DetectorId": (str, True),
        "InvitationId": (str, False),
        "MasterId": (str, True),
    }


class Member(AWSObject):
    """
    `Member <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html>`__
    """

    resource_type = "AWS::GuardDuty::Member"

    props: PropsDictType = {
        "DetectorId": (str, False),
        "DisableEmailNotification": (boolean, False),
        "Email": (str, True),
        "MemberId": (str, False),
        "Message": (str, False),
        "Status": (str, False),
    }


class CFNDestinationProperties(AWSProperty):
    """
    `CFNDestinationProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-publishingdestination-cfndestinationproperties.html>`__
    """

    props: PropsDictType = {
        "DestinationArn": (str, False),
        "KmsKeyArn": (str, False),
    }


class PublishingDestination(AWSObject):
    """
    `PublishingDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-publishingdestination.html>`__
    """

    resource_type = "AWS::GuardDuty::PublishingDestination"

    props: PropsDictType = {
        "DestinationProperties": (CFNDestinationProperties, True),
        "DestinationType": (str, True),
        "DetectorId": (str, True),
        "Tags": ([TagItem], False),
    }


class ThreatIntelSet(AWSObject):
    """
    `ThreatIntelSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html>`__
    """

    resource_type = "AWS::GuardDuty::ThreatIntelSet"

    props: PropsDictType = {
        "Activate": (boolean, False),
        "DetectorId": (str, False),
        "Format": (str, True),
        "Location": (str, True),
        "Name": (str, False),
        "Tags": ([TagItem], False),
    }


class CFNStatusReasons(AWSProperty):
    """
    `CFNStatusReasons <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-malwareprotectionplan-cfnstatusreasons.html>`__
    """

    props: PropsDictType = {
        "Code": (str, False),
        "Message": (str, False),
    }

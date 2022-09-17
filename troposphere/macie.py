# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import integer
from .validators.macie import (
    findingsfilter_action,
    session_findingpublishingfrequency,
    session_status,
)


class AllowList(AWSObject):
    """
    `AllowList <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html>`__
    """

    resource_type = "AWS::Macie::AllowList"

    props: PropsDictType = {
        "Criteria": (dict, True),
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class CustomDataIdentifier(AWSObject):
    """
    `CustomDataIdentifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html>`__
    """

    resource_type = "AWS::Macie::CustomDataIdentifier"

    props: PropsDictType = {
        "Description": (str, False),
        "IgnoreWords": ([str], False),
        "Keywords": ([str], False),
        "MaximumMatchDistance": (integer, False),
        "Name": (str, True),
        "Regex": (str, True),
    }


class FindingCriteria(AWSProperty):
    """
    `FindingCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html>`__
    """

    props: PropsDictType = {
        "Criterion": (dict, False),
    }


class FindingsFilter(AWSObject):
    """
    `FindingsFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html>`__
    """

    resource_type = "AWS::Macie::FindingsFilter"

    props: PropsDictType = {
        "Action": (findingsfilter_action, False),
        "Description": (str, False),
        "FindingCriteria": (FindingCriteria, True),
        "Name": (str, True),
        "Position": (integer, False),
    }


class Session(AWSObject):
    """
    `Session <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html>`__
    """

    resource_type = "AWS::Macie::Session"

    props: PropsDictType = {
        "FindingPublishingFrequency": (session_findingpublishingfrequency, False),
        "Status": (session_status, False),
    }

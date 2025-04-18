# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.globalaccelerator import (
    accelerator_ipaddresstype,
    endpointgroup_healthcheckprotocol,
    listener_clientaffinity,
    listener_protocol,
)


class Accelerator(AWSObject):
    """
    `Accelerator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html>`__
    """

    resource_type = "AWS::GlobalAccelerator::Accelerator"

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "IpAddressType": (accelerator_ipaddresstype, False),
        "IpAddresses": ([str], False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class Resource(AWSProperty):
    """
    `Resource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-crossaccountattachment-resource.html>`__
    """

    props: PropsDictType = {
        "Cidr": (str, False),
        "EndpointId": (str, False),
        "Region": (str, False),
    }


class CrossAccountAttachment(AWSObject):
    """
    `CrossAccountAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-crossaccountattachment.html>`__
    """

    resource_type = "AWS::GlobalAccelerator::CrossAccountAttachment"

    props: PropsDictType = {
        "Name": (str, True),
        "Principals": ([str], False),
        "Resources": ([Resource], False),
        "Tags": (Tags, False),
    }


class EndpointConfiguration(AWSProperty):
    """
    `EndpointConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html>`__
    """

    props: PropsDictType = {
        "AttachmentArn": (str, False),
        "ClientIPPreservationEnabled": (boolean, False),
        "EndpointId": (str, True),
        "Weight": (integer, False),
    }


class PortOverride(AWSProperty):
    """
    `PortOverride <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html>`__
    """

    props: PropsDictType = {
        "EndpointPort": (integer, True),
        "ListenerPort": (integer, True),
    }


class EndpointGroup(AWSObject):
    """
    `EndpointGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html>`__
    """

    resource_type = "AWS::GlobalAccelerator::EndpointGroup"

    props: PropsDictType = {
        "EndpointConfigurations": ([EndpointConfiguration], False),
        "EndpointGroupRegion": (str, True),
        "HealthCheckIntervalSeconds": (integer, False),
        "HealthCheckPath": (str, False),
        "HealthCheckPort": (integer, False),
        "HealthCheckProtocol": (endpointgroup_healthcheckprotocol, False),
        "ListenerArn": (str, True),
        "PortOverrides": ([PortOverride], False),
        "ThresholdCount": (integer, False),
        "TrafficDialPercentage": (double, False),
    }


class PortRange(AWSProperty):
    """
    `PortRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html>`__
    """

    props: PropsDictType = {
        "FromPort": (integer, True),
        "ToPort": (integer, True),
    }


class Listener(AWSObject):
    """
    `Listener <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html>`__
    """

    resource_type = "AWS::GlobalAccelerator::Listener"

    props: PropsDictType = {
        "AcceleratorArn": (str, True),
        "ClientAffinity": (listener_clientaffinity, False),
        "PortRanges": ([PortRange], True),
        "Protocol": (listener_protocol, True),
    }

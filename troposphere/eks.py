# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.eks import VALID_TAINT_EFFECT  # noqa: F401
from .validators.eks import (
    validate_cluster_logging,
    validate_taint_effect,
    validate_taint_key,
    validate_taint_value,
)


class AccessScope(AWSProperty):
    """
    `AccessScope <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-accessentry-accessscope.html>`__
    """

    props: PropsDictType = {
        "Namespaces": ([str], False),
        "Type": (str, True),
    }


class AccessPolicy(AWSProperty):
    """
    `AccessPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-accessentry-accesspolicy.html>`__
    """

    props: PropsDictType = {
        "AccessScope": (AccessScope, True),
        "PolicyArn": (str, True),
    }


class AccessEntry(AWSObject):
    """
    `AccessEntry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-accessentry.html>`__
    """

    resource_type = "AWS::EKS::AccessEntry"

    props: PropsDictType = {
        "AccessPolicies": ([AccessPolicy], False),
        "ClusterName": (str, True),
        "KubernetesGroups": ([str], False),
        "PrincipalArn": (str, True),
        "Tags": (Tags, False),
        "Type": (str, False),
        "Username": (str, False),
    }


class PodIdentityAssociationProperty(AWSProperty):
    """
    `PodIdentityAssociationProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-addon-podidentityassociation.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, True),
        "ServiceAccount": (str, True),
    }


class Addon(AWSObject):
    """
    `Addon <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html>`__
    """

    resource_type = "AWS::EKS::Addon"

    props: PropsDictType = {
        "AddonName": (str, True),
        "AddonVersion": (str, False),
        "ClusterName": (str, True),
        "ConfigurationValues": (str, False),
        "PodIdentityAssociations": ([PodIdentityAssociationProperty], False),
        "PreserveOnDelete": (boolean, False),
        "ResolveConflicts": (str, False),
        "ServiceAccountRoleArn": (str, False),
        "Tags": (Tags, False),
    }


class AccessConfig(AWSProperty):
    """
    `AccessConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-accessconfig.html>`__
    """

    props: PropsDictType = {
        "AuthenticationMode": (str, False),
        "BootstrapClusterCreatorAdminPermissions": (boolean, False),
    }


class ComputeConfig(AWSProperty):
    """
    `ComputeConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-computeconfig.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "NodePools": ([str], False),
        "NodeRoleArn": (str, False),
    }


class Provider(AWSProperty):
    """
    `Provider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html>`__
    """

    props: PropsDictType = {
        "KeyArn": (str, False),
    }


class EncryptionConfig(AWSProperty):
    """
    `EncryptionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-encryptionconfig.html>`__
    """

    props: PropsDictType = {
        "Provider": (Provider, False),
        "Resources": ([str], False),
    }


class ElasticLoadBalancing(AWSProperty):
    """
    `ElasticLoadBalancing <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-elasticloadbalancing.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class KubernetesNetworkConfig(AWSProperty):
    """
    `KubernetesNetworkConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html>`__
    """

    props: PropsDictType = {
        "ElasticLoadBalancing": (ElasticLoadBalancing, False),
        "IpFamily": (str, False),
        "ServiceIpv4Cidr": (str, False),
        "ServiceIpv6Cidr": (str, False),
    }


class LoggingTypeConfig(AWSProperty):
    """
    `LoggingTypeConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-loggingtypeconfig.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
    }


class ClusterLogging(AWSProperty):
    """
    `ClusterLogging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-clusterlogging.html>`__
    """

    props: PropsDictType = {
        "EnabledTypes": ([LoggingTypeConfig], False),
    }

    def validate(self):
        validate_cluster_logging(self)


class Logging(AWSProperty):
    """
    `Logging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-logging.html>`__
    """

    props: PropsDictType = {
        "ClusterLogging": (ClusterLogging, False),
    }


class ControlPlanePlacement(AWSProperty):
    """
    `ControlPlanePlacement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-controlplaneplacement.html>`__
    """

    props: PropsDictType = {
        "GroupName": (str, False),
    }


class OutpostConfig(AWSProperty):
    """
    `OutpostConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-outpostconfig.html>`__
    """

    props: PropsDictType = {
        "ControlPlaneInstanceType": (str, True),
        "ControlPlanePlacement": (ControlPlanePlacement, False),
        "OutpostArns": ([str], True),
    }


class RemoteNodeNetwork(AWSProperty):
    """
    `RemoteNodeNetwork <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-remotenodenetwork.html>`__
    """

    props: PropsDictType = {
        "Cidrs": ([str], True),
    }


class RemotePodNetwork(AWSProperty):
    """
    `RemotePodNetwork <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-remotepodnetwork.html>`__
    """

    props: PropsDictType = {
        "Cidrs": ([str], True),
    }


class RemoteNetworkConfig(AWSProperty):
    """
    `RemoteNetworkConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-remotenetworkconfig.html>`__
    """

    props: PropsDictType = {
        "RemoteNodeNetworks": ([RemoteNodeNetwork], True),
        "RemotePodNetworks": ([RemotePodNetwork], False),
    }


class ResourcesVpcConfig(AWSProperty):
    """
    `ResourcesVpcConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html>`__
    """

    props: PropsDictType = {
        "EndpointPrivateAccess": (boolean, False),
        "EndpointPublicAccess": (boolean, False),
        "PublicAccessCidrs": ([str], False),
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], True),
    }


class BlockStorage(AWSProperty):
    """
    `BlockStorage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-blockstorage.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class StorageConfig(AWSProperty):
    """
    `StorageConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-storageconfig.html>`__
    """

    props: PropsDictType = {
        "BlockStorage": (BlockStorage, False),
    }


class UpgradePolicy(AWSProperty):
    """
    `UpgradePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-upgradepolicy.html>`__
    """

    props: PropsDictType = {
        "SupportType": (str, False),
    }


class ZonalShiftConfig(AWSProperty):
    """
    `ZonalShiftConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-zonalshiftconfig.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class Cluster(AWSObject):
    """
    `Cluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html>`__
    """

    resource_type = "AWS::EKS::Cluster"

    props: PropsDictType = {
        "AccessConfig": (AccessConfig, False),
        "BootstrapSelfManagedAddons": (boolean, False),
        "ComputeConfig": (ComputeConfig, False),
        "EncryptionConfig": ([EncryptionConfig], False),
        "Force": (boolean, False),
        "KubernetesNetworkConfig": (KubernetesNetworkConfig, False),
        "Logging": (Logging, False),
        "Name": (str, False),
        "OutpostConfig": (OutpostConfig, False),
        "RemoteNetworkConfig": (RemoteNetworkConfig, False),
        "ResourcesVpcConfig": (ResourcesVpcConfig, True),
        "RoleArn": (str, True),
        "StorageConfig": (StorageConfig, False),
        "Tags": (Tags, False),
        "UpgradePolicy": (UpgradePolicy, False),
        "Version": (str, False),
        "ZonalShiftConfig": (ZonalShiftConfig, False),
    }


class Label(AWSProperty):
    """
    `Label <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class Selector(AWSProperty):
    """
    `Selector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html>`__
    """

    props: PropsDictType = {
        "Labels": ([Label], False),
        "Namespace": (str, True),
    }


class FargateProfile(AWSObject):
    """
    `FargateProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html>`__
    """

    resource_type = "AWS::EKS::FargateProfile"

    props: PropsDictType = {
        "ClusterName": (str, True),
        "FargateProfileName": (str, False),
        "PodExecutionRoleArn": (str, True),
        "Selectors": ([Selector], True),
        "Subnets": ([str], False),
        "Tags": (Tags, False),
    }


class RequiredClaim(AWSProperty):
    """
    `RequiredClaim <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-requiredclaim.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class OidcIdentityProviderConfig(AWSProperty):
    """
    `OidcIdentityProviderConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html>`__
    """

    props: PropsDictType = {
        "ClientId": (str, True),
        "GroupsClaim": (str, False),
        "GroupsPrefix": (str, False),
        "IssuerUrl": (str, True),
        "RequiredClaims": ([RequiredClaim], False),
        "UsernameClaim": (str, False),
        "UsernamePrefix": (str, False),
    }


class IdentityProviderConfig(AWSObject):
    """
    `IdentityProviderConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html>`__
    """

    resource_type = "AWS::EKS::IdentityProviderConfig"

    props: PropsDictType = {
        "ClusterName": (str, True),
        "IdentityProviderConfigName": (str, False),
        "Oidc": (OidcIdentityProviderConfig, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class LaunchTemplateSpecification(AWSProperty):
    """
    `LaunchTemplateSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html>`__
    """

    props: PropsDictType = {
        "Id": (str, False),
        "Name": (str, False),
        "Version": (str, False),
    }


class NodeRepairConfig(AWSProperty):
    """
    `NodeRepairConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-noderepairconfig.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class RemoteAccess(AWSProperty):
    """
    `RemoteAccess <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html>`__
    """

    props: PropsDictType = {
        "Ec2SshKey": (str, True),
        "SourceSecurityGroups": ([str], False),
    }


class ScalingConfig(AWSProperty):
    """
    `ScalingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html>`__
    """

    props: PropsDictType = {
        "DesiredSize": (integer, False),
        "MaxSize": (integer, False),
        "MinSize": (integer, False),
    }


class Taint(AWSProperty):
    """
    `Taint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html>`__
    """

    props: PropsDictType = {
        "Effect": (validate_taint_effect, False),
        "Key": (validate_taint_key, False),
        "Value": (validate_taint_value, False),
    }


class UpdateConfig(AWSProperty):
    """
    `UpdateConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html>`__
    """

    props: PropsDictType = {
        "MaxUnavailable": (double, False),
        "MaxUnavailablePercentage": (double, False),
        "UpdateStrategy": (str, False),
    }


class Nodegroup(AWSObject):
    """
    `Nodegroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html>`__
    """

    resource_type = "AWS::EKS::Nodegroup"

    props: PropsDictType = {
        "AmiType": (str, False),
        "CapacityType": (str, False),
        "ClusterName": (str, True),
        "DiskSize": (integer, False),
        "ForceUpdateEnabled": (boolean, False),
        "InstanceTypes": ([str], False),
        "Labels": (dict, False),
        "LaunchTemplate": (LaunchTemplateSpecification, False),
        "NodeRepairConfig": (NodeRepairConfig, False),
        "NodeRole": (str, True),
        "NodegroupName": (str, False),
        "ReleaseVersion": (str, False),
        "RemoteAccess": (RemoteAccess, False),
        "ScalingConfig": (ScalingConfig, False),
        "Subnets": ([str], True),
        "Tags": (dict, False),
        "Taints": ([Taint], False),
        "UpdateConfig": (UpdateConfig, False),
        "Version": (str, False),
    }


class PodIdentityAssociation(AWSObject):
    """
    `PodIdentityAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-podidentityassociation.html>`__
    """

    resource_type = "AWS::EKS::PodIdentityAssociation"

    props: PropsDictType = {
        "ClusterName": (str, True),
        "DisableSessionTags": (boolean, False),
        "Namespace": (str, True),
        "RoleArn": (str, True),
        "ServiceAccount": (str, True),
        "Tags": (Tags, False),
        "TargetRoleArn": (str, False),
    }

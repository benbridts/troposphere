# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.iam import Active  # noqa: F401
from .validators.iam import Inactive  # noqa: F401
from .validators.iam import (
    iam_group_name,
    iam_path,
    iam_role_name,
    iam_user_name,
    policytypes,
    status,
    validate_tags_or_list,
)


class AccessKey(AWSObject):
    """
    `AccessKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html>`__
    """

    resource_type = "AWS::IAM::AccessKey"

    props: PropsDictType = {
        "Serial": (integer, False),
        "Status": (status, False),
        "UserName": (str, True),
    }


class Policy(AWSProperty):
    """
    `Policy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-policy.html>`__
    """

    props: PropsDictType = {
        "PolicyDocument": (policytypes, True),
        "PolicyName": (str, True),
    }


class Group(AWSObject):
    """
    `Group <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html>`__
    """

    resource_type = "AWS::IAM::Group"

    props: PropsDictType = {
        "GroupName": (iam_group_name, False),
        "ManagedPolicyArns": ([str], False),
        "Path": (iam_path, False),
        "Policies": ([Policy], False),
    }


class GroupPolicy(AWSObject):
    """
    `GroupPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html>`__
    """

    resource_type = "AWS::IAM::GroupPolicy"

    props: PropsDictType = {
        "GroupName": (str, True),
        "PolicyDocument": (dict, False),
        "PolicyName": (str, True),
    }


class InstanceProfile(AWSObject):
    """
    `InstanceProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__
    """

    resource_type = "AWS::IAM::InstanceProfile"

    props: PropsDictType = {
        "InstanceProfileName": (str, False),
        "Path": (iam_path, False),
        "Roles": ([str], True),
    }


class ManagedPolicy(AWSObject):
    """
    `ManagedPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html>`__
    """

    resource_type = "AWS::IAM::ManagedPolicy"

    props: PropsDictType = {
        "Description": (str, False),
        "Groups": ([str], False),
        "ManagedPolicyName": (str, False),
        "Path": (iam_path, False),
        "PolicyDocument": (policytypes, True),
        "Roles": ([str], False),
        "Users": ([str], False),
    }


class OIDCProvider(AWSObject):
    """
    `OIDCProvider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html>`__
    """

    resource_type = "AWS::IAM::OIDCProvider"

    props: PropsDictType = {
        "ClientIdList": ([str], False),
        "Tags": (Tags, False),
        "ThumbprintList": ([str], False),
        "Url": (str, False),
    }


class PolicyType(AWSObject):
    """
    `PolicyType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
    """

    resource_type = "AWS::IAM::Policy"

    props: PropsDictType = {
        "Groups": ([str], False),
        "PolicyDocument": (policytypes, True),
        "PolicyName": (str, True),
        "Roles": ([str], False),
        "Users": ([str], False),
    }


class Role(AWSObject):
    """
    `Role <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__
    """

    resource_type = "AWS::IAM::Role"

    props: PropsDictType = {
        "AssumeRolePolicyDocument": (policytypes, True),
        "Description": (str, False),
        "ManagedPolicyArns": ([str], False),
        "MaxSessionDuration": (integer, False),
        "Path": (iam_path, False),
        "PermissionsBoundary": (str, False),
        "Policies": ([Policy], False),
        "RoleName": (iam_role_name, False),
        "Tags": (validate_tags_or_list, False),
    }


class RolePolicy(AWSObject):
    """
    `RolePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html>`__
    """

    resource_type = "AWS::IAM::RolePolicy"

    props: PropsDictType = {
        "PolicyDocument": (dict, False),
        "PolicyName": (str, True),
        "RoleName": (str, True),
    }


class SAMLPrivateKey(AWSProperty):
    """
    `SAMLPrivateKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-samlprovider-samlprivatekey.html>`__
    """

    props: PropsDictType = {
        "KeyId": (str, True),
        "Timestamp": (str, True),
    }


class SAMLProvider(AWSObject):
    """
    `SAMLProvider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html>`__
    """

    resource_type = "AWS::IAM::SAMLProvider"

    props: PropsDictType = {
        "AddPrivateKey": (str, False),
        "AssertionEncryptionMode": (str, False),
        "Name": (str, False),
        "PrivateKeyList": ([SAMLPrivateKey], False),
        "RemovePrivateKey": (str, False),
        "SamlMetadataDocument": (str, False),
        "Tags": (Tags, False),
    }


class ServerCertificate(AWSObject):
    """
    `ServerCertificate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html>`__
    """

    resource_type = "AWS::IAM::ServerCertificate"

    props: PropsDictType = {
        "CertificateBody": (str, False),
        "CertificateChain": (str, False),
        "Path": (str, False),
        "PrivateKey": (str, False),
        "ServerCertificateName": (str, False),
        "Tags": (Tags, False),
    }


class ServiceLinkedRole(AWSObject):
    """
    `ServiceLinkedRole <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html>`__
    """

    resource_type = "AWS::IAM::ServiceLinkedRole"

    props: PropsDictType = {
        "AWSServiceName": (str, False),
        "CustomSuffix": (str, False),
        "Description": (str, False),
    }


class LoginProfile(AWSProperty):
    """
    `LoginProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-loginprofile.html>`__
    """

    props: PropsDictType = {
        "Password": (str, True),
        "PasswordResetRequired": (boolean, False),
    }


class User(AWSObject):
    """
    `User <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html>`__
    """

    resource_type = "AWS::IAM::User"

    props: PropsDictType = {
        "Groups": ([str], False),
        "LoginProfile": (LoginProfile, False),
        "ManagedPolicyArns": ([str], False),
        "Path": (iam_path, False),
        "PermissionsBoundary": (str, False),
        "Policies": ([Policy], False),
        "Tags": (Tags, False),
        "UserName": (iam_user_name, False),
    }


class UserPolicy(AWSObject):
    """
    `UserPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html>`__
    """

    resource_type = "AWS::IAM::UserPolicy"

    props: PropsDictType = {
        "PolicyDocument": (dict, False),
        "PolicyName": (str, True),
        "UserName": (str, True),
    }


class UserToGroupAddition(AWSObject):
    """
    `UserToGroupAddition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html>`__
    """

    resource_type = "AWS::IAM::UserToGroupAddition"

    props: PropsDictType = {
        "GroupName": (str, True),
        "Users": ([str], True),
    }


class VirtualMFADevice(AWSObject):
    """
    `VirtualMFADevice <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html>`__
    """

    resource_type = "AWS::IAM::VirtualMFADevice"

    props: PropsDictType = {
        "Path": (str, False),
        "Tags": (Tags, False),
        "Users": ([str], True),
        "VirtualMfaDeviceName": (str, False),
    }

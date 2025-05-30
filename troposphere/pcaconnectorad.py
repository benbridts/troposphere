# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double


class VpcInformation(AWSProperty):
    """
    `VpcInformation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-connector-vpcinformation.html>`__
    """

    props: PropsDictType = {
        "IpAddressType": (str, False),
        "SecurityGroupIds": ([str], True),
    }


class Connector(AWSObject):
    """
    `Connector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html>`__
    """

    resource_type = "AWS::PCAConnectorAD::Connector"

    props: PropsDictType = {
        "CertificateAuthorityArn": (str, True),
        "DirectoryId": (str, True),
        "Tags": (dict, False),
        "VpcInformation": (VpcInformation, True),
    }


class DirectoryRegistration(AWSObject):
    """
    `DirectoryRegistration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-directoryregistration.html>`__
    """

    resource_type = "AWS::PCAConnectorAD::DirectoryRegistration"

    props: PropsDictType = {
        "DirectoryId": (str, True),
        "Tags": (dict, False),
    }


class ServicePrincipalName(AWSObject):
    """
    `ServicePrincipalName <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-serviceprincipalname.html>`__
    """

    resource_type = "AWS::PCAConnectorAD::ServicePrincipalName"

    props: PropsDictType = {
        "ConnectorArn": (str, False),
        "DirectoryRegistrationArn": (str, False),
    }


class ValidityPeriod(AWSProperty):
    """
    `ValidityPeriod <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-validityperiod.html>`__
    """

    props: PropsDictType = {
        "Period": (double, True),
        "PeriodType": (str, True),
    }


class CertificateValidity(AWSProperty):
    """
    `CertificateValidity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-certificatevalidity.html>`__
    """

    props: PropsDictType = {
        "RenewalPeriod": (ValidityPeriod, True),
        "ValidityPeriod": (ValidityPeriod, True),
    }


class EnrollmentFlagsV2(AWSProperty):
    """
    `EnrollmentFlagsV2 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html>`__
    """

    props: PropsDictType = {
        "EnableKeyReuseOnNtTokenKeysetStorageFull": (boolean, False),
        "IncludeSymmetricAlgorithms": (boolean, False),
        "NoSecurityExtension": (boolean, False),
        "RemoveInvalidCertificateFromPersonalStore": (boolean, False),
        "UserInteractionRequired": (boolean, False),
    }


class ApplicationPolicy(AWSProperty):
    """
    `ApplicationPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicy.html>`__
    """

    props: PropsDictType = {
        "PolicyObjectIdentifier": (str, False),
        "PolicyType": (str, False),
    }


class ApplicationPolicies(AWSProperty):
    """
    `ApplicationPolicies <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicies.html>`__
    """

    props: PropsDictType = {
        "Critical": (boolean, False),
        "Policies": ([ApplicationPolicy], True),
    }


class KeyUsageFlags(AWSProperty):
    """
    `KeyUsageFlags <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html>`__
    """

    props: PropsDictType = {
        "DataEncipherment": (boolean, False),
        "DigitalSignature": (boolean, False),
        "KeyAgreement": (boolean, False),
        "KeyEncipherment": (boolean, False),
        "NonRepudiation": (boolean, False),
    }


class KeyUsage(AWSProperty):
    """
    `KeyUsage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusage.html>`__
    """

    props: PropsDictType = {
        "Critical": (boolean, False),
        "UsageFlags": (KeyUsageFlags, True),
    }


class ExtensionsV2(AWSProperty):
    """
    `ExtensionsV2 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv2.html>`__
    """

    props: PropsDictType = {
        "ApplicationPolicies": (ApplicationPolicies, False),
        "KeyUsage": (KeyUsage, True),
    }


class GeneralFlagsV2(AWSProperty):
    """
    `GeneralFlagsV2 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv2.html>`__
    """

    props: PropsDictType = {
        "AutoEnrollment": (boolean, False),
        "MachineType": (boolean, False),
    }


class PrivateKeyAttributesV2(AWSProperty):
    """
    `PrivateKeyAttributesV2 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv2.html>`__
    """

    props: PropsDictType = {
        "CryptoProviders": ([str], False),
        "KeySpec": (str, True),
        "MinimalKeyLength": (double, True),
    }


class PrivateKeyFlagsV2(AWSProperty):
    """
    `PrivateKeyFlagsV2 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv2.html>`__
    """

    props: PropsDictType = {
        "ClientVersion": (str, True),
        "ExportableKey": (boolean, False),
        "StrongKeyProtectionRequired": (boolean, False),
    }


class SubjectNameFlagsV2(AWSProperty):
    """
    `SubjectNameFlagsV2 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html>`__
    """

    props: PropsDictType = {
        "RequireCommonName": (boolean, False),
        "RequireDirectoryPath": (boolean, False),
        "RequireDnsAsCn": (boolean, False),
        "RequireEmail": (boolean, False),
        "SanRequireDirectoryGuid": (boolean, False),
        "SanRequireDns": (boolean, False),
        "SanRequireDomainDns": (boolean, False),
        "SanRequireEmail": (boolean, False),
        "SanRequireSpn": (boolean, False),
        "SanRequireUpn": (boolean, False),
    }


class TemplateV2(AWSProperty):
    """
    `TemplateV2 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html>`__
    """

    props: PropsDictType = {
        "CertificateValidity": (CertificateValidity, True),
        "EnrollmentFlags": (EnrollmentFlagsV2, True),
        "Extensions": (ExtensionsV2, True),
        "GeneralFlags": (GeneralFlagsV2, True),
        "PrivateKeyAttributes": (PrivateKeyAttributesV2, True),
        "PrivateKeyFlags": (PrivateKeyFlagsV2, True),
        "SubjectNameFlags": (SubjectNameFlagsV2, True),
        "SupersededTemplates": ([str], False),
    }


class EnrollmentFlagsV3(AWSProperty):
    """
    `EnrollmentFlagsV3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html>`__
    """

    props: PropsDictType = {
        "EnableKeyReuseOnNtTokenKeysetStorageFull": (boolean, False),
        "IncludeSymmetricAlgorithms": (boolean, False),
        "NoSecurityExtension": (boolean, False),
        "RemoveInvalidCertificateFromPersonalStore": (boolean, False),
        "UserInteractionRequired": (boolean, False),
    }


class ExtensionsV3(AWSProperty):
    """
    `ExtensionsV3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv3.html>`__
    """

    props: PropsDictType = {
        "ApplicationPolicies": (ApplicationPolicies, False),
        "KeyUsage": (KeyUsage, True),
    }


class GeneralFlagsV3(AWSProperty):
    """
    `GeneralFlagsV3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv3.html>`__
    """

    props: PropsDictType = {
        "AutoEnrollment": (boolean, False),
        "MachineType": (boolean, False),
    }


class KeyUsagePropertyFlags(AWSProperty):
    """
    `KeyUsagePropertyFlags <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusagepropertyflags.html>`__
    """

    props: PropsDictType = {
        "Decrypt": (boolean, False),
        "KeyAgreement": (boolean, False),
        "Sign": (boolean, False),
    }


class KeyUsageProperty(AWSProperty):
    """
    `KeyUsageProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageproperty.html>`__
    """

    props: PropsDictType = {
        "PropertyFlags": (KeyUsagePropertyFlags, False),
        "PropertyType": (str, False),
    }


class PrivateKeyAttributesV3(AWSProperty):
    """
    `PrivateKeyAttributesV3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html>`__
    """

    props: PropsDictType = {
        "Algorithm": (str, True),
        "CryptoProviders": ([str], False),
        "KeySpec": (str, True),
        "KeyUsageProperty": (KeyUsageProperty, True),
        "MinimalKeyLength": (double, True),
    }


class PrivateKeyFlagsV3(AWSProperty):
    """
    `PrivateKeyFlagsV3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html>`__
    """

    props: PropsDictType = {
        "ClientVersion": (str, True),
        "ExportableKey": (boolean, False),
        "RequireAlternateSignatureAlgorithm": (boolean, False),
        "StrongKeyProtectionRequired": (boolean, False),
    }


class SubjectNameFlagsV3(AWSProperty):
    """
    `SubjectNameFlagsV3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html>`__
    """

    props: PropsDictType = {
        "RequireCommonName": (boolean, False),
        "RequireDirectoryPath": (boolean, False),
        "RequireDnsAsCn": (boolean, False),
        "RequireEmail": (boolean, False),
        "SanRequireDirectoryGuid": (boolean, False),
        "SanRequireDns": (boolean, False),
        "SanRequireDomainDns": (boolean, False),
        "SanRequireEmail": (boolean, False),
        "SanRequireSpn": (boolean, False),
        "SanRequireUpn": (boolean, False),
    }


class TemplateV3(AWSProperty):
    """
    `TemplateV3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html>`__
    """

    props: PropsDictType = {
        "CertificateValidity": (CertificateValidity, True),
        "EnrollmentFlags": (EnrollmentFlagsV3, True),
        "Extensions": (ExtensionsV3, True),
        "GeneralFlags": (GeneralFlagsV3, True),
        "HashAlgorithm": (str, True),
        "PrivateKeyAttributes": (PrivateKeyAttributesV3, True),
        "PrivateKeyFlags": (PrivateKeyFlagsV3, True),
        "SubjectNameFlags": (SubjectNameFlagsV3, True),
        "SupersededTemplates": ([str], False),
    }


class EnrollmentFlagsV4(AWSProperty):
    """
    `EnrollmentFlagsV4 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html>`__
    """

    props: PropsDictType = {
        "EnableKeyReuseOnNtTokenKeysetStorageFull": (boolean, False),
        "IncludeSymmetricAlgorithms": (boolean, False),
        "NoSecurityExtension": (boolean, False),
        "RemoveInvalidCertificateFromPersonalStore": (boolean, False),
        "UserInteractionRequired": (boolean, False),
    }


class ExtensionsV4(AWSProperty):
    """
    `ExtensionsV4 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv4.html>`__
    """

    props: PropsDictType = {
        "ApplicationPolicies": (ApplicationPolicies, False),
        "KeyUsage": (KeyUsage, True),
    }


class GeneralFlagsV4(AWSProperty):
    """
    `GeneralFlagsV4 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv4.html>`__
    """

    props: PropsDictType = {
        "AutoEnrollment": (boolean, False),
        "MachineType": (boolean, False),
    }


class PrivateKeyAttributesV4(AWSProperty):
    """
    `PrivateKeyAttributesV4 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html>`__
    """

    props: PropsDictType = {
        "Algorithm": (str, False),
        "CryptoProviders": ([str], False),
        "KeySpec": (str, True),
        "KeyUsageProperty": (KeyUsageProperty, False),
        "MinimalKeyLength": (double, True),
    }


class PrivateKeyFlagsV4(AWSProperty):
    """
    `PrivateKeyFlagsV4 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html>`__
    """

    props: PropsDictType = {
        "ClientVersion": (str, True),
        "ExportableKey": (boolean, False),
        "RequireAlternateSignatureAlgorithm": (boolean, False),
        "RequireSameKeyRenewal": (boolean, False),
        "StrongKeyProtectionRequired": (boolean, False),
        "UseLegacyProvider": (boolean, False),
    }


class SubjectNameFlagsV4(AWSProperty):
    """
    `SubjectNameFlagsV4 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html>`__
    """

    props: PropsDictType = {
        "RequireCommonName": (boolean, False),
        "RequireDirectoryPath": (boolean, False),
        "RequireDnsAsCn": (boolean, False),
        "RequireEmail": (boolean, False),
        "SanRequireDirectoryGuid": (boolean, False),
        "SanRequireDns": (boolean, False),
        "SanRequireDomainDns": (boolean, False),
        "SanRequireEmail": (boolean, False),
        "SanRequireSpn": (boolean, False),
        "SanRequireUpn": (boolean, False),
    }


class TemplateV4(AWSProperty):
    """
    `TemplateV4 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html>`__
    """

    props: PropsDictType = {
        "CertificateValidity": (CertificateValidity, True),
        "EnrollmentFlags": (EnrollmentFlagsV4, True),
        "Extensions": (ExtensionsV4, True),
        "GeneralFlags": (GeneralFlagsV4, True),
        "HashAlgorithm": (str, False),
        "PrivateKeyAttributes": (PrivateKeyAttributesV4, True),
        "PrivateKeyFlags": (PrivateKeyFlagsV4, True),
        "SubjectNameFlags": (SubjectNameFlagsV4, True),
        "SupersededTemplates": ([str], False),
    }


class TemplateDefinition(AWSProperty):
    """
    `TemplateDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatedefinition.html>`__
    """

    props: PropsDictType = {
        "TemplateV2": (TemplateV2, False),
        "TemplateV3": (TemplateV3, False),
        "TemplateV4": (TemplateV4, False),
    }


class Template(AWSObject):
    """
    `Template <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html>`__
    """

    resource_type = "AWS::PCAConnectorAD::Template"

    props: PropsDictType = {
        "ConnectorArn": (str, True),
        "Definition": (TemplateDefinition, True),
        "Name": (str, True),
        "ReenrollAllCertificateHolders": (boolean, False),
        "Tags": (dict, False),
    }


class AccessRights(AWSProperty):
    """
    `AccessRights <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights.html>`__
    """

    props: PropsDictType = {
        "AutoEnroll": (str, False),
        "Enroll": (str, False),
    }


class TemplateGroupAccessControlEntry(AWSObject):
    """
    `TemplateGroupAccessControlEntry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html>`__
    """

    resource_type = "AWS::PCAConnectorAD::TemplateGroupAccessControlEntry"

    props: PropsDictType = {
        "AccessRights": (AccessRights, True),
        "GroupDisplayName": (str, True),
        "GroupSecurityIdentifier": (str, False),
        "TemplateArn": (str, False),
    }

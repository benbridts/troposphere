# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class AnalysisParameter(AWSProperty):
    """
    `AnalysisParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisparameter.html>`__
    """

    props: PropsDictType = {
        "DefaultValue": (str, False),
        "Name": (str, True),
        "Type": (str, True),
    }


class AnalysisSchema(AWSProperty):
    """
    `AnalysisSchema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisschema.html>`__
    """

    props: PropsDictType = {
        "ReferencedTables": ([str], True),
    }


class S3Location(AWSProperty):
    """
    `S3Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-s3location.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "Key": (str, True),
    }


class AnalysisTemplateArtifact(AWSProperty):
    """
    `AnalysisTemplateArtifact <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifact.html>`__
    """

    props: PropsDictType = {
        "Location": (S3Location, True),
    }


class AnalysisTemplateArtifacts(AWSProperty):
    """
    `AnalysisTemplateArtifacts <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts.html>`__
    """

    props: PropsDictType = {
        "AdditionalArtifacts": ([AnalysisTemplateArtifact], False),
        "EntryPoint": (AnalysisTemplateArtifact, True),
        "RoleArn": (str, True),
    }


class AnalysisSource(AWSProperty):
    """
    `AnalysisSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysissource.html>`__
    """

    props: PropsDictType = {
        "Artifacts": (AnalysisTemplateArtifacts, False),
        "Text": (str, False),
    }


class Hash(AWSProperty):
    """
    `Hash <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-hash.html>`__
    """

    props: PropsDictType = {
        "Sha256": (str, False),
    }


class AnalysisTemplateArtifactMetadata(AWSProperty):
    """
    `AnalysisTemplateArtifactMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata.html>`__
    """

    props: PropsDictType = {
        "AdditionalArtifactHashes": ([Hash], False),
        "EntryPointHash": (Hash, True),
    }


class AnalysisSourceMetadata(AWSProperty):
    """
    `AnalysisSourceMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysissourcemetadata.html>`__
    """

    props: PropsDictType = {
        "Artifacts": (AnalysisTemplateArtifactMetadata, True),
    }


class AnalysisTemplate(AWSObject):
    """
    `AnalysisTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html>`__
    """

    resource_type = "AWS::CleanRooms::AnalysisTemplate"

    props: PropsDictType = {
        "AnalysisParameters": ([AnalysisParameter], False),
        "Description": (str, False),
        "Format": (str, True),
        "MembershipIdentifier": (str, True),
        "Name": (str, True),
        "Schema": (AnalysisSchema, False),
        "Source": (AnalysisSource, True),
        "SourceMetadata": (AnalysisSourceMetadata, False),
        "Tags": (Tags, False),
    }


class DataEncryptionMetadata(AWSProperty):
    """
    `DataEncryptionMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html>`__
    """

    props: PropsDictType = {
        "AllowCleartext": (boolean, True),
        "AllowDuplicates": (boolean, True),
        "AllowJoinsOnColumnsWithDifferentNames": (boolean, True),
        "PreserveNulls": (boolean, True),
    }


class MLMemberAbilities(AWSProperty):
    """
    `MLMemberAbilities <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-mlmemberabilities.html>`__
    """

    props: PropsDictType = {
        "CustomMLMemberAbilities": ([str], True),
    }


class JobComputePaymentConfig(AWSProperty):
    """
    `JobComputePaymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-jobcomputepaymentconfig.html>`__
    """

    props: PropsDictType = {
        "IsResponsible": (boolean, True),
    }


class ModelInferencePaymentConfig(AWSProperty):
    """
    `ModelInferencePaymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-modelinferencepaymentconfig.html>`__
    """

    props: PropsDictType = {
        "IsResponsible": (boolean, True),
    }


class ModelTrainingPaymentConfig(AWSProperty):
    """
    `ModelTrainingPaymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-modeltrainingpaymentconfig.html>`__
    """

    props: PropsDictType = {
        "IsResponsible": (boolean, True),
    }


class MLPaymentConfig(AWSProperty):
    """
    `MLPaymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-mlpaymentconfig.html>`__
    """

    props: PropsDictType = {
        "ModelInference": (ModelInferencePaymentConfig, False),
        "ModelTraining": (ModelTrainingPaymentConfig, False),
    }


class QueryComputePaymentConfig(AWSProperty):
    """
    `QueryComputePaymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-querycomputepaymentconfig.html>`__
    """

    props: PropsDictType = {
        "IsResponsible": (boolean, True),
    }


class PaymentConfiguration(AWSProperty):
    """
    `PaymentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-paymentconfiguration.html>`__
    """

    props: PropsDictType = {
        "JobCompute": (JobComputePaymentConfig, False),
        "MachineLearning": (MLPaymentConfig, False),
        "QueryCompute": (QueryComputePaymentConfig, True),
    }


class MemberSpecification(AWSProperty):
    """
    `MemberSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html>`__
    """

    props: PropsDictType = {
        "AccountId": (str, True),
        "DisplayName": (str, True),
        "MLMemberAbilities": (MLMemberAbilities, False),
        "MemberAbilities": ([str], False),
        "PaymentConfiguration": (PaymentConfiguration, False),
    }


class Collaboration(AWSObject):
    """
    `Collaboration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html>`__
    """

    resource_type = "AWS::CleanRooms::Collaboration"

    props: PropsDictType = {
        "AnalyticsEngine": (str, False),
        "CreatorDisplayName": (str, True),
        "CreatorMLMemberAbilities": (MLMemberAbilities, False),
        "CreatorMemberAbilities": ([str], False),
        "CreatorPaymentConfiguration": (PaymentConfiguration, False),
        "DataEncryptionMetadata": (DataEncryptionMetadata, False),
        "Description": (str, True),
        "JobLogStatus": (str, False),
        "Members": ([MemberSpecification], False),
        "Name": (str, True),
        "QueryLogStatus": (str, True),
        "Tags": (Tags, False),
    }


class AggregateColumn(AWSProperty):
    """
    `AggregateColumn <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html>`__
    """

    props: PropsDictType = {
        "ColumnNames": ([str], True),
        "Function": (str, True),
    }


class AggregationConstraint(AWSProperty):
    """
    `AggregationConstraint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html>`__
    """

    props: PropsDictType = {
        "ColumnName": (str, True),
        "Minimum": (double, True),
        "Type": (str, True),
    }


class AnalysisRuleAggregation(AWSProperty):
    """
    `AnalysisRuleAggregation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html>`__
    """

    props: PropsDictType = {
        "AdditionalAnalyses": (str, False),
        "AggregateColumns": ([AggregateColumn], True),
        "AllowedJoinOperators": ([str], False),
        "DimensionColumns": ([str], True),
        "JoinColumns": ([str], True),
        "JoinRequired": (str, False),
        "OutputConstraints": ([AggregationConstraint], True),
        "ScalarFunctions": ([str], True),
    }


class DifferentialPrivacyColumn(AWSProperty):
    """
    `DifferentialPrivacyColumn <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-differentialprivacycolumn.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
    }


class DifferentialPrivacy(AWSProperty):
    """
    `DifferentialPrivacy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-differentialprivacy.html>`__
    """

    props: PropsDictType = {
        "Columns": ([DifferentialPrivacyColumn], True),
    }


class AnalysisRuleCustom(AWSProperty):
    """
    `AnalysisRuleCustom <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html>`__
    """

    props: PropsDictType = {
        "AdditionalAnalyses": (str, False),
        "AllowedAnalyses": ([str], True),
        "AllowedAnalysisProviders": ([str], False),
        "DifferentialPrivacy": (DifferentialPrivacy, False),
        "DisallowedOutputColumns": ([str], False),
    }


class AnalysisRuleList(AWSProperty):
    """
    `AnalysisRuleList <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html>`__
    """

    props: PropsDictType = {
        "AdditionalAnalyses": (str, False),
        "AllowedJoinOperators": ([str], False),
        "JoinColumns": ([str], True),
        "ListColumns": ([str], True),
    }


class ConfiguredTableAnalysisRulePolicyV1(AWSProperty):
    """
    `ConfiguredTableAnalysisRulePolicyV1 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html>`__
    """

    props: PropsDictType = {
        "Aggregation": (AnalysisRuleAggregation, False),
        "Custom": (AnalysisRuleCustom, False),
        "List": (AnalysisRuleList, False),
    }


class ConfiguredTableAnalysisRulePolicy(AWSProperty):
    """
    `ConfiguredTableAnalysisRulePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy.html>`__
    """

    props: PropsDictType = {
        "V1": (ConfiguredTableAnalysisRulePolicyV1, True),
    }


class AnalysisRule(AWSProperty):
    """
    `AnalysisRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrule.html>`__
    """

    props: PropsDictType = {
        "Policy": (ConfiguredTableAnalysisRulePolicy, True),
        "Type": (str, True),
    }


class AthenaTableReference(AWSProperty):
    """
    `AthenaTableReference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-athenatablereference.html>`__
    """

    props: PropsDictType = {
        "DatabaseName": (str, True),
        "OutputLocation": (str, False),
        "TableName": (str, True),
        "WorkGroup": (str, True),
    }


class GlueTableReference(AWSProperty):
    """
    `GlueTableReference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-gluetablereference.html>`__
    """

    props: PropsDictType = {
        "DatabaseName": (str, True),
        "TableName": (str, True),
    }


class SnowflakeTableSchemaV1(AWSProperty):
    """
    `SnowflakeTableSchemaV1 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketableschemav1.html>`__
    """

    props: PropsDictType = {
        "ColumnName": (str, True),
        "ColumnType": (str, True),
    }


class SnowflakeTableSchema(AWSProperty):
    """
    `SnowflakeTableSchema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketableschema.html>`__
    """

    props: PropsDictType = {
        "V1": ([SnowflakeTableSchemaV1], True),
    }


class SnowflakeTableReference(AWSProperty):
    """
    `SnowflakeTableReference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketablereference.html>`__
    """

    props: PropsDictType = {
        "AccountIdentifier": (str, True),
        "DatabaseName": (str, True),
        "SchemaName": (str, True),
        "SecretArn": (str, True),
        "TableName": (str, True),
        "TableSchema": (SnowflakeTableSchema, True),
    }


class TableReference(AWSProperty):
    """
    `TableReference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-tablereference.html>`__
    """

    props: PropsDictType = {
        "Athena": (AthenaTableReference, False),
        "Glue": (GlueTableReference, False),
        "Snowflake": (SnowflakeTableReference, False),
    }


class ConfiguredTable(AWSObject):
    """
    `ConfiguredTable <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html>`__
    """

    resource_type = "AWS::CleanRooms::ConfiguredTable"

    props: PropsDictType = {
        "AllowedColumns": ([str], True),
        "AnalysisMethod": (str, True),
        "AnalysisRules": ([AnalysisRule], False),
        "Description": (str, False),
        "Name": (str, True),
        "SelectedAnalysisMethods": ([str], False),
        "TableReference": (TableReference, True),
        "Tags": (Tags, False),
    }


class ConfiguredTableAssociationAnalysisRuleAggregation(AWSProperty):
    """
    `ConfiguredTableAssociationAnalysisRuleAggregation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation.html>`__
    """

    props: PropsDictType = {
        "AllowedAdditionalAnalyses": ([str], False),
        "AllowedResultReceivers": ([str], False),
    }


class ConfiguredTableAssociationAnalysisRuleCustom(AWSProperty):
    """
    `ConfiguredTableAssociationAnalysisRuleCustom <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulecustom.html>`__
    """

    props: PropsDictType = {
        "AllowedAdditionalAnalyses": ([str], False),
        "AllowedResultReceivers": ([str], False),
    }


class ConfiguredTableAssociationAnalysisRuleList(AWSProperty):
    """
    `ConfiguredTableAssociationAnalysisRuleList <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulelist.html>`__
    """

    props: PropsDictType = {
        "AllowedAdditionalAnalyses": ([str], False),
        "AllowedResultReceivers": ([str], False),
    }


class ConfiguredTableAssociationAnalysisRulePolicyV1(AWSProperty):
    """
    `ConfiguredTableAssociationAnalysisRulePolicyV1 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1.html>`__
    """

    props: PropsDictType = {
        "Aggregation": (ConfiguredTableAssociationAnalysisRuleAggregation, False),
        "Custom": (ConfiguredTableAssociationAnalysisRuleCustom, False),
        "List": (ConfiguredTableAssociationAnalysisRuleList, False),
    }


class ConfiguredTableAssociationAnalysisRulePolicy(AWSProperty):
    """
    `ConfiguredTableAssociationAnalysisRulePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy.html>`__
    """

    props: PropsDictType = {
        "V1": (ConfiguredTableAssociationAnalysisRulePolicyV1, True),
    }


class ConfiguredTableAssociationAnalysisRule(AWSProperty):
    """
    `ConfiguredTableAssociationAnalysisRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule.html>`__
    """

    props: PropsDictType = {
        "Policy": (ConfiguredTableAssociationAnalysisRulePolicy, True),
        "Type": (str, True),
    }


class ConfiguredTableAssociation(AWSObject):
    """
    `ConfiguredTableAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html>`__
    """

    resource_type = "AWS::CleanRooms::ConfiguredTableAssociation"

    props: PropsDictType = {
        "ConfiguredTableAssociationAnalysisRules": (
            [ConfiguredTableAssociationAnalysisRule],
            False,
        ),
        "ConfiguredTableIdentifier": (str, True),
        "Description": (str, False),
        "MembershipIdentifier": (str, True),
        "Name": (str, True),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
    }


class IdMappingTableInputReferenceConfig(AWSProperty):
    """
    `IdMappingTableInputReferenceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig.html>`__
    """

    props: PropsDictType = {
        "InputReferenceArn": (str, True),
        "ManageResourcePolicies": (boolean, True),
    }


class IdMappingTable(AWSObject):
    """
    `IdMappingTable <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idmappingtable.html>`__
    """

    resource_type = "AWS::CleanRooms::IdMappingTable"

    props: PropsDictType = {
        "Description": (str, False),
        "InputReferenceConfig": (IdMappingTableInputReferenceConfig, True),
        "KmsKeyArn": (str, False),
        "MembershipIdentifier": (str, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class IdMappingConfig(AWSProperty):
    """
    `IdMappingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idmappingconfig.html>`__
    """

    props: PropsDictType = {
        "AllowUseAsDimensionColumn": (boolean, True),
    }


class IdNamespaceAssociationInputReferenceConfig(AWSProperty):
    """
    `IdNamespaceAssociationInputReferenceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig.html>`__
    """

    props: PropsDictType = {
        "InputReferenceArn": (str, True),
        "ManageResourcePolicies": (boolean, True),
    }


class IdNamespaceAssociation(AWSObject):
    """
    `IdNamespaceAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idnamespaceassociation.html>`__
    """

    resource_type = "AWS::CleanRooms::IdNamespaceAssociation"

    props: PropsDictType = {
        "Description": (str, False),
        "IdMappingConfig": (IdMappingConfig, False),
        "InputReferenceConfig": (IdNamespaceAssociationInputReferenceConfig, True),
        "MembershipIdentifier": (str, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class MembershipJobComputePaymentConfig(AWSProperty):
    """
    `MembershipJobComputePaymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipjobcomputepaymentconfig.html>`__
    """

    props: PropsDictType = {
        "IsResponsible": (boolean, True),
    }


class MembershipModelInferencePaymentConfig(AWSProperty):
    """
    `MembershipModelInferencePaymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipmodelinferencepaymentconfig.html>`__
    """

    props: PropsDictType = {
        "IsResponsible": (boolean, True),
    }


class MembershipModelTrainingPaymentConfig(AWSProperty):
    """
    `MembershipModelTrainingPaymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipmodeltrainingpaymentconfig.html>`__
    """

    props: PropsDictType = {
        "IsResponsible": (boolean, True),
    }


class MembershipMLPaymentConfig(AWSProperty):
    """
    `MembershipMLPaymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipmlpaymentconfig.html>`__
    """

    props: PropsDictType = {
        "ModelInference": (MembershipModelInferencePaymentConfig, False),
        "ModelTraining": (MembershipModelTrainingPaymentConfig, False),
    }


class MembershipQueryComputePaymentConfig(AWSProperty):
    """
    `MembershipQueryComputePaymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipquerycomputepaymentconfig.html>`__
    """

    props: PropsDictType = {
        "IsResponsible": (boolean, True),
    }


class MembershipPaymentConfiguration(AWSProperty):
    """
    `MembershipPaymentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershippaymentconfiguration.html>`__
    """

    props: PropsDictType = {
        "JobCompute": (MembershipJobComputePaymentConfig, False),
        "MachineLearning": (MembershipMLPaymentConfig, False),
        "QueryCompute": (MembershipQueryComputePaymentConfig, True),
    }


class ProtectedJobS3OutputConfigurationInput(AWSProperty):
    """
    `ProtectedJobS3OutputConfigurationInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "KeyPrefix": (str, False),
    }


class MembershipProtectedJobOutputConfiguration(AWSProperty):
    """
    `MembershipProtectedJobOutputConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedjoboutputconfiguration.html>`__
    """

    props: PropsDictType = {
        "S3": (ProtectedJobS3OutputConfigurationInput, True),
    }


class MembershipProtectedJobResultConfiguration(AWSProperty):
    """
    `MembershipProtectedJobResultConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration.html>`__
    """

    props: PropsDictType = {
        "OutputConfiguration": (MembershipProtectedJobOutputConfiguration, True),
        "RoleArn": (str, True),
    }


class ProtectedQueryS3OutputConfiguration(AWSProperty):
    """
    `ProtectedQueryS3OutputConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "KeyPrefix": (str, False),
        "ResultFormat": (str, True),
        "SingleFileOutput": (boolean, False),
    }


class MembershipProtectedQueryOutputConfiguration(AWSProperty):
    """
    `MembershipProtectedQueryOutputConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration.html>`__
    """

    props: PropsDictType = {
        "S3": (ProtectedQueryS3OutputConfiguration, True),
    }


class MembershipProtectedQueryResultConfiguration(AWSProperty):
    """
    `MembershipProtectedQueryResultConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration.html>`__
    """

    props: PropsDictType = {
        "OutputConfiguration": (MembershipProtectedQueryOutputConfiguration, True),
        "RoleArn": (str, False),
    }


class Membership(AWSObject):
    """
    `Membership <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html>`__
    """

    resource_type = "AWS::CleanRooms::Membership"

    props: PropsDictType = {
        "CollaborationIdentifier": (str, True),
        "DefaultJobResultConfiguration": (
            MembershipProtectedJobResultConfiguration,
            False,
        ),
        "DefaultResultConfiguration": (
            MembershipProtectedQueryResultConfiguration,
            False,
        ),
        "JobLogStatus": (str, False),
        "PaymentConfiguration": (MembershipPaymentConfiguration, False),
        "QueryLogStatus": (str, True),
        "Tags": (Tags, False),
    }


class Parameters(AWSProperty):
    """
    `Parameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-privacybudgettemplate-parameters.html>`__
    """

    props: PropsDictType = {
        "Epsilon": (integer, True),
        "UsersNoisePerQuery": (integer, True),
    }


class PrivacyBudgetTemplate(AWSObject):
    """
    `PrivacyBudgetTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-privacybudgettemplate.html>`__
    """

    resource_type = "AWS::CleanRooms::PrivacyBudgetTemplate"

    props: PropsDictType = {
        "AutoRefresh": (str, True),
        "MembershipIdentifier": (str, True),
        "Parameters": (Parameters, True),
        "PrivacyBudgetType": (str, True),
        "Tags": (Tags, False),
    }


class IdMappingTableInputSource(AWSProperty):
    """
    `IdMappingTableInputSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource.html>`__
    """

    props: PropsDictType = {
        "IdNamespaceAssociationId": (str, True),
        "Type": (str, True),
    }


class IdMappingTableInputReferenceProperties(AWSProperty):
    """
    `IdMappingTableInputReferenceProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties.html>`__
    """

    props: PropsDictType = {
        "IdMappingTableInputSource": ([IdMappingTableInputSource], True),
    }


class IdNamespaceAssociationInputReferenceProperties(AWSProperty):
    """
    `IdNamespaceAssociationInputReferenceProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties.html>`__
    """

    props: PropsDictType = {
        "IdMappingWorkflowsSupported": (Tags, False),
        "IdNamespaceType": (str, False),
    }

from __future__ import annotations

from aws_cdk import aws_organizations as organizations
from aws_cdk import Stack
from constructs import Construct


class OrganizationStack(Stack):

    FEATURE_SET = "ALL"

    def construct_organization(self, org_name: str, feature_set: str):
        cfn_organization = organizations.CfnOrganization(self, org_name, feature_set=feature_set)

        return cfn_organization

    def __init__(self, scope: Construct, construct_id: str, org_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.construct_organization(org_name, self.FEATURE_SET)

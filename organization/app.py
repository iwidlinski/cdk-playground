#!/usr/bin/env python3
from __future__ import annotations

import aws_cdk as cdk

from organization.organization_stack import OrganizationStack


app = cdk.App()
OrganizationStack(app, "OrganizationStack", org_name="WIDLINSKI")

app.synth()

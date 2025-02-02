from __future__ import annotations

import aws_cdk as core
import aws_cdk.assertions as assertions

from reports.reports_stack import ReportsStack


# example tests. To run these tests, uncomment this file along with the example
# resource in reports/reports_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ReportsStack(app, "reports")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

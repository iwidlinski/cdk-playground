from __future__ import annotations

import aws_cdk as core
import aws_cdk.assertions as assertions

from essential_budgets.essential_budgets_stack import EssentialBudgetsStack


# example tests. To run these tests, uncomment this file along with the example
# resource in essential_budgets/essential_budgets_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EssentialBudgetsStack(app, "essential-budgets")
    assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

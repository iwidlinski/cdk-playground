#!/usr/bin/env python3
from __future__ import annotations

import aws_cdk as cdk

from essential_budgets.essential_budgets_stack import EssentialBudgetsStack

subscribers = ["aws1-budgets@widlin.ski"]

app = cdk.App()
EssentialBudgetsStack(
    app,
    "ZeroSpendBudget",
    budget_name="ZeroSpendBudget",
    budget_limit=1,
    threshold=0.01,
    subscribers=subscribers,
)
EssentialBudgetsStack(
    app,
    "MinimalSpendBudget",
    budget_name="MinimalSpendBudget",
    budget_limit=10,
    threshold=10,
    subscribers=subscribers,
)

app.synth()

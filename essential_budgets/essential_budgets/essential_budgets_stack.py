from __future__ import annotations

from aws_cdk import aws_budgets as budgets
from aws_cdk import Stack
from constructs import Construct

UNIT = "USD"


def construct_notification_property(threshold: float):
    notification = budgets.CfnBudget.NotificationProperty(
        comparison_operator="GREATER_THAN",
        notification_type="ACTUAL",
        threshold=threshold,
        threshold_type="ABSOLUTE_VALUE",
    )

    return notification


def construct_subscriber_property(subscriber: str):
    subscriber = budgets.CfnBudget.SubscriberProperty(address=subscriber, subscription_type="EMAIL")

    return subscriber


def construct_notification_with_subscribers_property(subscribers: list, threshold: float):

    subscribers_property = []
    for subscriber in subscribers:
        subscriber_property = construct_subscriber_property(subscriber=subscriber)
        subscribers_property.append(subscriber_property)

    notification_property = construct_notification_property(threshold=threshold)

    notification_with_subscribers_property = budgets.CfnBudget.NotificationWithSubscribersProperty(
        notification=notification_property,
        subscribers=subscribers_property,
    )

    return notification_with_subscribers_property


def construct_spend_property(budget_limit: float):
    spend_property = budgets.CfnBudget.SpendProperty(amount=budget_limit, unit=UNIT)

    return spend_property


def construct_cost_types_property():
    cost_types = budgets.CfnBudget.CostTypesProperty(
        include_credit=False,
        include_discount=True,
        include_other_subscription=True,
        include_recurring=True,
        include_refund=False,
        include_subscription=True,
        include_support=True,
        include_tax=True,
        include_upfront=True,
        use_amortized=False,
        use_blended=False,
    )
    return cost_types


def construct_budget_data_property(budget_limit: float, budget_name: str):

    spend_property = construct_spend_property(budget_limit=budget_limit)
    cost_types = construct_cost_types_property()
    bdp = budgets.CfnBudget.BudgetDataProperty(
        budget_type="COST",
        time_unit="MONTHLY",
        budget_limit=spend_property,
        budget_name=budget_name,
        cost_types=cost_types,
    )

    return bdp


class EssentialBudgetsStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        budget_name: str,
        budget_limit: float,
        threshold: float,
        subscribers: list,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        notifications_with_subscribers = construct_notification_with_subscribers_property(
            subscribers=subscribers,
            threshold=threshold,
        )
        bdp = construct_budget_data_property(budget_limit=budget_limit, budget_name=budget_name)

        budgets.CfnBudget(
            self,
            budget_name,
            budget=bdp,
            notifications_with_subscribers=[notifications_with_subscribers],
        )

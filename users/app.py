#!/usr/bin/env python3
from __future__ import annotations

import logging

from aws_cdk import App
from aws_cdk import Environment

from users.users_stack import UsersStack

logger = logging.getLogger(__name__)
loghandler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
loghandler.setFormatter(formatter)
logger.addHandler(loghandler)
logger.setLevel(logging.DEBUG)

app = App()
profile = app.node.try_get_context("profile")
account_id = app.node.try_get_context("accountID")
region_name = app.node.try_get_context("region")

env_info = Environment(account=account_id, region=region_name)
logger.debug(env_info)

UsersStack(app, "UsersStack", username="admin", env=env_info)
UsersStack(app, "UsersStack-john", username="john", env=env_info)
app.synth()

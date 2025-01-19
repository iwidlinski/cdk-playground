#!/usr/bin/env python3
from __future__ import annotations

import logging

from aws_cdk import App

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

UsersStack(app, "UsersStack-admin", username="admin", role="AdministratorAccess")
UsersStack(app, "UsersStack-john", username="john", role="AdministratorAccess")
app.synth()

from __future__ import annotations

import logging

from aws_cdk import aws_iam as iam
from aws_cdk import aws_secretsmanager as secretsmanager
from aws_cdk import Stack
from constructs import Construct


logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)


class UsersStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        username: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        user = iam.User(self, username, user_name=username)
        user.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AdministratorAccess",
            ),
        )
        access_key = iam.AccessKey(self, "AccessKey", user=user)
        secretsmanager.Secret(
            self,
            id=f"{username}-key",
            secret_name=f"{username}-{access_key.access_key_id}-secret-key",
            secret_string_value=access_key.secret_access_key,
        )
        # example resource
        # queue = sqs.Queue(
        #     self, "UsersQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

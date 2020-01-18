# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=unused-argument

from knack.util import CLIError


def plan_list(cmd, client, resource_group_name=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()

def plan_show(cmd, client, resource_group_name, plan_name):
    return client.get(resource_group_name=resource_group_name, plan_name=plan_name)

def plan_create(cmd, client, resource_group_name, plan_name, location, tags=None):
    raise CLIError('TODO: Implement `vso plan create`')

def plan_get_token(cmd, client, resource_group_name, plan_name):
    raise CLIError('TODO: Implement `vso plan get-token`')

def env_list(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `vso env list`')
def env_create(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `vso env create`')
def env_open(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `vso env open`')

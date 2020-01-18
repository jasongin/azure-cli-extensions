# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from ._client_factory import cf_vso
from ._client_factory import cf_vso_plan


def load_command_table(self, _):

    # vso_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#None.{}',
    #    client_factory=cf_vso)
    vso_operations = CliCommandType(
        operations_tmpl='azext_vso.vendored_sdks.vsonline.operations.plan_operations#PlanOperations.{}',
        client_factory=cf_vso)

    with self.command_group('vso plan', vso_operations, client_factory=cf_vso_plan) as g:
        g.custom_command('list', 'plan_list')
        g.custom_command('show', 'plan_show')
        g.custom_command('create', 'plan_create')
        #g.command('delete', 'delete')
        #g.custom_command('get-token', 'plan_get_token')

    with self.command_group('vso env') as g:
        g.custom_command('list', 'env_list')
        g.custom_command('create', 'env_create')
        g.custom_command('open', 'env_open')

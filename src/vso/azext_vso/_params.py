# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type, get_resource_name_completion_list
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    name_arg_type = CLIArgumentType(options_list=['--name', '-n'], metavar='NAME')
    plan_name_help = 'Name of the VS Online plan resource. You can configure the default using `az configure --defaults vso-plan=<name>`'
    plan_name_completer = get_resource_name_completion_list('Microsoft.VSOnline/plans')
    new_plan_name_arg_type = CLIArgumentType(overrides=name_arg_type, configured_default='vso-plan', help=plan_name_help)
    existing_plan_name_arg_type = CLIArgumentType(overrides=name_arg_type,
                                                  configured_default='vso-plan',
                                                  help=plan_name_help,
                                                  completer=plan_name_completer,
                                                  id_part='name')

    with self.argument_context('vso plan') as c:
        c.argument('plan_name', existing_plan_name_arg_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)

    with self.argument_context('vso plan create') as c:
        c.argument('plan_name', new_plan_name_arg_type)

    with self.argument_context('vso env') as c:
        c.argument('plan_name', existing_plan_name_arg_type)

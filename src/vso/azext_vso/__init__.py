# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

from azext_vso._help import helps  # pylint: disable=unused-import


class VsoCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_vso._client_factory import cf_vso
        vso_custom = CliCommandType(
            operations_tmpl='azext_vso.custom#{}',
            client_factory=cf_vso)
        super(VsoCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                  custom_command_type=vso_custom)

    def load_command_table(self, args):
        from azext_vso.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_vso._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = VsoCommandsLoader

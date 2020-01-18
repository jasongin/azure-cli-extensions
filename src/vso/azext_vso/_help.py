# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import


helps['vso'] = """
    type: group
    short-summary: Commands to manage VS Online plans and environments.
"""

helps['vso plan'] = """
    type: group
    short-summary: Commands to manage VS Online plans.
"""

helps['vso plan list'] = """
     type: command
     short-summary: List all VS Online plans in the current subscription.
"""

helps['vso plan set'] = """
     type: command
     short-summary: Set a VS Online plan to be the current active plan.
"""

helps['vso plan show'] = """
     type: command
     short-summary: Get the details of a VS Online plan.
"""

helps['vso plan create'] = """
     type: command
     short-summary: Create a VS Online plan.
"""

helps['vso plan delete'] = """
     type: command
     short-summary: Delete a VS Online plan.
"""

helps['vso plan get-token'] = """
     type: command
     short-summary: Get an access token for a VS Online plan.
"""

helps['vso env'] = """
    type: group
    short-summary: Commands to manage VS Online Environments.
"""

helps['vso env list'] = """
     type: command
     short-summary: List all VS Online environments in the current plan.
"""

helps['vso env show'] = """
     type: command
     short-summary: Get the details of a VS Online environment.
"""

helps['vso env create'] = """
     type: command
     short-summary: Create a VS Online environment.
"""

helps['vso env delete'] = """
     type: command
     short-summary: Delete a VS Online environment.
"""

helps['vso env open'] = """
     type: command
     short-summary: Open a VS Online environment in the browser.
"""

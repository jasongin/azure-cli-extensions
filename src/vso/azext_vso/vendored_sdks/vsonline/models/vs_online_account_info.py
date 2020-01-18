# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VSOnlineAccountInfo(Model):
    """VS Online Account properties. Holds properties that describe the account.

    :param sku: SKU of the service.
    :type sku: ~microsoft.vsonline.models.Sku
    """

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, **kwargs):
        super(VSOnlineAccountInfo, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)

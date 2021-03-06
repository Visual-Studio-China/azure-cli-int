# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class Formula(Model):
    """A formula for creating a VM, specifying an image base and other parameters.

    :param description: The description of the formula.
    :type description: str
    :param author: The author of the formula.
    :type author: str
    :param os_type: The OS type of the formula.
    :type os_type: str
    :param creation_date: The creation date of the formula.
    :type creation_date: datetime
    :param formula_content: The content of the formula.
    :type formula_content: :class:`LabVirtualMachineCreationParameter
     <azure.mgmt.devtestlabs.models.LabVirtualMachineCreationParameter>`
    :param vm: Information about a VM from which a formula is to be created.
    :type vm: :class:`FormulaPropertiesFromVm
     <azure.mgmt.devtestlabs.models.FormulaPropertiesFromVm>`
    :param provisioning_state: The provisioning status of the resource.
    :type provisioning_state: str
    :param unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :type unique_identifier: str
    :param id: The identifier of the resource.
    :type id: str
    :param name: The name of the resource.
    :type name: str
    :param type: The type of the resource.
    :type type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    """

    _attribute_map = {
        'description': {'key': 'properties.description', 'type': 'str'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'formula_content': {'key': 'properties.formulaContent', 'type': 'LabVirtualMachineCreationParameter'},
        'vm': {'key': 'properties.vm', 'type': 'FormulaPropertiesFromVm'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, description=None, author=None, os_type=None, creation_date=None, formula_content=None, vm=None, provisioning_state=None, unique_identifier=None, id=None, name=None, type=None, location=None, tags=None):
        self.description = description
        self.author = author
        self.os_type = os_type
        self.creation_date = creation_date
        self.formula_content = formula_content
        self.vm = vm
        self.provisioning_state = provisioning_state
        self.unique_identifier = unique_identifier
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.tags = tags

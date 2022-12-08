# coding: utf-8

"""
    Console API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.0.2
    Generated by: https://openapi-generator.tech
"""

from aitrios_console_rest_client_sdk_primitive.paths.models_model_id.delete import DeleteModelFunc
from aitrios_console_rest_client_sdk_primitive.paths.models_model_id_base.get import GetBaseModelStatusFunc
from aitrios_console_rest_client_sdk_primitive.paths.models.get import GetModelsFunc
from aitrios_console_rest_client_sdk_primitive.paths.models.post import ImportBaseModelFunc
from aitrios_console_rest_client_sdk_primitive.paths.models_model_id.post import ImportNonConvertedModelFunc


class TrainModelApi(
    DeleteModelFunc,
    GetBaseModelStatusFunc,
    GetModelsFunc,
    ImportBaseModelFunc,
    ImportNonConvertedModelFunc,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

# coding: utf-8

"""
    Console API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.0.2
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from aitrios_console_rest_client_sdk_primitive import schemas  # noqa: F401


class ImportDeviceAppJsonBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ImportDeviceApp Json Body
    """


    class MetaOapg:
        required = {
            "app_name",
            "file_content",
            "compiled_flg",
            "file_name",
            "version_number",
        }
        
        class properties:
            compiled_flg = schemas.StrSchema
            app_name = schemas.StrSchema
            version_number = schemas.StrSchema
            file_name = schemas.StrSchema
            file_content = schemas.StrSchema
            entry_point = schemas.StrSchema
            comment = schemas.StrSchema
            __annotations__ = {
                "compiled_flg": compiled_flg,
                "app_name": app_name,
                "version_number": version_number,
                "file_name": file_name,
                "file_content": file_content,
                "entry_point": entry_point,
                "comment": comment,
            }
    
    app_name: MetaOapg.properties.app_name
    file_content: MetaOapg.properties.file_content
    compiled_flg: MetaOapg.properties.compiled_flg
    file_name: MetaOapg.properties.file_name
    version_number: MetaOapg.properties.version_number
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compiled_flg"]) -> MetaOapg.properties.compiled_flg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_name"]) -> MetaOapg.properties.app_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_number"]) -> MetaOapg.properties.version_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_content"]) -> MetaOapg.properties.file_content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entry_point"]) -> MetaOapg.properties.entry_point: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["compiled_flg", "app_name", "version_number", "file_name", "file_content", "entry_point", "comment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compiled_flg"]) -> MetaOapg.properties.compiled_flg: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_name"]) -> MetaOapg.properties.app_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_number"]) -> MetaOapg.properties.version_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_content"]) -> MetaOapg.properties.file_content: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entry_point"]) -> typing.Union[MetaOapg.properties.entry_point, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["compiled_flg", "app_name", "version_number", "file_name", "file_content", "entry_point", "comment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        app_name: typing.Union[MetaOapg.properties.app_name, str, ],
        file_content: typing.Union[MetaOapg.properties.file_content, str, ],
        compiled_flg: typing.Union[MetaOapg.properties.compiled_flg, str, ],
        file_name: typing.Union[MetaOapg.properties.file_name, str, ],
        version_number: typing.Union[MetaOapg.properties.version_number, str, ],
        entry_point: typing.Union[MetaOapg.properties.entry_point, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImportDeviceAppJsonBody':
        return super().__new__(
            cls,
            *args,
            app_name=app_name,
            file_content=file_content,
            compiled_flg=compiled_flg,
            file_name=file_name,
            version_number=version_number,
            entry_point=entry_point,
            comment=comment,
            _configuration=_configuration,
            **kwargs,
        )

# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from aitrios_console_rest_client_sdk_primitive import api_client, exceptions
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

from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.inference import Inference

# query params
NumberOfInferenceresultsSchema = schemas.IntSchema
FilterSchema = schemas.StrSchema
RawSchema = schemas.IntSchema
TimeSchema = schemas.StrSchema
# path params
DeviceIdSchema = schemas.StrSchema


class SchemaFor200ResponseBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    id = schemas.StrSchema
                    device_id = schemas.StrSchema
                    model_id = schemas.StrSchema
                    version_number = schemas.StrSchema
                    model_version_id = schemas.StrSchema
                    model_type = schemas.StrSchema
                    training_kit_name = schemas.StrSchema
                    _ts = schemas.IntSchema
                    
                    
                    class inference_result(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                DeviceID = schemas.StrSchema
                                ModelID = schemas.StrSchema
                                Image = schemas.BoolSchema
                                
                                
                                class Inferences(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def items() -> typing.Type['Inference']:
                                            return Inference
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple['Inference'], typing.List['Inference']],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'Inferences':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> 'Inference':
                                        return super().__getitem__(i)
                                id = schemas.StrSchema
                                ttl = schemas.IntSchema
                                _rid = schemas.StrSchema
                                _self = schemas.StrSchema
                                _etag = schemas.StrSchema
                                _attachments = schemas.StrSchema
                                _ts = schemas.IntSchema
                                __annotations__ = {
                                    "DeviceID": DeviceID,
                                    "ModelID": ModelID,
                                    "Image": Image,
                                    "Inferences": Inferences,
                                    "id": id,
                                    "ttl": ttl,
                                    "_rid": _rid,
                                    "_self": _self,
                                    "_etag": _etag,
                                    "_attachments": _attachments,
                                    "_ts": _ts,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["DeviceID"]) -> MetaOapg.properties.DeviceID: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ModelID"]) -> MetaOapg.properties.ModelID: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Image"]) -> MetaOapg.properties.Image: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["Inferences"]) -> MetaOapg.properties.Inferences: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ttl"]) -> MetaOapg.properties.ttl: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["_rid"]) -> MetaOapg.properties._rid: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["_self"]) -> MetaOapg.properties._self: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["_etag"]) -> MetaOapg.properties._etag: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["_attachments"]) -> MetaOapg.properties._attachments: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["_ts"]) -> MetaOapg.properties._ts: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["DeviceID", "ModelID", "Image", "Inferences", "id", "ttl", "_rid", "_self", "_etag", "_attachments", "_ts", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["DeviceID"]) -> typing.Union[MetaOapg.properties.DeviceID, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ModelID"]) -> typing.Union[MetaOapg.properties.ModelID, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Image"]) -> typing.Union[MetaOapg.properties.Image, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["Inferences"]) -> typing.Union[MetaOapg.properties.Inferences, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ttl"]) -> typing.Union[MetaOapg.properties.ttl, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["_rid"]) -> typing.Union[MetaOapg.properties._rid, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["_self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["_etag"]) -> typing.Union[MetaOapg.properties._etag, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["_attachments"]) -> typing.Union[MetaOapg.properties._attachments, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["_ts"]) -> typing.Union[MetaOapg.properties._ts, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["DeviceID", "ModelID", "Image", "Inferences", "id", "ttl", "_rid", "_self", "_etag", "_attachments", "_ts", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            DeviceID: typing.Union[MetaOapg.properties.DeviceID, str, schemas.Unset] = schemas.unset,
                            ModelID: typing.Union[MetaOapg.properties.ModelID, str, schemas.Unset] = schemas.unset,
                            Image: typing.Union[MetaOapg.properties.Image, bool, schemas.Unset] = schemas.unset,
                            Inferences: typing.Union[MetaOapg.properties.Inferences, list, tuple, schemas.Unset] = schemas.unset,
                            id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                            ttl: typing.Union[MetaOapg.properties.ttl, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _rid: typing.Union[MetaOapg.properties._rid, str, schemas.Unset] = schemas.unset,
                            _self: typing.Union[MetaOapg.properties._self, str, schemas.Unset] = schemas.unset,
                            _etag: typing.Union[MetaOapg.properties._etag, str, schemas.Unset] = schemas.unset,
                            _attachments: typing.Union[MetaOapg.properties._attachments, str, schemas.Unset] = schemas.unset,
                            _ts: typing.Union[MetaOapg.properties._ts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'inference_result':
                            return super().__new__(
                                cls,
                                *args,
                                DeviceID=DeviceID,
                                ModelID=ModelID,
                                Image=Image,
                                Inferences=Inferences,
                                id=id,
                                ttl=ttl,
                                _rid=_rid,
                                _self=_self,
                                _etag=_etag,
                                _attachments=_attachments,
                                _ts=_ts,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class inferences(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Inference']:
                                return Inference
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['Inference'], typing.List['Inference']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'inferences':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Inference':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "id": id,
                        "device_id": device_id,
                        "model_id": model_id,
                        "version_number": version_number,
                        "model_version_id": model_version_id,
                        "model_type": model_type,
                        "training_kit_name": training_kit_name,
                        "_ts": _ts,
                        "inference_result": inference_result,
                        "inferences": inferences,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["model_id"]) -> MetaOapg.properties.model_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["version_number"]) -> MetaOapg.properties.version_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["model_version_id"]) -> MetaOapg.properties.model_version_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["model_type"]) -> MetaOapg.properties.model_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["training_kit_name"]) -> MetaOapg.properties.training_kit_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["_ts"]) -> MetaOapg.properties._ts: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["inference_result"]) -> MetaOapg.properties.inference_result: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["inferences"]) -> MetaOapg.properties.inferences: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "device_id", "model_id", "version_number", "model_version_id", "model_type", "training_kit_name", "_ts", "inference_result", "inferences", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["model_id"]) -> typing.Union[MetaOapg.properties.model_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["version_number"]) -> typing.Union[MetaOapg.properties.version_number, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["model_version_id"]) -> typing.Union[MetaOapg.properties.model_version_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["model_type"]) -> typing.Union[MetaOapg.properties.model_type, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["training_kit_name"]) -> typing.Union[MetaOapg.properties.training_kit_name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["_ts"]) -> typing.Union[MetaOapg.properties._ts, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["inference_result"]) -> typing.Union[MetaOapg.properties.inference_result, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["inferences"]) -> typing.Union[MetaOapg.properties.inferences, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "device_id", "model_id", "version_number", "model_version_id", "model_type", "training_kit_name", "_ts", "inference_result", "inferences", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                device_id: typing.Union[MetaOapg.properties.device_id, str, schemas.Unset] = schemas.unset,
                model_id: typing.Union[MetaOapg.properties.model_id, str, schemas.Unset] = schemas.unset,
                version_number: typing.Union[MetaOapg.properties.version_number, str, schemas.Unset] = schemas.unset,
                model_version_id: typing.Union[MetaOapg.properties.model_version_id, str, schemas.Unset] = schemas.unset,
                model_type: typing.Union[MetaOapg.properties.model_type, str, schemas.Unset] = schemas.unset,
                training_kit_name: typing.Union[MetaOapg.properties.training_kit_name, str, schemas.Unset] = schemas.unset,
                _ts: typing.Union[MetaOapg.properties._ts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                inference_result: typing.Union[MetaOapg.properties.inference_result, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                inferences: typing.Union[MetaOapg.properties.inferences, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    id=id,
                    device_id=device_id,
                    model_id=model_id,
                    version_number=version_number,
                    model_version_id=model_version_id,
                    model_type=model_type,
                    training_kit_name=training_kit_name,
                    _ts=_ts,
                    inference_result=inference_result,
                    inferences=inferences,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
SchemaFor400ResponseBodyApplicationJson = ErrorResponse
SchemaFor401ResponseBodyApplicationJson = ErrorResponse
SchemaFor403ResponseBodyApplicationJson = ErrorResponse
SchemaFor500ResponseBodyApplicationJson = ErrorResponse
SchemaFor503ResponseBodyApplicationJson = ErrorResponse
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_inference_results_oapg(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        GetInferenceResults
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_device_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_number_of_inferenceresults,
            request_query_filter,
            request_query_raw,
            request_query_time,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class GetInferenceResults(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def get_inference_results(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._get_inference_results_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def get(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._get_inference_results_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )



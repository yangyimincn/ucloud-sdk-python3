""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields
from ucloud.services.umon.schemas import models


class GetMetricRequestSchema(schema.RequestSchema):

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ResourceId": fields.Str(required=False, dump_to="ResourceId"),
        "ResourceType": fields.Str(required=True, dump_to="ResourceType"),
        "MetricName": fields.List(fields.Str()),
        "BeginTime": fields.Str(required=False, dump_to="BeginTime"),
        "EndTime": fields.Int(required=False, dump_to="EndTime"),
    }


class GetMetricResponseSchema(schema.ResponseSchema):
    fields = {
        "Action": fields.Str(required=True, load_from="Action"),
        "RetCode": fields.Int(required=True, load_from="RetCode"),
        "DataSets": fields.Dict(required=False, load_from="DataSets")
    }

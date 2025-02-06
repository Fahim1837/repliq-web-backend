from rest_framework import serializers as s

def unexpected_key_names(allowed, incoming):
    incoming_fields = set(incoming)
    allowed_fields = set(allowed)

    unexpected_fields = incoming_fields - allowed_fields

    if unexpected_fields:
        raise s.ValidationError(
            {field: "Unexpected field name." for field in unexpected_fields}
        )
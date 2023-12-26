schema_list_province_normal = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "rajaongkir": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "array",
                    "items": {}
                },
                "status": {
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "integer"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "code",
                        "description"
                    ]
                },
                "results": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "province_id": {
                                    "type": "string"
                                },
                                "province": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "province_id",
                                "province"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "province_id": {
                                    "type": "string"
                                },
                                "province": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "province_id",
                                "province"
                            ]
                        }
                    ]
                }
            },
            "required": [
                "query",
                "status",
                "results"
            ]
        }
    },
    "required": [
        "rajaongkir"
    ]
}

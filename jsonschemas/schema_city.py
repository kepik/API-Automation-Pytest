schema_list_city_normal = {
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
                                "city_id": {
                                    "type": "string"
                                },
                                "province_id": {
                                    "type": "string"
                                },
                                "province": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                },
                                "city_name": {
                                    "type": "string"
                                },
                                "postal_code": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "city_id",
                                "province_id",
                                "province",
                                "type",
                                "city_name",
                                "postal_code"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "city_id": {
                                    "type": "string"
                                },
                                "province_id": {
                                    "type": "string"
                                },
                                "province": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                },
                                "city_name": {
                                    "type": "string"
                                },
                                "postal_code": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "city_id",
                                "province_id",
                                "province",
                                "type",
                                "city_name",
                                "postal_code"
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

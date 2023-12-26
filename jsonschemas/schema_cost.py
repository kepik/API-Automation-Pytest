schema_list_cost_normal = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "rajaongkir": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string"
                        },
                        "destination": {
                            "type": "string"
                        },
                        "weight": {
                            "type": "integer"
                        },
                        "courier": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "origin",
                        "destination",
                        "weight",
                        "courier"
                    ]
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
                "origin_details": {
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
                "destination_details": {
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
                "results": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "code": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "costs": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "service": {
                                                    "type": "string"
                                                },
                                                "description": {
                                                    "type": "string"
                                                },
                                                "cost": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "value": {
                                                                    "type": "integer"
                                                                },
                                                                "etd": {
                                                                    "type": "string"
                                                                },
                                                                "note": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "value",
                                                                "etd",
                                                                "note"
                                                            ]
                                                        }
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "service",
                                                "description",
                                                "cost"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "code",
                                "name",
                                "costs"
                            ]
                        }
                    ]
                }
            },
            "required": [
                "query",
                "status",
                "origin_details",
                "destination_details",
                "results"
            ]
        }
    },
    "required": [
        "rajaongkir"
    ]
}
def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    obj_module = getattr(obj, 'module', '__main__')
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }
    return info


number_info = introspection_info(42)
print(number_info)

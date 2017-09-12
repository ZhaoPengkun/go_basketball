def init_module(api):
    from app.api.auth.resources import ns
    _add_model(ns)
    api.add_namespace(ns)


def _add_model(namespace):
    from app.api.auth import schemas
    for name in schemas.__all__:
        model = getattr(schemas, name)
        namespace.add_model(model.name, model)

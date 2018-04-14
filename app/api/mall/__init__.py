from app.api.mall.resources import ns
from app.api.mall import schemas


def init_module(api):
    _add_model(ns)
    api.add_namespace(ns)


def _add_model(namespace):
    for name in schemas.__all__:
        model = getattr(schemas, name)
        namespace.add_model(model.name, model)

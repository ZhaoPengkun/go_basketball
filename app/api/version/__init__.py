from app.api.version.resources import ns


def init_module(api):
    api.add_namespace(ns)

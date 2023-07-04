from importlib import reload

from .plugin import PluginBaseClass


def GetDefaultPlugins():
    from .online_documentation import plugin_online_documentation
    from .manual_documentation import plugin_manual_docs
    from .fb_property import fb_property_plugin
    from .dunder_methods import dunder_methods

    reload(plugin_online_documentation)
    reload(plugin_manual_docs)
    reload(fb_property_plugin)
    reload(dunder_methods)

    return (
        plugin_online_documentation.PluginOnlineDocumentation,
        plugin_manual_docs.PluginManualDocumentation,
        fb_property_plugin.PluginFbProperty,
        dunder_methods.PluginDunderMethods
    )

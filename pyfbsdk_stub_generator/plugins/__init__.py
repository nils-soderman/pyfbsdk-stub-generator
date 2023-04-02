from importlib import reload

from .plugin import PluginBaseClass

def GetDefaultPlugins():
    from .online_documentation import plugin_online_documentation
    reload(plugin_online_documentation)
    
    from .manual_documentation import PluginManualDocs

    return (
        plugin_online_documentation.PluginOnlineDocumentation,
        # PluginManualDocs
    )

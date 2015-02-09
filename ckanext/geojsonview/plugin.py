import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.resourceproxy.plugin as proxy
import ckan.lib.datapreview as datapreview

from ckan.common import json

class GeojsonviewPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IResourceView, inherit=True)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('public', 'ckanext-geojsonview')

    # IResourceView
    def info(self):
        return {
            'name': 'geojson_view',
            'title': 'Map View',
            'icon': 'globe',
            'iframed': True
        }

    def setup_template_variables(self, context, data_dict):
        proxified_url = proxy.get_proxified_resource_url(data_dict)

        return {
            'proxied_url': json.dumps(proxified_url)
        }

    def can_view(self, data_dict):
        return data_dict['resource'].get('format', '').lower() == 'geojson'

    def view_template(self, context, data_dict):
        return 'dataviewer/geojsonview.html'

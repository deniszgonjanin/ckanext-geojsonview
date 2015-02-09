import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


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
            'iframed': False
        }

    def can_view(self, data_dict):
        return data_dict['resource'].get('format', '').lower() == 'geojson':

    def view_template(self):
        return 'dataviewer/geojsonview.html'

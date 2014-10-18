import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.dasish.helpers as helpers

class DasishPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.ITemplateHelpers)

    def get_helpers(self):
        return{
               'featured_groups': helpers.featured_groups,
               'extras_to_exclude': helpers.extras_to_exclude
              }

    def update_config(self, config):
        toolkit.add_public_directory(config, 'public')
        toolkit.add_template_directory(config, 'templates')

    def dataset_facets(self, facets_dict, package_type):
        return self._facets(facets_dict)

    def group_facets(self, facets_dict, group_type, package_type):
        return self._facets(facets_dict)

    def organization_facets(self, facets_dict, organization_type,
                            package_type):
        return self._facets(facets_dict)

    def _facets(self, facets_dict):
        # Deleted facets
        if 'organization' in facets_dict:
            del facets_dict['organization']
        if 'license_id' in facets_dict:
            del facets_dict['license_id']
        if 'res_format' in facets_dict:
            del facets_dict['res_format']
	    if 'tags' in facets_dict:
	        del facets_dict['tags']
        # Renamed facets
        #if 'groups' in facets_dict:
            #facets_dict['groups'] = 'Communities'
        # New facets
        facets_dict['Creator'] = 'Creator'
        facets_dict['extras_DataProvider'] = 'Data Provider'
        facets_dict['extras_Collection'] = 'Collection'
        facets_dict['extras_Discipline'] = 'Discipline'
        facets_dict['extras_Language'] = 'Language'
        facets_dict['extras_Subject'] = 'Subject'
        facets_dict['extras_Country'] = 'Country'
        facets_dict['extras_CreationDate'] = 'CreationDate'
        return facets_dict

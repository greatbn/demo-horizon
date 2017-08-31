from django.utils.translation import ugettext_lazy as _

# The slug of the panel group to be added to HORIZON_CONFIG. Required.
PANEL_GROUP = 'caas_service'
# The display name of the PANEL_GROUP. Required.
PANEL_GROUP_NAME = _('CaaS Service')
# The slug of the dashboard the PANEL_GROUP associated with. Required.
PANEL_GROUP_DASHBOARD = 'project'

ADD_INSTALLED_APPS = ['caas_ui']

AUTO_DISCOVER_STATIC_FILES = True

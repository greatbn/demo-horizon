from django.utils.translation import ugettext_lazy as _
import horizon

class Clusters(horizon.Panel):
    name = _("Clusters")
    slug = "clusters"

from django.conf import settings
from django.shortcuts import render

from snmp_switch.utils import snmp_status, snmp_toggle

# TODO: move settings into app settings/config.

def toggle(request, post_name='portno', template_name='snmp_toggle.html', extra_context={}):
    port = request.POST[post_name]

    context = {}
    context.update(extra_context)

    context.update(snmp_toggle(
        host=settings.SNMP_SWITCH_HOST,
        username=settings.SNMP_SWITCH_USERNAME,
        authkey=settings.SNMP_SWITCH_AUTHKEY,
        privkey=settings.SNMP_SWITCH_PRIVKEY,
        oid=settings.SNMP_SWITCH_OID,
        port=port))

    return render(request, template_name=template_name, context=context)

def status(request, port, template_name='snmp_status.html', extra_context={}):

    context = {}
    context.update(extra_context)

    context.update(snmp_status(
        host=settings.SNMP_SWITCH_HOST,
        username=settings.SNMP_SWITCH_USERNAME,
        authkey=settings.SNMP_SWITCH_AUTHKEY,
        privkey=settings.SNMP_SWITCH_PRIVKEY,
        oid=settings.SNMP_SWITCH_OID,
        port=port))

    return render(request, template_name=template_name, context=context)

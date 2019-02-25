from OFS.Folder import Folder
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

class PollMain(Folder):
    meta_type = "POLL"
    index_html = PageTemplateFile("index_html", globals())

manage_addPollMain = PageTemplateFile("manage_addPollMain_form", globals())


def addPollMain(context, id):
    """ """
    context._setObject(id, PollMain(id))
    return "POLL Installed: %s" % id
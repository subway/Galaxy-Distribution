# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1389957425.987718
_template_filename='templates/admin/review_tool_migration_stages.mako'
_template_uri='admin/review_tool_migration_stages.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x13c77a50', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x13c77a50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x13c77a50')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        migration_stages_dict = _import_ns.get('migration_stages_dict', context.get('migration_stages_dict', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        if message:
            # SOURCE LINE 5
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 7
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Tool migrations that can be performed on this Galaxy instance</div>\n    <div class="toolFormBody">\n        <div class="form-row">\n            <p>\n                The list of tool migration stages below, displayed most recent to oldest, provides information about the repositories in the\n                main Galaxy tool shed that will be cloned at each stage if you run the shell command for that stage.  This enables you to execute\n                the migration process for any stage at any time.\n            </p>\n            <p>\n                Keep in mind that tools included in a repository that you want to be displayed in the Galaxy tool panel when the repository is\n                installed must be defined in the <b>tool_conf.xml</b> (or equivalent) config file prior to execution of the migration process for a\n                stage.  Executing a migration process multiple times will have no affect unless the repositories associated with that stage have been\n                uninstalled prior to the execution of the migration process.\n            </p>\n            <p>\n                When you initiate a migration process, the associated repositories will be cloned from the Galaxy tool shed at\n                <a href="http://toolshed.g2.bx.psu.edu" target="_blank">http://toolshed.g2.bx.psu.edu</a>.  The location in which the tool repositories\n                will be installed is the value of the \'tool_path\' attribute in the <tool> tag of the file named ./migrated_tool_conf.xml\n                (i.e., <b>&lt;toolbox tool_path="../shed_tools"&gt;</b>).  The default location setting is <b>\'../shed_tools\'</b>, which may be problematic\n                for some cluster environments, so make sure to change it before you execute the installation process if appropriate.  The configured location\n                must be outside of the Galaxy installation directory or it must be in a sub-directory protected by a properly configured <b>.hgignore</b>\n                file if the directory is within the Galaxy installation directory hierarchy.  This is because tool shed repositories will be installed using\n                mercurial\'s clone feature, which creates .hg directories and associated mercurial repository files.  Not having <b>.hgignore</b> properly\n                configured could result in undesired behavior when modifying or updating your local Galaxy instance or the tool shed repositories if they are\n                in directories that pose conflicts.  See mercurial\'s .hgignore documentation at\n                <a href="http://mercurial.selenic.com/wiki/.hgignore" target="_blank">http://mercurial.selenic.com/wiki/.hgignore</a> for details.\n            </p>\n        </div>\n        <table class="grid">\n            ')
        # SOURCE LINE 38
        from tool_shed.util.shed_util_common import to_html_string 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['to_html_string'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        # SOURCE LINE 39
        for stage in migration_stages_dict.keys():
            # SOURCE LINE 40
            __M_writer(u'                ')

            migration_command = 'sh ./scripts/migrate_tools/%04d_tools.sh' % stage
            install_dependencies = '%s install_dependencies' % migration_command
            migration_tup = migration_stages_dict[ stage ]
            migration_info, repo_name_dependency_tups = migration_tup
            repository_names = []
            for repo_name_dependency_tup in repo_name_dependency_tups:
                repository_name, tool_dependencies = repo_name_dependency_tup
                if repository_name not in repository_names:
                    repository_names.append( repository_name )
            if repository_names:
                repository_names.sort()
                repository_names = ', '.join( repository_names )
                            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['repository_name','migration_tup','repository_names','migration_command','repo_name_dependency_tup','migration_info','install_dependencies','repo_name_dependency_tups','tool_dependencies'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 53
            __M_writer(u'\n                <tr><td bgcolor="#D8D8D8"><b>Tool migration stage ')
            # SOURCE LINE 54
            __M_writer(unicode(stage))
            __M_writer(u' - repositories: ')
            __M_writer(unicode(repository_names))
            __M_writer(u'</b></td></tr>\n                <tr>\n                    <td bgcolor="#FFFFCC">\n                        <div class="form-row">\n                            <p>')
            # SOURCE LINE 58
            __M_writer(unicode(to_html_string(migration_info)))
            __M_writer(u' <b>Run commands from the Galaxy installation directory!</b></p>\n                            <p>\n')
            # SOURCE LINE 60
            if tool_dependencies:
                # SOURCE LINE 61
                __M_writer(u'                                    This migration stage includes tools that have tool dependencies that can be automatically installed.  To install them, run:<br/>\n                                    <b>')
                # SOURCE LINE 62
                __M_writer(unicode(install_dependencies))
                __M_writer(u'</b><br/><br/>\n                                    To skip tool dependency installation run:<br/>\n                                    <b>')
                # SOURCE LINE 64
                __M_writer(unicode(migration_command))
                __M_writer(u'</b>\n')
                # SOURCE LINE 65
            else:
                # SOURCE LINE 66
                __M_writer(u'                                    <b>')
                __M_writer(unicode(migration_command))
                __M_writer(u'</b>\n')
                pass
            # SOURCE LINE 68
            __M_writer(u'                            </p>\n                        </div>\n                    </td>\n                </tr>\n')
            # SOURCE LINE 72
            for repo_name_dependency_tup in repo_name_dependency_tups:
                # SOURCE LINE 73
                __M_writer(u'                    ')
                repository_name, tool_dependencies = repo_name_dependency_tup 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['repository_name','tool_dependencies'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                    <tr>\n                        <td bgcolor="#DADFEF">\n                            <div class="form-row">\n                                <b>Repository:</b> ')
                # SOURCE LINE 77
                __M_writer(unicode(repository_name))
                __M_writer(u'\n                            </div>\n                        </td>\n                    </tr>\n')
                # SOURCE LINE 81
                if tool_dependencies:
                    # SOURCE LINE 82
                    __M_writer(u'                        <tr>\n                            <td>\n                                <div class="form-row">\n                                    <b>Tool dependencies</b>\n                                </div>\n                            </td>\n                        </tr>\n')
                    # SOURCE LINE 89
                    for tool_dependencies_tup in tool_dependencies:
                        # SOURCE LINE 90
                        __M_writer(u'                            ')

                        tool_dependency_name = tool_dependencies_tup[0]
                        tool_dependency_version = tool_dependencies_tup[1]
                        tool_dependency_type = tool_dependencies_tup[2]
                        installation_requirements = tool_dependencies_tup[3].replace( '\n', '<br/>' )
                                                    
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tool_dependency_name','tool_dependency_type','installation_requirements','tool_dependency_version'] if __M_key in __M_locals_builtin_stored]))
                        # SOURCE LINE 95
                        __M_writer(u'\n                            <tr>\n                                <td>\n                                    <div class="form-row">\n                                        <b>Name:</b> ')
                        # SOURCE LINE 99
                        __M_writer(unicode(tool_dependency_name))
                        __M_writer(u' <b>Version:</b> ')
                        __M_writer(unicode(tool_dependency_version))
                        __M_writer(u' <b>Type:</b> ')
                        __M_writer(unicode(tool_dependency_type))
                        __M_writer(u'\n                                    </div>\n                                    <div class="form-row">\n                                        <b>Requirements and installation information:</b><br/>\n                                        ')
                        # SOURCE LINE 103
                        __M_writer(unicode(installation_requirements))
                        __M_writer(u'\n                                    </div>\n                                </td>\n                            </tr>\n')
                        pass
                    # SOURCE LINE 108
                else:
                    # SOURCE LINE 109
                    __M_writer(u'                        <tr>\n                            <td>\n                                <div class="form-row">\n                                    No tool dependencies have been defined for this repository.\n                                </div>\n                            </td>\n                        </tr>\n')
                    pass
                pass
            pass
        # SOURCE LINE 119
        __M_writer(u'        </table>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



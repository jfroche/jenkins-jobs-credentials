
import sys
import os
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../jenkins_jobs_credentials'))
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage',
              'jenkins_jobs.sphinx.yaml', 'sphinxcontrib.programoutput',
              'sphinx.ext.extlinks']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Jenkins Job Builder Credentials'
copyright = u'2016, Jean-François Roche'

from jenkins_jobs.version import version_info as jenkins_jobs_version
release = jenkins_jobs_version.version_string_with_vcs()

version = jenkins_jobs_version.canonical_version_string()

exclude_patterns = []
pygments_style = 'sphinx'

html_theme = 'default'
htmlhelp_basename = 'JenkinsJobBuilderCredentialsdoc'
latex_elements = {
}
latex_documents = [
    ('index', 'JenkinsJobBuilderCredentials.tex',
     u'Jenkins Job Builder Credentials Documentation',
     u'Jean-François Roche', 'manual')]

linkcheck_timeout = 15


man_pages = [
    ('index', 'jenkins-jobs-credentials', u'Jenkins Job Builder Credentials Documentation',
     [u'Jean-François Roche'], 1)]


texinfo_documents = [
    ('index', 'JenkinsJobBuilderCredentials', u'Jenkins Job Builder Credentials Documentation',
     u'Jean-François Roche', 'JenkinsJobBuilderCredentials', 'Add credentials to Jenkins Job Builder.',
     'Miscellaneous'),
]


extlinks = {'jenkins-wiki': ('https://wiki.jenkins-ci.org/display/JENKINS/%s',
                             None)}

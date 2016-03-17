#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as XML
from jenkins_jobs.errors import JenkinsJobsException
import jenkins_jobs.modules.base


def folder_credential(parser, xml_parent, data):
    """yaml: folder-credential
    Plugin enable folder (:jenkins-wiki:`CloudBees Folders <CloudBees+Folders+Plugin>`) scoped credential.
    Requires the Jenkins :jenkins-wiki:`Credentials Plugin <Credentials+Plugin>`.
    If you want to store ssh keys you will also need: :jenkins-wiki:`Jenkins SSH Credentials Plugin <SSH+Credentials+Plugin>`.

    We can implement two kind of credential:

     1. Username with password
     2. SSH username with private key

    Username with Password credential:

    :arg string type: UsernamePassword (required)
    :arg string username: the username (required)
    :arg string description: the description of the credential
    :arg string password: the password (required)

    SSH Username with private key:

    :arg string type: SSHKey (required)
    :arg string username: the username (required)
    :arg string passphrase: the passphrase to use with the key
    :arg string description: the description of the credential
    :arg string keytype: `source` use the inline private key provided in the `privatekey` parameter (required)
    :arg string privatekey: the private key

    Example:

    .. literalinclude:: /../../tests/properties/fixtures/folder_credential.yaml
    """
    folder_cred = XML.SubElement(xml_parent,
                                 'com.cloudbees.hudson.plugins.folder.'
                                 'properties.FolderCredentialsProvider_'
                                 '-FolderCredentialsProperty')
    domainCredentialsMap = XML.SubElement(folder_cred, 'domainCredentialsMap',
                                          **{'class': "hudson.util.CopyOnWriteMap$Hash"})
    entry = XML.SubElement(domainCredentialsMap, "entry")
    domain = XML.SubElement(entry, "com.cloudbees.plugins.credentials.domains.Domain", plugin="credentials")
    XML.SubElement(domain, "specifications")
    creds = XML.SubElement(entry, "java.util.concurrent.CopyOnWriteArrayList")
    for cred_id, credential in data.items():
        if credential['type'] == 'UsernamePassword':
            pwdCred = XML.SubElement(creds, "com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl",
                                          plugin="credentials")
            XML.SubElement(pwdCred, "id").text = cred_id
            XML.SubElement(pwdCred, "username").text = credential['username']
            XML.SubElement(pwdCred, "description").text = credential.get('description')
            XML.SubElement(pwdCred, "password").text = credential['password']
        elif credential['type'] == 'SSHKey':
            keyCred = XML.SubElement(creds, "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey",
                                     plugin="ssh-credentials")
            XML.SubElement(keyCred, "id").text = cred_id
            XML.SubElement(keyCred, "username").text = credential['username']
            XML.SubElement(keyCred, "description").text = credential.get('description')
            XML.SubElement(keyCred, "passphrase").text = credential.get('passphrase')
            if credential.get('keytype') == 'source':
                privKey = XML.SubElement(keyCred, "privateKeySource", **{'class': "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey$DirectEntryPrivateKeySource"})
            XML.SubElement(privKey, "privateKey").text = credential['privatekey']
        else:
            raise JenkinsJobsException('unknown credential type. Must be UsernamePassword or SSHKey')


class Properties(jenkins_jobs.modules.base.Base):
    sequence = 20

    component_type = 'property'
    component_list_type = 'properties'

    def gen_xml(self, parser, xml_parent, data):
        properties = xml_parent.find('properties')
        if properties is None:
            properties = XML.SubElement(xml_parent, 'properties')

        for prop in data.get('properties', []):
            self.registry.dispatch('property', parser, properties, prop)

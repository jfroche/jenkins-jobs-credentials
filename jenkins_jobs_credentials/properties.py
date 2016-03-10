#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as XML
from jenkins_jobs.errors import JenkinsJobsException
import logging
import jenkins_jobs.modules.base


def folder_credential(parser, xml_parent, data):
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

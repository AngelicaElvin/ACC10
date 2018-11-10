from datainit import *


def hostfileedit(fixed_ip1):
    with open('/etc/hosts', 'rt') as f:
         s = f.read() + '\n' + fixed_ip1 + '\t' + 'sparkworker1 ' + '\n'
         with open('/tmp/etc_hosts.tmp', 'wt') as outf:
             outf.write(s)

    os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')

    with open('/etc/ansible/hosts', 'rt') as f:
         s = f.read() + '\n' + '[sparkworker]' + '\n'
         s1 = f.read() + '\n' + 'ansible-node ansible_ssh_host=' + fixed_ip1[0]  + '\n'
         s2 = f.read() + '\n' + 'sparkmaster ansible_connection=ssh ansible_user=ubuntu' + '\n'
         with open('/tmp/etc_hosts.tmp', 'wt') as outf:
             outf.write(s+s1+s2)

    os.system('sudo mv /tmp/etc_hosts.tmp /etc/ansible/hosts')

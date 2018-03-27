#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText

content = """=====================================================================
                   Red Hat Security Advisory

Synopsis:          Critical: firefox security update
Advisory ID:       RHSA-2018:0549-01
Product:           Red Hat Enterprise Linux
Advisory URL:      https://access.redhat.com/errata/RHSA-2018:0549
Issue date:        2018-03-19
CVE Names:         CVE-2018-5146 
=====================================================================

1. Summary:

An update for firefox is now available for Red Hat Enterprise Linux 6 and
Red Hat Enterprise Linux 7.

Red Hat Product Security has rated this update as having a security impact
of Critical. A Common Vulnerability Scoring System (CVSS) base score, which
gives a detailed severity rating, is available for each vulnerability from
the CVE link(s) in the References section.

2. Relevant releases/architectures:

Red Hat Enterprise Linux Client (v. 7) - x86_64
Red Hat Enterprise Linux Client Optional (v. 7) - x86_64
Red Hat Enterprise Linux Desktop (v. 6) - i386, x86_64
Red Hat Enterprise Linux Desktop Optional (v. 6) - x86_64
Red Hat Enterprise Linux HPC Node Optional (v. 6) - x86_64
Red Hat Enterprise Linux Server (v. 6) - i386, ppc64, s390x, x86_64
Red Hat Enterprise Linux Server (v. 7) - ppc64, ppc64le, s390x, x86_64
Red Hat Enterprise Linux Server Optional (v. 6) - ppc64, s390x, x86_64
Red Hat Enterprise Linux Server Optional (v. 7) - ppc64, s390x, x86_64
Red Hat Enterprise Linux Workstation (v. 6) - i386, x86_64
Red Hat Enterprise Linux Workstation (v. 7) - x86_64
Red Hat Enterprise Linux Workstation Optional (v. 6) - x86_64
Red Hat Enterprise Linux Workstation Optional (v. 7) - x86_64
Red Hat Enterprise Linux for ARM and IBM Power LE (POWER9) Server (v. 7) - aarch64, ppc64le

3. Description:

Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance, and portability.

This update upgrades Firefox to version 52.7.2 ESR.

Security Fix(es):

* Mozilla: Vorbis audio processing out of bounds write (MFSA 2018-08)
(CVE-2018-5146)

For more details about the security issue(s), including the impact, a CVSS
score, acknowledgments, and other related information, refer to the CVE
page(s) listed in the References section.

4. Solution:

For details on how to apply this update, which includes the changes
described in this advisory, refer to:

https://access.redhat.com/articles/11258

After installing the update, Firefox must be restarted for the changes to
take effect.

5. Bugs fixed (https://bugzilla.redhat.com/):

1557221 - CVE-2018-5146 Mozilla: Vorbis audio processing out of bounds write (MFSA 2018-08)

6. Package List:

Red Hat Enterprise Linux Desktop (v. 6):

Source:
firefox-52.7.2-1.el6_9.src.rpm

i386:
firefox-52.7.2-1.el6_9.i686.rpm
firefox-debuginfo-52.7.2-1.el6_9.i686.rpm

x86_64:
firefox-52.7.2-1.el6_9.x86_64.rpm
firefox-debuginfo-52.7.2-1.el6_9.x86_64.rpm

Red Hat Enterprise Linux Desktop Optional (v. 6):

x86_64:
firefox-52.7.2-1.el6_9.i686.rpm
firefox-debuginfo-52.7.2-1.el6_9.i686.rpm

Red Hat Enterprise Linux HPC Node Optional (v. 6):

Source:
firefox-52.7.2-1.el6_9.src.rpm

x86_64:
firefox-52.7.2-1.el6_9.i686.rpm
firefox-52.7.2-1.el6_9.x86_64.rpm
firefox-debuginfo-52.7.2-1.el6_9.i686.rpm
firefox-debuginfo-52.7.2-1.el6_9.x86_64.rpm

Red Hat Enterprise Linux Server (v. 6):

Source:
firefox-52.7.2-1.el6_9.src.rpm

i386:
firefox-52.7.2-1.el6_9.i686.rpm
firefox-debuginfo-52.7.2-1.el6_9.i686.rpm

ppc64:
firefox-52.7.2-1.el6_9.ppc64.rpm
firefox-debuginfo-52.7.2-1.el6_9.ppc64.rpm

s390x:
firefox-52.7.2-1.el6_9.s390x.rpm
firefox-debuginfo-52.7.2-1.el6_9.s390x.rpm

x86_64:
firefox-52.7.2-1.el6_9.x86_64.rpm
firefox-debuginfo-52.7.2-1.el6_9.x86_64.rpm

Red Hat Enterprise Linux Server Optional (v. 6):

ppc64:
firefox-52.7.2-1.el6_9.ppc.rpm
firefox-debuginfo-52.7.2-1.el6_9.ppc.rpm

s390x:
firefox-52.7.2-1.el6_9.s390.rpm
firefox-debuginfo-52.7.2-1.el6_9.s390.rpm

x86_64:
firefox-52.7.2-1.el6_9.i686.rpm
firefox-debuginfo-52.7.2-1.el6_9.i686.rpm

Red Hat Enterprise Linux Workstation (v. 6):

Source:
firefox-52.7.2-1.el6_9.src.rpm

i386:
firefox-52.7.2-1.el6_9.i686.rpm
firefox-debuginfo-52.7.2-1.el6_9.i686.rpm

x86_64:
firefox-52.7.2-1.el6_9.x86_64.rpm
firefox-debuginfo-52.7.2-1.el6_9.x86_64.rpm

Red Hat Enterprise Linux Workstation Optional (v. 6):

x86_64:
firefox-52.7.2-1.el6_9.i686.rpm
firefox-debuginfo-52.7.2-1.el6_9.i686.rpm

Red Hat Enterprise Linux Client (v. 7):

Source:
firefox-52.7.2-1.el7_4.src.rpm

x86_64:
firefox-52.7.2-1.el7_4.x86_64.rpm
firefox-debuginfo-52.7.2-1.el7_4.x86_64.rpm

Red Hat Enterprise Linux Client Optional (v. 7):

x86_64:
firefox-52.7.2-1.el7_4.i686.rpm
firefox-debuginfo-52.7.2-1.el7_4.i686.rpm

Red Hat Enterprise Linux Server (v. 7):

Source:
firefox-52.7.2-1.el7_4.src.rpm

ppc64:
firefox-52.7.2-1.el7_4.ppc64.rpm
firefox-debuginfo-52.7.2-1.el7_4.ppc64.rpm

ppc64le:
firefox-52.7.2-1.el7_4.ppc64le.rpm
firefox-debuginfo-52.7.2-1.el7_4.ppc64le.rpm

s390x:
firefox-52.7.2-1.el7_4.s390x.rpm
firefox-debuginfo-52.7.2-1.el7_4.s390x.rpm

x86_64:
firefox-52.7.2-1.el7_4.x86_64.rpm
firefox-debuginfo-52.7.2-1.el7_4.x86_64.rpm

Red Hat Enterprise Linux for ARM and IBM Power LE (POWER9) Server (v. 7):

Source:
firefox-52.7.2-1.el7_4.src.rpm

aarch64:
firefox-52.7.2-1.el7_4.aarch64.rpm
firefox-debuginfo-52.7.2-1.el7_4.aarch64.rpm

ppc64le:
firefox-52.7.2-1.el7_4.ppc64le.rpm
firefox-debuginfo-52.7.2-1.el7_4.ppc64le.rpm

Red Hat Enterprise Linux Server Optional (v. 7):

ppc64:
firefox-52.7.2-1.el7_4.ppc.rpm
firefox-debuginfo-52.7.2-1.el7_4.ppc.rpm

s390x:
firefox-52.7.2-1.el7_4.s390.rpm
firefox-debuginfo-52.7.2-1.el7_4.s390.rpm

x86_64:
firefox-52.7.2-1.el7_4.i686.rpm
firefox-debuginfo-52.7.2-1.el7_4.i686.rpm

Red Hat Enterprise Linux Workstation (v. 7):

Source:
firefox-52.7.2-1.el7_4.src.rpm

x86_64:
firefox-52.7.2-1.el7_4.x86_64.rpm
firefox-debuginfo-52.7.2-1.el7_4.x86_64.rpm

Red Hat Enterprise Linux Workstation Optional (v. 7):

x86_64:
firefox-52.7.2-1.el7_4.i686.rpm
firefox-debuginfo-52.7.2-1.el7_4.i686.rpm

These packages are GPG signed by Red Hat for security.  Our key and
details on how to verify the signature are available from
https://access.redhat.com/security/team/key/

7. References:

https://access.redhat.com/security/cve/CVE-2018-5146
https://access.redhat.com/security/updates/classification/#critical
https://www.mozilla.org/en-US/security/advisories/mfsa2018-08/

8. Contact:

The Red Hat security contact is <secalert redhat com>. More contact
details at https://access.redhat.com/security/team/contact/

Copyright 2018 Red Hat, Inc.
"""

msg = MIMEText(content)

msg['Subject'] = '[RHSA-2018:0549-01] Critical: firefox security update'
msg['From'] = 'rhsa-announce@redhat.com'
msg['To'] = 'rhsa-announce@redhat.com'

s = smtplib.SMTP('localhost', 10025)
s.send_message(msg)
s.quit()

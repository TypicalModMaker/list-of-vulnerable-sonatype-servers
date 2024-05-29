# Servers vulnerable to [CVE-2024-4956](https://support.sonatype.com/hc/en-us/articles/29416509323923-CVE-2024-4956-Nexus-Repository-3-Path-Traversal-2024-05-16)

Nexus Repository Manager 3 Unauthenticated Path Traversal

Servers running on the nexus docker image are excluded 

all-servers-from-shodan.txt - list of all sonatype nexus servers on shodan\
all-servers-vulnerable.txt - list of all vulnerable sonatype nexus servers that are vulnerable\
all-servers-running-as-root-vulnerable.txt - list of all vulnerable sonatype nexus servers that are being ran as root

check-vulnerable-servers.py - checks if /etc/passwd exists from all-servers-from-shodan.txt\
check-root-servers.py - checks if /etc/shadow exists from all-servers-from-shodan.txt\
check-private_keys.py - checks for common private key paths on root and tries to ssh as root with found keys

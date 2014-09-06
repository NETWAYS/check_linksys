check_linksys
=============

Checks a Linksys Router or Switch using SNMP.


### Requirements

* Perl libraries: `Net::SNMP`


### Usage

    check_linksys.pl -H|--host=<host> -C|--community=<SNMP community string>
                [-e|--ethernetinterfaces]
                [-u|--uptime]
                [-d|--description]
                [-t|--timeout=<timeout in seconds>]
                [-v|--verbose=<verbosity level>]
                [-h|--help] [-V|--version]

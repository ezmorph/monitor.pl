Name:           monitor
Version:        0.15.0
Release:        1%{?dist}
Summary:        Perl-based Zabbix agent daemon

Group:          Applications/Internet
License:        GPL
URL:            http://www.wikimart.ru/
Source0:        monitor.tar.gz
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Buildarch:      noarch

AutoReqProv:    no
Requires:       bash, perl, logrotate, perl(Data::Dumper), perl(DBI), perl(DBD::mysql), perl(JSON), perl(JSON::XS)
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/chkconfig

%description
Perl-based Zabbix agent daemon

%prep

%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
tar -xzvf %{SOURCE0} -C $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add monitor

%preun
if [ "$1" = 0 ]
then
  /etc/init.d/monitor forcestop
  /sbin/chkconfig --del monitor
fi

%files
/etc/init.d/monitor
/etc/monitor.pl
/etc/logrotate.d/monitor
%config(noreplace) /usr/bin/monitor.pl
/usr/lib/monitor/diskstats.pl
/usr/lib/monitor/diskstats_lld.pl
/usr/lib/monitor/diskusage.pl
/usr/lib/monitor/memcache.pl
/usr/lib/monitor/monitor.pl
/usr/lib/monitor/mysql.pl
/usr/lib/monitor/nginx.pl
/usr/lib/monitor/nginxlog.pl
/usr/lib/monitor/process.pl
/usr/lib/monitor/zabbix.pl
/usr/lib/monitor/rabbit.pl
/usr/lib/monitor/sphinx.pl
/usr/lib/monitor/snmp.pl
/usr/lib/monitor/phpfpm.pl
/usr/lib/monitor/redis.pl
/usr/lib/monitor/ccissraid.pl
/usr/lib/monitor/postfixlog.pl
/usr/lib/monitor/_template.pl
/usr/lib/monitor/yml.pl
/usr/lib/monitor/megaraid.pl
/usr/lib/monitor/haproxy.pl

/usr/share/monitor/cisco_gen_zbx_tmpl.pl

%changelog
* Mon Aug 25 2014 - dolphin@wikimart.ru
- v0.15.0 DuskUsage module added

* Tue Jul 29 2014 - dolphin@wikimart.ru
- v0.14.0 Haproxy module added

* Wed Jul 14 2014 - dkhlynin@wikimart.ru
- v0.13.1 Added php_avg_resp_time to NginxLog module

* Wed Jul 09 2014 - dolphin@wikimart.ru
- v0.13.0 LLD version of DiskStat added

* Wed Jun 04 2014 - dolphin@wikimart.ru
- v0.12.5 Mysql & Megaraid fixes

* Thu Jan 30 2014 - dolphin@wikimart.ru
- v0.12.4 Mysql Innodb_row_lock_current_waits fix

* Thu Jan 23 2014 - dolphin@wikimart.ru
- v0.12.3 NginxLog fixed

* Wed Dec 04 2013 - dolphin@wikimart.ru
- v0.12.2 Redis protocol fix

* Fri Oct 18 2013 - dolphin@wikimart.ru
- v0.12.1 Nginxlog module portability fix

* Sat Oct 05 2013 - dolphin@wikimart.ru
- v0.12.0 Megaraid module added

* Wed Oct 03 2012 - dkhlynin@wikimart.ru 
- v0.11.2 ccissraid: added CentOS-6 support

* Mon Sep 06 2012 - dolphin@wikimart.ru
- v0.11.1 Tool for generating complex zabbix templates for cisco networking hardware

* Mon Aug 13 2012 - dkhlynin@wikimart.ru
- v0.11.0 Added postfix module & logrotate configuration file

* Tue Feb 12 2012 - dolphin@wikimart.ru
- v0.10.2 Rabbit node memory usage added

* Thu Jan 17 2012 - dolphin@wikimart.ru
- v0.10.1 Redis hitrate added

* Thu Nov 24 2011 - dkhlynin@wikimart.ru
- v0.10.0 CCISS RAID module added

* Wed Oct 12 2011 - dolphin@wikimart.ru
- v0.9.0 Redis module added

* Mon Oct 10 2011 - dolphin@wikimart.ru
- v0.8.0 Diskstats module rewritten

* Thu Oct 6 2011 - dolphin@wikimart.ru
- v0.7.0 PHP FPM module improvement and code cleanup, versioning changed

* Tue Oct 4 2011 - dolphin@wikimart.ru
- v0.0.6 Added PHP FPM module

* Fri Sep 30 2011 - dolphin@wikimart.ru
- v0.0.5 Added snmp module

* Tue Jul 26 2011 - dolphin@wikimart.ru
- v0.0.4 Added sphinx module

* Tue Jul 26 2011 - dolphin@wikimart.ru
- v0.0.3 Added rabbitmq monitoring via rabbit_management plugin

* Tue Jul 5 2011 - dolphin@wikimart.ru
- v0.0.2 Added hit_rate, free_mem to memcache module

* Tue Jul 5 2011 - dolphin@wikimart.ru
- v0.0.1 Initial packaging

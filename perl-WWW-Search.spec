%define upstream_name    WWW-Search
%define upstream_version 2.508

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Virtual base class for WWW searches
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Bit::Vector)
BuildRequires:	perl(CGI)
BuildRequires:	perl(Date::Manip)
BuildRequires:	perl(HTML::Tree)
BuildRequires:	perl(IO::Capture) >= 0.05
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::File)
BuildRequires:	perl(Test::Inline) >= 0.16

BuildArch:	noarch

%description
This class is the parent for all access methods supported by the WWW::Search
library. This library implements a Perl API to web-based search engines.

See README for a list of search engines currently supported, and for a lot of
interesting high-level information about this distribution.

Search results can be limited, and there is a pause between each request to
avoid overloading either the client or the server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
for file in `find lib -type f` Changes README; do
    chmod 644 $file
done
perl -pi -e 's|/usr/local/bin/perl|/usr/bin/perl|' lib/WWW/Search/*.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
export PATH=$PATH:%{buildroot}%{_bindir}
%{__make} test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/WWW
%{_mandir}/*/*


%changelog
* Mon Jul 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.508.0-1mdv2011.0
+ Revision: 551205
- update to 2.508

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.507-2mdv2010.0
+ Revision: 440750
- rebuild

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.507-1mdv2009.1
+ Revision: 309455
- update to new version 2.507

* Tue Jul 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.504-1mdv2009.0
+ Revision: 240017
- update to new version 2.504

* Thu Jul 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.503-1mdv2009.0
+ Revision: 236723
- update to new version 2.503

* Tue Jul 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.502-1mdv2009.0
+ Revision: 235797
- fix tests execution
- update to new version 2.502

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.501-1mdv2009.0
+ Revision: 194963
- update to new version 2.501

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.497-1mdv2008.1
+ Revision: 156182
- update to new version 2.497

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.496-1mdv2008.1
+ Revision: 109506
- update to new version 2.496

* Thu Aug 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.495-1mdv2008.0
+ Revision: 64001
- new version

* Thu Jul 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.494-1mdv2008.0
+ Revision: 48657
- new version

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 2.491-1mdv2008.0
+ Revision: 20721
- 2.491


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.489-1mdv2007.0
- New version 2.489
- better summary and description

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.488-1mdk
- New release 2.488
- better sources URL
- better buildrequires syntax

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.487-2mdk
- fix buildrequires

* Fri Mar 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.487-1mdk
- New release 2.487

* Thu Feb 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.486-1mdk
- New release 2.486

* Mon Jan 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.485-1mdk
- New release 2.485
- drop patch0 (merged upstream)

* Tue Jan 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.484-2mdk
- fix files encoding and perms

* Tue Jan 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.484-1mdk
- New release 2.484
- rediff patch0

* Thu Aug 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.479-1mdk
- New release 2.479

* Sun Jul 31 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.476-2mdk
- Fix BuildRequires

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.476-1mdk
- initial Mandriva package


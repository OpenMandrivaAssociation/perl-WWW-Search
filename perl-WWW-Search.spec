%define module  WWW-Search
%define name    perl-%{module}
%define version 2.494
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Summary:    Virtual base class for WWW searches
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/WWW/%{module}-%{version}.tar.bz2
Patch:       WWW-Search-2.494-fix-tests.patch
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(HTML::Tree)
BuildRequires:  perl(IO::Capture) >= 0.05
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::Inline) >= 0.16
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(CGI)
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This class is the parent for all access methods supported by the WWW::Search
library. This library implements a Perl API to web-based search engines.

See README for a list of search engines currently supported, and for a lot of
interesting high-level information about this distribution.

Search results can be limited, and there is a pause between each request to
avoid overloading either the client or the server.

%prep
%setup -q -n %{module}-%{version} 
%patch0 -p 1
for file in `find lib -type f` Changes README; do
    chmod 644 $file
done
perl -pi -e 's|/usr/local/bin/perl|/usr/bin/perl|' lib/WWW/Search/*.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/WWW
%{_mandir}/*/*


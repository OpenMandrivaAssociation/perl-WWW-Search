%define upstream_name    WWW-Search
%define upstream_version 2.508

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Virtual base class for WWW searches
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Bit::Vector)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(HTML::Tree)
BuildRequires:  perl(IO::Capture) >= 0.05
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::Inline) >= 0.16

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
export PATH=$PATH:%{buildroot}%{_bindir}
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

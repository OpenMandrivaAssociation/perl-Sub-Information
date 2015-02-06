%define upstream_name    Sub-Information
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Get subroutine information
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Sub/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(B)
BuildRequires:	perl(Data::Dump::Streamer)
BuildRequires:	perl(Devel::Peek)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Typically, if we need to get information about code references, we have to
remember which of myriad modules to load. Need to know if it's blessed?
'Scalar::Util' will do that. Package it was declared in: 'Sub::Identify'.
Source code: 'Data::Dump::Streamer'. And so on ...

This module integrates those together so that you don't have to remember
them.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 658426
- rebuild for updated rpm-setup

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 444013
- import perl-Sub-Information


* Thu Sep 17 2009 cpan2dist 0.10-1mdv
- initial mdv release, generated with cpan2dist

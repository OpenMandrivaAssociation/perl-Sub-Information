%define upstream_name    Sub-Information
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Get subroutine information
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Sub/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B)
BuildRequires: perl(Data::Dump::Streamer)
BuildRequires: perl(Devel::Peek)
BuildRequires: perl(PadWalker)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Identify)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



%define upstream_name    Dist-Zilla-Plugin-Test-CPAN-Changes
%define upstream_version 0.013

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Release tests for your changelog
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/karenetheridge/Dist-Zilla-Plugin-Test-CPAN-Changes
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-Test-CPAN-Changes-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires:	perl(Dist::Zilla::Role::FileMunger)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This is an extension of the Dist::Zilla::Plugin::InlineFiles manpage,
providing the following file:

    xt/release/cpan-changes.t - a standard Test::CPAN::Changes test

See the Test::CPAN::Changes manpage for what this test does.

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
%doc README CHANGES LICENSE META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Sort
%define		pnam	Fields
Summary:	Sort::Fields perl module
Summary(pl.UTF-8):	Moduł perla Sort::Fields
Name:		perl-Sort-Fields
Version:	0.90
Release:	11
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	72a10526c1c0c747da41b808a362fe42
URL:		http://search.cpan.org/dist/Sort-Fields/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::Fields provides a general purpose technique for efficiently
sorting lists of lines that contain data separated into fields.

%description -l pl.UTF-8
Sort::Fields udostępnia technikę wydajnego sortowania linii
zawierających podzielone na pola dane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sort/Fields.pm
%{_mandir}/man3/*

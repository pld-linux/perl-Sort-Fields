%include	/usr/lib/rpm/macros.perl
%define	pdir	Sort
%define	pnam	Fields
Summary:	Sort::Fields perl module
Summary(pl):	Modu³ perla Sort::Fields
Name:		perl-Sort-Fields
Version:	0.90
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	72a10526c1c0c747da41b808a362fe42
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::Fields provides a general purpose technique for efficiently
sorting lists of lines that contain data separated into fields.

%description -l pl
Sort::Fields udostpênia technikê wydajnego sortowania linii
zawieraj±cych podzielone na pola dane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sort/Fields.pm
%{_mandir}/man3/*

%include	/usr/lib/rpm/macros.perl
Summary:	Sort-Fields perl module
Summary(pl):	Modu³ perla Sort-Fields
Name:		perl-Sort-Fields
Version:	0.90
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sort/Sort-Fields-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort-Fields provides a general purpose technique for efficiently
sorting lists of lines that contain data separated into fields.

%description -l pl
Sort-Fields udostpênia technikê wydajnego sortowania linii
zawieraj±cych podzielone na pola dane.

%prep
%setup -q -n Sort-Fields-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Sort/Fields.pm
%{_mandir}/man3/*

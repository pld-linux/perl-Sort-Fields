%include	/usr/lib/rpm/macros.perl
Summary:	Sort-Fields perl module
Summary(pl):	Modu³ perla Sort-Fields
Name:		perl-Sort-Fields
Version:	0.90
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sort/Sort-Fields-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Sort-Fields provides a general purpose technique for efficiently sorting lists
of lines that contain data separated into fields. 

%description -l pl
Sort-Fields udostpênia technikê wydajnego sortowania linii zawieraj±cych 
podzielone na pola dane.

%prep
%setup -q -n Sort-Fields-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Sort/Fields
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Sort/Fields.pm
%{perl_sitearch}/auto/Sort/Fields

%{_mandir}/man3/*

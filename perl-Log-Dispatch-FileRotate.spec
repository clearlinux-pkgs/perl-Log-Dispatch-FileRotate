#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Dispatch-FileRotate
Version  : 1.38
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/Log-Dispatch-FileRotate-1.38.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/Log-Dispatch-FileRotate-1.38.tar.gz
Summary  : 'Log to Files that Archive/Rotate Themselves'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Log-Dispatch-FileRotate-license = %{version}-%{release}
Requires: perl-Log-Dispatch-FileRotate-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Date::Manip)
BuildRequires : perl(Log::Dispatch)
BuildRequires : perl(Log::Dispatch::File)
BuildRequires : perl(Log::Dispatch::Output)
BuildRequires : perl(Log::Dispatch::Screen)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Warn)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(namespace::autoclean)

%description
This archive contains the distribution Log-Dispatch-FileRotate,
version 1.38:
Log to Files that Archive/Rotate Themselves

%package dev
Summary: dev components for the perl-Log-Dispatch-FileRotate package.
Group: Development
Provides: perl-Log-Dispatch-FileRotate-devel = %{version}-%{release}
Requires: perl-Log-Dispatch-FileRotate = %{version}-%{release}

%description dev
dev components for the perl-Log-Dispatch-FileRotate package.


%package license
Summary: license components for the perl-Log-Dispatch-FileRotate package.
Group: Default

%description license
license components for the perl-Log-Dispatch-FileRotate package.


%package perl
Summary: perl components for the perl-Log-Dispatch-FileRotate package.
Group: Default
Requires: perl-Log-Dispatch-FileRotate = %{version}-%{release}

%description perl
perl components for the perl-Log-Dispatch-FileRotate package.


%prep
%setup -q -n Log-Dispatch-FileRotate-1.38
cd %{_builddir}/Log-Dispatch-FileRotate-1.38

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Dispatch-FileRotate
cp %{_builddir}/Log-Dispatch-FileRotate-1.38/LICENSE %{buildroot}/usr/share/package-licenses/perl-Log-Dispatch-FileRotate/bab88f54ea8c7c2588e407bd69fad8bf7cb47c1b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Dispatch::FileRotate.3
/usr/share/man/man3/Log::Dispatch::FileRotate::Flock.3
/usr/share/man/man3/Log::Dispatch::FileRotate::Mutex.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Log-Dispatch-FileRotate/bab88f54ea8c7c2588e407bd69fad8bf7cb47c1b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

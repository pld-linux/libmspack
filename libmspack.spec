Summary:	A library for Microsoft compression formats
Summary(pl):	Biblioteka do formatów kompresji u¿ywanych przez Microsoft
Name:		libmspack
Version:	0.0.20060920alpha
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.kyz.uklinux.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	72003dfa5da2e843e3d5ae0c18f7c969
URL:		http://www.kyz.uklinux.net/libmspack/
BuildRequires:	gcc >= 5:3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of libmspack is to provide compressors and decompressors,
archivers and dearchivers for Microsoft compression formats: CAB, CHM,
HLP, KWAJ, LIT and SZDD. It is also designed to be easily embeddable,
stable, robust and resource-efficient.

%description -l pl
Celem libmspack jest dostarczenie kompresorów i dekompresorów,
archiwizerów i dearchiwizerów dla formatów kompresji u¿ywanych przez
Microsoft: CAB, CHM, HLP, KWAJ, LIT i SZDD. Ponadto biblioteka zosta³a
zaprojektowana tak, by byæ ³atwo osadzalna, stabilna, mocna i wydajna
pod wzglêdem zasobów.

%package devel
Summary:	Header files for libmspack library
Summary(pl):	Pliki nag³ówkowe biblioteki libmspack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmspack library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libmspack.

%package static
Summary:	Static libmspack library
Summary(pl):	Statyczna biblioteka libmspack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmspack library.

%description static -l pl
Statyczna biblioteka libmspack.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libmspack.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.{html,css,png}
%attr(755,root,root) %{_libdir}/libmspack.so
%{_libdir}/libmspack.la
%{_includedir}/mspack.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmspack.a

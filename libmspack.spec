#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	A library for Microsoft compression formats
Summary(pl.UTF-8):	Biblioteka do formatów kompresji używanych przez Microsoft
Name:		libmspack
Version:	0.8alpha
Release:	2
License:	LGPL v2.1
Group:		Libraries
Source0:	https://www.cabextract.org.uk/libmspack/%{name}-%{version}.tar.gz
# Source0-md5:	be4ed61868c6c1ecc173b678ce3459be
Patch0:		%{name}-deps.patch
Patch1:		%{name}-headers.patch
URL:		https://www.cabextract.org.uk/libmspack/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gcc >= 5:3.0
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
The purpose of libmspack is to provide compressors and decompressors,
archivers and dearchivers for Microsoft compression formats: CAB, CHM,
HLP, KWAJ, LIT, SZDD and WIM. It is also designed to be easily
embeddable, stable, robust and resource-efficient.

%description -l pl.UTF-8
Celem libmspack jest dostarczenie kompresorów i dekompresorów,
archiwizerów i dearchiwizerów dla formatów kompresji używanych przez
Microsoft: CAB, CHM, HLP, KWAJ, LIT, SZDD i WIM. Ponadto biblioteka
została zaprojektowana tak, by być łatwo osadzalna, stabilna, mocna i
wydajna pod względem zasobów.

%package devel
Summary:	Header files for libmspack library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmspack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmspack library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmspack.

%package static
Summary:	Static libmspack library
Summary(pl.UTF-8):	Statyczna biblioteka libmspack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmspack library.

%description static -l pl.UTF-8
Statyczna biblioteka libmspack.

%package progs
Summary:	MS expand-compatible, .cab and .chm decompressors
Summary(pl.UTF-8):	Dekompresory do plików .cab, .chm i zgodnych z MS expand
Group:		Applications/Archiving
Requires:	%{name} = %{version}-%{release}

%description progs
Microsoft expand.exe-compatible, .cab and .chm file decompressors.

%description progs -l pl.UTF-8
Programy dekompresujące pliki .cab, .chm i zgodne z expand.exe
Microsoftu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	includedir=%{_includedir}/mspack \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libmspack.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmspack.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_libdir}/libmspack.so
%{_libdir}/libmspack.la
%dir %{_includedir}/mspack
%{_includedir}/mspack/system.h
%{_includedir}/mspack/mspack.h
%{_pkgconfigdir}/libmspack.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmspack.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cabrip
%attr(755,root,root) %{_bindir}/chmextract
%attr(755,root,root) %{_bindir}/msexpand
%attr(755,root,root) %{_bindir}/oabextract

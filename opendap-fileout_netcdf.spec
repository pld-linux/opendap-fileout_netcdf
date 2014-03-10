#
# Conditional build:
%bcond_with	tests	# make check (requires BES server)
#
Summary:	OPeNDAP server module to return a NetCDF file for a DAP Data response
Summary(pl.UTF-8):	Moduł serwera OPeNDAP zwracający pliki NetCDF jako odpowiedź DAP
Name:		opendap-fileout_netcdf
Version:	1.2.1
Release:	1
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://www.opendap.org/pub/source/fileout_netcdf-%{version}.tar.gz
# Source0-md5:	d165b3ebac9b61ad16b1046aa1a3a585
URL:		http://opendap.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.10
%{?with_tests:BuildRequires:	bes >= 3.9.0}
BuildRequires:	bes-devel >= 3.9.0
BuildRequires:	libdap-devel >= 3.11.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	netcdf-devel >= 4.0.0
BuildRequires:	pkgconfig
Requires:	bes >= 3.9.0
Requires:	libdap >= 3.11.0
Requires:	netcdf >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the fileout netCDF response handler for Hyrax - the OPeNDAP
data server. With this handler a server can easily be configured to
return data packaged in a netCDF 3 file.

%description -l pl.UTF-8
Ten pakiet zawiera moduł serwera danych OPeNDAP (Hyrax) obsługujący
odpowiedzi fileout netCDF. Przy jego użyciu można łatwo skonfigurować
serwer, aby zwracał dane spakowane w pliku netCDF 3.

%prep
%setup -q -n fileout_netcdf-%{version}

%build
# rebuild autotools for -as-needed to work
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-openjpeg-prefix=/usr
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/bes/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/fonc.conf
%attr(755,root,root) %{_libdir}/bes/libfonc_module.so

%define	major 2
%define libname	%mklibname bhpos_serverlibs %{major}

Summary:	BananaPOS bhpos server libraries
Name:		bhpos_serverlibs
Version:	2.0.0
Release:	%mkrel 0.beta3.3
License:	GPL
Group:		System/Libraries
URL:		http://www.bananahead.com
Source0:	ftp://bananahead.com/pub/bhpos2/stable/%{name}-%{version}.tar.bz2
Patch0:		bhpos_serverlibs-2.0.0-mysql.diff
BuildRequires:	bhpos_commonlibs-devel >= 2.0.0
BuildRequires:	bhpos_base >= 2.0.0
BuildRequires:	bhpos_base-devel >= 2.0.0
BuildRequires:	gtkmm2.4
BuildRequires:	gtkmm2.4-devel
BuildRequires:	intltool
BuildRequires:	libtool >= 1.5
BuildRequires:	libxml2 >= 2.5.8
BuildRequires:	libusb-devel >= 0.1.8
BuildRequires:	libxml++-devel >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	mysql-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
BananaPOS server libraries, are required by the server (mysql version).

%package -n	%{libname}
Summary:	BananaPOS bhpos server libraries
Group:          System/Libraries
Requires:	bhpos_base >= 2.0.0

%description -n	%{libname}
BananaPOS server libraries, are required by the server (mysql version).

%package -n	%{libname}-devel
Summary:	Development files for the %{libname} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	bhpos_commonlibs-devel >= 2.0.0
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
Development files for the %{libname} library

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%build
sh ./autogen.sh

%configure2_5x \
    --with-mysql=%{_prefix}

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog NEWS README
%{_libdir}/bhpos2.0/lib*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)  
%{_libdir}/bhpos2.0/*.a
%{_libdir}/bhpos2.0/*.la
%{_libdir}/bhpos2.0/*.so
%{_libdir}/pkgconfig/bhserverlib-2.0.pc
%{_includedir}/bhpos2.0/*.h



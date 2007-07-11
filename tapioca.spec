%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

%define	name tapioca
%define	version 0.3.9
%define	release %mkrel 1

Summary:	A framework for Voice over IP (VoIP) and Instant Messaging (IM)		
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		http://tapioca-voip.sourceforge.net/wiki/index.php/Tapioca
Group:		Networking/Instant messaging
Source0:	http://ovh.dl.sourceforge.net/sourceforge/tapioca-voip/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  pkgconfig
BuildRequires:  libdbus-devel >= 0.36
BuildRequires:  libdbus-glib >= 0.36
Requires:       %{libname}

%description

Tapioca is a framework for Voice over IP (VoIP) and 
Instant Messaging (IM). Its main goal is to provide 
an easy way for developing and using VoIP and IM 
services in any kind of application. It was designed 
to be cross-platform, lightweight, thread-safe, having 
mobile devices and applications in mind.

	Tapioca's main goals are:
	
    * Create a solution that integrates all components 
used by VoIP and IM applications in a single, reliable 
and easy to use framework, which is able to work on different 
platforms.

    * Spare resources, providing central services for multiple 
applications. Eg.: The control of all incoming and outgoing SIP 
requests are managed by the SIP service, avoiding the creation of
 one SIP stack and allocation of a network port for each SIP-based 
application.

    * Reduce the overhead of control layers and library dependencies. 

%package -n %{libname}
Summary:	Tapioca  library
Group:		Graphical desktop/KDE
Provides:	%{libname_orig} = %{version}-%{release}
Requires:	%name = %version-%release

%description -n %{libname}
Library for %name


%package -n %{libname}-devel
Summary:	Headers of %name for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}

%description -n %{libname}-devel
Headers of %{name} for development.


%prep
%setup -q

%build
export QTDIR=%qtdir
export KDEDIR=%_prefix

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig


%files
%defattr(-,root,root)
%{_bindir}/tapiocad-0.3
%{_datadir}/dbus-1/services/org.tapioca.Server.service

%files -n %{libname}
%{_libdir}/libtapioca-client-0.3.so.0
%{_libdir}/libtapioca-client-0.3.so.0.0.0
%{_libdir}/libtapioca-core-0.3.so.0
%{_libdir}/libtapioca-core-0.3.so.0.0.0
%{_libdir}/libtapioca-base-0.3.so.0
%{_libdir}/libtapioca-base-0.3.so.0.0.0

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/libtapioca-core-0.3.la
%{_libdir}/libtapioca-core-0.3.so
%{_libdir}/libtapioca-client-0.3.la
%{_libdir}/libtapioca-client-0.3.so
%{_libdir}/libtapioca-base-0.3.la
%{_libdir}/libtapioca-base-0.3.so
%{_libdir}/pkgconfig/tapioca-client-0.3.pc
%{_libdir}/pkgconfig/tapioca-core-0.3.pc
%{_libdir}/pkgconfig/tapioca-base-0.3.pc
%{_includedir}/tapioca-0.3/tapioca/client/*.h
%{_includedir}/tapioca-0.3/tapioca/core/*.h
%{_includedir}/tapioca-0.3/tapioca/base/*.h




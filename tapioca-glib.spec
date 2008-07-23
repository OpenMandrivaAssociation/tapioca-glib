%define libname_orig lib%{name}
%define libname %mklibname tapioca 0
%define develname %mklibname -d tapioca

%define	name tapioca-glib
%define	version 0.14.0.1
%define	release %mkrel 3

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
BuildRequires:  libdbus-glib-devel >= 0.36
Requires:       %{libname} = %{version}
Obsoletes:	tapioca < 0.14.0.1
Provides:	tapioca = %{version}-%{release}

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


%package -n %{develname}
Summary:	Headers of %name for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n %{develname}
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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README RELEASE
%doc %{_datadir}/gtk-doc/html/tapioca-glib-client
%doc %{_datadir}/gtk-doc/html/tapioca-glib-core

%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.*

%files -n %{develname}
%doc COPYING README
%defattr(-,root,root)
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*/tapioca/*.h
%{_includedir}/*/tapioca/*/*.h

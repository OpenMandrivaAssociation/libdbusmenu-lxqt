%define major 0
%define libname %mklibname dbusmenu-lxqt
%define devname %mklibname dbusmenu-lxqt -d

Name: libdbusmenu-lxqt
Version: 0.4.0
Release: 2
Source0: https://github.com/lxqt/libdbusmenu-lxqt/releases/download/%{version}/libdbusmenu-lxqt-%{version}.tar.xz
Summary: The LXQt implementation of the DBusMenu protocol
URL: https://github.com/lxqt/libdbusmenu-lxqt
License: LGPL-2.1
Group: System/Libraries
BuildSystem: cmake
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: pkgconfig(QJson)

%description
The LXQt implementation of the DBusMenu protocol

%package -n %{libname}
Summary: The LXQt implementation of the DBusMenu protocol
Group: System/Libraries

%description -n %{libname}
The LXQt implementation of the DBusMenu protocol

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*

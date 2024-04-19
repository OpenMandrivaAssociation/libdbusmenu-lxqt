%define major 0
%define libname %mklibname dbusmenu-lxqt
%define devname %mklibname dbusmenu-lxqt -d

Name: libdbusmenu-lxqt
Version: 0.1.0
Release: 1
Source0: https://github.com/lxqt/libdbusmenu-lxqt/archive/%{version}/%{name}-%{version}.tar.gz
Summary: The LXQt implementation of the DBusMenu protocol
URL: https://github.com/lxqt/libdbusmenu-lxqt
License: LGPL-2.1
Group: System/Libraries
BuildRequires: cmake
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

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*

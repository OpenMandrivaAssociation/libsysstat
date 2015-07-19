%define major 0
%define beta %{nil}
%define scmrev %{nil}
%define libname %mklibname sysstat-qt5 %{major}
%define devname %mklibname sysstat-qt5 -d
%define qt4libname %mklibname sysstat %{major}
%define qt4devname %mklibname sysstat -d

Name: libsysstat
Version: 0.3.0
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 3
Source0: http://lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
%else
Release: 0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: System status library for LXQt
URL: http://lxqt.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5LinguistTools)

%description
System status library for LXQt

%package -n %{libname}
Summary: System status library for LXQt
Group: System/Libraries
%rename %{qt4libname}

%description -n %{libname}
System status library for LXQt

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
%rename %{qt4devname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%if "%{scmrev}" == ""
%setup -q
%else
%setup -q -n %{name}-%{scmrev}
%endif
%cmake_qt5

%build
%make -C build

%install
%makeinstall_std -C build


%files -n %{libname}
%{_libdir}/*sysstat-qt5.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/sysstat-qt5

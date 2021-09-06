#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kqtquickcharts
Version  : 21.08.1
Release  : 29
URL      : https://download.kde.org/stable/release-service/21.08.1/src/kqtquickcharts-21.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.1/src/kqtquickcharts-21.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.1/src/kqtquickcharts-21.08.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kqtquickcharts-lib = %{version}-%{release}
Requires: kqtquickcharts-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev mesa-dev

%description
kqtquickcharts
==============
Beautiful and interactive charts for Qt Quick
## Installation

%package dev
Summary: dev components for the kqtquickcharts package.
Group: Development
Requires: kqtquickcharts-lib = %{version}-%{release}
Provides: kqtquickcharts-devel = %{version}-%{release}
Requires: kqtquickcharts = %{version}-%{release}

%description dev
dev components for the kqtquickcharts package.


%package lib
Summary: lib components for the kqtquickcharts package.
Group: Libraries
Requires: kqtquickcharts-license = %{version}-%{release}

%description lib
lib components for the kqtquickcharts package.


%package license
Summary: license components for the kqtquickcharts package.
Group: Default

%description license
license components for the kqtquickcharts package.


%prep
%setup -q -n kqtquickcharts-21.08.1
cd %{_builddir}/kqtquickcharts-21.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630896419
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1630896419
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kqtquickcharts
cp %{_builddir}/kqtquickcharts-21.08.1/COPYING %{buildroot}/usr/share/package-licenses/kqtquickcharts/f425e50e051b87590a5c1ac4d6f52506ff12d134
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/kqtquickcharts_version.h
/usr/lib64/cmake/KQtQuickCharts/KQtQuickChartsVersion.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/qml/org/kde/charts/BarChart.qml
/usr/lib64/qt5/qml/org/kde/charts/Label.qml
/usr/lib64/qt5/qml/org/kde/charts/LegendItem.qml
/usr/lib64/qt5/qml/org/kde/charts/LineChart.qml
/usr/lib64/qt5/qml/org/kde/charts/LineLabel.qml
/usr/lib64/qt5/qml/org/kde/charts/XYChart.qml
/usr/lib64/qt5/qml/org/kde/charts/libkqtquickcharts.so
/usr/lib64/qt5/qml/org/kde/charts/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kqtquickcharts/f425e50e051b87590a5c1ac4d6f52506ff12d134

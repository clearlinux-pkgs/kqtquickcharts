#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kqtquickcharts
Version  : 20.04.0
Release  : 18
URL      : https://download.kde.org/stable/release-service/20.04.0/src/kqtquickcharts-20.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.0/src/kqtquickcharts-20.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.0/src/kqtquickcharts-20.04.0.tar.xz.sig
Summary  : A QtQuick plugin to render beautiful and interactive charts
Group    : Development/Tools
License  : LGPL-2.1
Requires: kqtquickcharts-lib = %{version}-%{release}
Requires: kqtquickcharts-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
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
%setup -q -n kqtquickcharts-20.04.0
cd %{_builddir}/kqtquickcharts-20.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587687694
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1587687694
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kqtquickcharts
cp %{_builddir}/kqtquickcharts-20.04.0/COPYING %{buildroot}/usr/share/package-licenses/kqtquickcharts/f425e50e051b87590a5c1ac4d6f52506ff12d134
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

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v26
# autospec commit: 99a7985
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kxmlgui
Version  : 6.14.0
Release  : 114
URL      : https://download.kde.org/stable/frameworks/6.14/kxmlgui-6.14.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.14/kxmlgui-6.14.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.14/kxmlgui-6.14.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : User configurable main windows
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kxmlgui-data = %{version}-%{release}
Requires: kxmlgui-lib = %{version}-%{release}
Requires: kxmlgui-license = %{version}-%{release}
Requires: kxmlgui-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kauth-dev
BuildRequires : kcodecs-dev
BuildRequires : kcolorscheme-dev
BuildRequires : kconfig
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kglobalaccel
BuildRequires : kglobalaccel-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kitemviews-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : mesa-dev
BuildRequires : python3-dev
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
BuildRequires : qt6tools-dev
BuildRequires : qttools-dev
BuildRequires : sonnet-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KXMLGUI
Framework for managing menu and toolbar actions
## Introduction
KXMLGUI provides a framework for managing menu and toolbar actions in an
abstract way. The actions are configured through a XML description and hooks
in the application code. The framework supports merging of multiple
description for example for integrating actions from plugins.

%package data
Summary: data components for the kxmlgui package.
Group: Data

%description data
data components for the kxmlgui package.


%package dev
Summary: dev components for the kxmlgui package.
Group: Development
Requires: kxmlgui-lib = %{version}-%{release}
Requires: kxmlgui-data = %{version}-%{release}
Provides: kxmlgui-devel = %{version}-%{release}
Requires: kxmlgui = %{version}-%{release}

%description dev
dev components for the kxmlgui package.


%package lib
Summary: lib components for the kxmlgui package.
Group: Libraries
Requires: kxmlgui-data = %{version}-%{release}
Requires: kxmlgui-license = %{version}-%{release}

%description lib
lib components for the kxmlgui package.


%package license
Summary: license components for the kxmlgui package.
Group: Default

%description license
license components for the kxmlgui package.


%package locales
Summary: locales components for the kxmlgui package.
Group: Default

%description locales
locales components for the kxmlgui package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kxmlgui-6.14.0
cd %{_builddir}/kxmlgui-6.14.0
pushd ..
cp -a kxmlgui-6.14.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747088330
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1747088330
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kxmlgui
cp %{_builddir}/kxmlgui-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kxmlgui/ea97eb88ae53ec41e26f8542176ab986d7bc943a || :
cp %{_builddir}/kxmlgui-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kxmlgui/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kxmlgui-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kxmlgui/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kxmlgui-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kxmlgui/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kxmlgui-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kxmlgui/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kxmlgui-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kxmlgui/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kxmlgui-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kxmlgui/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kxmlgui-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kxmlgui/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kxmlgui-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kxmlgui/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kxmlgui6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kxmlgui.categories
/usr/share/qlogging-categories6/kxmlgui.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KXmlGui/KAboutApplicationDialog
/usr/include/KF6/KXmlGui/KAboutPluginDialog
/usr/include/KF6/KXmlGui/KActionCategory
/usr/include/KF6/KXmlGui/KActionCollection
/usr/include/KF6/KXmlGui/KBugReport
/usr/include/KF6/KXmlGui/KEditToolBar
/usr/include/KF6/KXmlGui/KHelpMenu
/usr/include/KF6/KXmlGui/KKeySequenceWidget
/usr/include/KF6/KXmlGui/KMainWindow
/usr/include/KF6/KXmlGui/KShortcutWidget
/usr/include/KF6/KXmlGui/KShortcutsDialog
/usr/include/KF6/KXmlGui/KShortcutsEditor
/usr/include/KF6/KXmlGui/KToggleToolBarAction
/usr/include/KF6/KXmlGui/KToolBar
/usr/include/KF6/KXmlGui/KToolTipHelper
/usr/include/KF6/KXmlGui/KUndoActions
/usr/include/KF6/KXmlGui/KXMLGUIBuilder
/usr/include/KF6/KXmlGui/KXMLGUIClient
/usr/include/KF6/KXmlGui/KXMLGUIFactory
/usr/include/KF6/KXmlGui/KXmlGuiWindow
/usr/include/KF6/KXmlGui/kaboutapplicationdialog.h
/usr/include/KF6/KXmlGui/kaboutplugindialog.h
/usr/include/KF6/KXmlGui/kactioncategory.h
/usr/include/KF6/KXmlGui/kactioncollection.h
/usr/include/KF6/KXmlGui/kbugreport.h
/usr/include/KF6/KXmlGui/kedittoolbar.h
/usr/include/KF6/KXmlGui/khelpmenu.h
/usr/include/KF6/KXmlGui/kkeysequencewidget.h
/usr/include/KF6/KXmlGui/kmainwindow.h
/usr/include/KF6/KXmlGui/kshortcutsdialog.h
/usr/include/KF6/KXmlGui/kshortcutseditor.h
/usr/include/KF6/KXmlGui/kshortcutwidget.h
/usr/include/KF6/KXmlGui/ktoggletoolbaraction.h
/usr/include/KF6/KXmlGui/ktoolbar.h
/usr/include/KF6/KXmlGui/ktooltiphelper.h
/usr/include/KF6/KXmlGui/kundoactions.h
/usr/include/KF6/KXmlGui/kxmlgui_export.h
/usr/include/KF6/KXmlGui/kxmlgui_version.h
/usr/include/KF6/KXmlGui/kxmlguibuilder.h
/usr/include/KF6/KXmlGui/kxmlguiclient.h
/usr/include/KF6/KXmlGui/kxmlguifactory.h
/usr/include/KF6/KXmlGui/kxmlguiwindow.h
/usr/lib64/cmake/KF6XmlGui/KF6XmlGuiConfig.cmake
/usr/lib64/cmake/KF6XmlGui/KF6XmlGuiConfigVersion.cmake
/usr/lib64/cmake/KF6XmlGui/KF6XmlGuiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6XmlGui/KF6XmlGuiTargets.cmake
/usr/lib64/libKF6XmlGui.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6XmlGui.so.6.14.0
/V3/usr/lib64/qt6/plugins/designer/kxmlgui6widgets.so
/usr/lib64/libKF6XmlGui.so.6
/usr/lib64/libKF6XmlGui.so.6.14.0
/usr/lib64/qt6/plugins/designer/kxmlgui6widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kxmlgui/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kxmlgui/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kxmlgui/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kxmlgui/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kxmlgui/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kxmlgui/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kxmlgui/ea97eb88ae53ec41e26f8542176ab986d7bc943a

%files locales -f kxmlgui6.lang
%defattr(-,root,root,-)


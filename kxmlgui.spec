#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kxmlgui
Version  : 5.90.0
Release  : 64
URL      : https://download.kde.org/stable/frameworks/5.90/kxmlgui-5.90.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.90/kxmlgui-5.90.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.90/kxmlgui-5.90.0.tar.xz.sig
Summary  : User configurable main windows
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kxmlgui-data = %{version}-%{release}
Requires: kxmlgui-lib = %{version}-%{release}
Requires: kxmlgui-license = %{version}-%{release}
Requires: kxmlgui-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : kauth-dev
BuildRequires : kcodecs-dev
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
BuildRequires : qttools-dev
BuildRequires : sonnet-dev

%description
# Overall summary of global shortcut implementation
## KAction, KGlobalAccel and KdedGlobalAccel

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
%setup -q -n kxmlgui-5.90.0
cd %{_builddir}/kxmlgui-5.90.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642093363
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
export SOURCE_DATE_EPOCH=1642093363
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kxmlgui
cp %{_builddir}/kxmlgui-5.90.0/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kxmlgui/ea97eb88ae53ec41e26f8542176ab986d7bc943a
cp %{_builddir}/kxmlgui-5.90.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kxmlgui/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/kxmlgui-5.90.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kxmlgui/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kxmlgui-5.90.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kxmlgui/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kxmlgui-5.90.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kxmlgui/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kxmlgui-5.90.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kxmlgui/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kxmlgui-5.90.0/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kxmlgui/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/kxmlgui-5.90.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kxmlgui/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kxmlgui-5.90.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kxmlgui/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kxmlgui-5.90.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kxmlgui/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang kxmlgui5

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/ksendbugmail

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kxmlgui.categories
/usr/share/qlogging-categories5/kxmlgui.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KXmlGui/KAboutApplicationDialog
/usr/include/KF5/KXmlGui/KAboutPluginDialog
/usr/include/KF5/KXmlGui/KActionCategory
/usr/include/KF5/KXmlGui/KActionCollection
/usr/include/KF5/KXmlGui/KBugReport
/usr/include/KF5/KXmlGui/KEditToolBar
/usr/include/KF5/KXmlGui/KHelpMenu
/usr/include/KF5/KXmlGui/KKeySequenceWidget
/usr/include/KF5/KXmlGui/KMainWindow
/usr/include/KF5/KXmlGui/KShortcutWidget
/usr/include/KF5/KXmlGui/KShortcutsDialog
/usr/include/KF5/KXmlGui/KShortcutsEditor
/usr/include/KF5/KXmlGui/KToggleToolBarAction
/usr/include/KF5/KXmlGui/KToolBar
/usr/include/KF5/KXmlGui/KToolTipHelper
/usr/include/KF5/KXmlGui/KUndoActions
/usr/include/KF5/KXmlGui/KXMLGUIBuilder
/usr/include/KF5/KXmlGui/KXMLGUIClient
/usr/include/KF5/KXmlGui/KXMLGUIFactory
/usr/include/KF5/KXmlGui/KXmlGuiWindow
/usr/include/KF5/KXmlGui/kaboutapplicationdialog.h
/usr/include/KF5/KXmlGui/kaboutplugindialog.h
/usr/include/KF5/KXmlGui/kactioncategory.h
/usr/include/KF5/KXmlGui/kactioncollection.h
/usr/include/KF5/KXmlGui/kbugreport.h
/usr/include/KF5/KXmlGui/kedittoolbar.h
/usr/include/KF5/KXmlGui/khelpmenu.h
/usr/include/KF5/KXmlGui/kkeysequencewidget.h
/usr/include/KF5/KXmlGui/kmainwindow.h
/usr/include/KF5/KXmlGui/kshortcutsdialog.h
/usr/include/KF5/KXmlGui/kshortcutseditor.h
/usr/include/KF5/KXmlGui/kshortcutwidget.h
/usr/include/KF5/KXmlGui/ktoggletoolbaraction.h
/usr/include/KF5/KXmlGui/ktoolbar.h
/usr/include/KF5/KXmlGui/ktooltiphelper.h
/usr/include/KF5/KXmlGui/kundoactions.h
/usr/include/KF5/KXmlGui/kxmlgui_export.h
/usr/include/KF5/KXmlGui/kxmlguibuilder.h
/usr/include/KF5/KXmlGui/kxmlguiclient.h
/usr/include/KF5/KXmlGui/kxmlguifactory.h
/usr/include/KF5/KXmlGui/kxmlguiwindow.h
/usr/include/KF5/kxmlgui_version.h
/usr/lib64/cmake/KF5XmlGui/KF5XmlGuiConfig.cmake
/usr/lib64/cmake/KF5XmlGui/KF5XmlGuiConfigVersion.cmake
/usr/lib64/cmake/KF5XmlGui/KF5XmlGuiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5XmlGui/KF5XmlGuiTargets.cmake
/usr/lib64/libKF5XmlGui.so
/usr/lib64/qt5/mkspecs/modules/qt_KXmlGui.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5XmlGui.so.5
/usr/lib64/libKF5XmlGui.so.5.90.0
/usr/lib64/qt5/plugins/designer/kxmlgui5widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kxmlgui/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kxmlgui/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kxmlgui/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kxmlgui/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kxmlgui/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kxmlgui/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kxmlgui/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/kxmlgui/ea97eb88ae53ec41e26f8542176ab986d7bc943a

%files locales -f kxmlgui5.lang
%defattr(-,root,root,-)


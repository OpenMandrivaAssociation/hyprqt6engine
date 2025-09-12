Name:		hyprqt6engine
Version:	0.1.0
Release:	1
URL:		https://github.com/hyprwm/hyprqt6engine
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Merge Request submitted upstream to fix issue
Patch0:     FixedGuiPrivate.patch
Summary:	QT6 Theme Provider for Hyprland
License:	BSD-3-Clause
Group:		Window Manager/Hyprland

BuildSystem:	cmake

BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(hyprlang)
BuildRequires:	pkgconfig(hyprutils)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(Qt6QmlCore)
BuildRequires:	vulkan-headers
BuildRequires:	cmake(Qt6LabsSynchronizer)
BuildRequires:	cmake(Qt6QmlAssetDownloader)
BuildRequires:	cmake(Qt6QmlNetwork)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(Qt6ExamplesAssetDownloaderPrivate)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Gui)


%description
QT6 Theme Provider for Hyprland. Compatible with KDE, replaces qt6ct.

%prep
%autosetup -p1

%files
%license LICENSE
%{_libdir}/lib%{name}-common.so
%{_qtdir}/plugins/platformthemes/lib%{name}.so
%{_qtdir}/plugins/styles/libhypr-style.so

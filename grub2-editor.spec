%define snap 20160124

Summary:	Grub2 editor
Name:		grub2-editor
Version:	0.5.8
Release:	1.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		https://github.com/maz-1/grub2-editor
# git clone https://github.com/maz-1/grub2-editor.git
# git archive --format=tar --prefix grub2-editor-0.5.8-$(date +%Y%m%d)/ HEAD | xz -vf > grub2-editor-0.5.8-$(date +%Y%m%d).tar.xz

Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(MagickCore)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	grub2
BuildRequires:	os-prober

%description
A KDE Control Module for configuring the GRUB2 bootloader.
Unofficial KF5 port.

%prep
%setup -qn %{name}-%{version}-%{snap}
%cmake_kde5
%build
%ninja -C build

%install
%ninja_install -C build

%files

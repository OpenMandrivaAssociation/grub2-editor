%define snap %nil

Summary:	Grub2 editor
Name:		grub2-editor
Version:	0.7.0
Release:	1
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		https://github.com/maz-1/grub2-editor
# git clone https://github.com/maz-1/grub2-editor.git
# git archive --format=tar --prefix grub2-editor-0.5.8-$(date +%Y%m%d)/ HEAD | xz -vf > grub2-editor-0.5.8-$(date +%Y%m%d).tar.xz

Source0:	%{name}-%{version}.tar.gz
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
%setup -q
%cmake_kde5 -DGRUB_INSTALL_EXE=%{_sbindir}/grub2-install \
			-DGRUB_MKCONFIG_EXE=%{_sbindir}/grub2-mkconfig \
            -DGRUB_PROBE_EXE=%{_sbindir}/grub2-probe \
            -DGRUB_SET_DEFAULT_EXE=%{_sbindir}/grub2-set-default \
            -DGRUB_MAKE_PASSWD_EXE=%{_bindir}/grub2-mkpasswd-pbkdf2

%build
%ninja -C build

%install
%ninja_install -C build

%files

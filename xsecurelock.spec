Name:           xsecurelock
Version:        1.7.0
Release:        1%{?dist}
Summary:        X11 screen lock utility with security in mind
License:        ASL 2.0
URL:            https://opensource.google/projects/xsecurelock

Source0:        https://github.com/google/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc libX11-devel libXmu-devel libXcomposite-devel pam-devel libpamtest-devel pamtester
 

%description
XSecureLock is an X11 screen lock utility designed with the primary goal of security.

%prep
%autosetup

%build
%configure --with-pam-service-name=xscreensaver
make %{?_smp_flags}

%install
%make_install


%files
%license LICENSE CONTRIBUTING
%doc README.md doc/xsecurelock.1* LICENSE CONTRIBUTING doc/examples/saver_livestreams
%{_bindir}/%{name}
%{_libexecdir}/%{name}/auth_x11
%{_libexecdir}/%{name}/authproto_pam
%{_libexecdir}/%{name}/authproto_pamtester
%{_libexecdir}/%{name}/dimmer
%{_libexecdir}/%{name}/pgrp_placeholder
%{_libexecdir}/%{name}/saver_blank
%{_libexecdir}/%{name}/saver_multiplex
%{_libexecdir}/%{name}/until_nonidle


%changelog
* Fri Feb 21 2020 Sam P <survient@fedoraproject.org>
- 

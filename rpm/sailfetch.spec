Name:       sailfetch
Summary:    Sailfetch
Version:    1.0.0
Release:    1
BuildArch:  noarch
Group:      Qt/Qt
License:    GPLv3
URL:        http://github.com/direc85/sailfetch
Source0:    %{name}-%{version}.tar.bz2
Requires:   busybox

%description
Sailfetch is a minimal Neofetch-like script for your Sailfish OS device!

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp %{_sourcedir}/../%{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/sailfetch


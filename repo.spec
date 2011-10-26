Summary:	Repository management tool built on top of Git
Name:		repo
Version:	1.13
Release:	1
License:	Apache v2.0
Group:		Development/Tools
Source0:	https://dl-ssl.google.com/dl/googlesource/git-%{name}/repo
# Source0-md5:	b9b310257d4a03fd38c13774213063cd
URL:		https://source.android.com/source/version-control.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Repo unifies the many Git repositories when necessary, can do uploads
to revision control system. Repo is not meant to replace Git, only to
make it easier to work with Git.

%prep
%setup -qcT
%{__sed} -e '1s,#!.*bin/sh,#!%{__python},' %{SOURCE0} > %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/repo

Name:           snzip
Version:        1.0.3
Release:        4%{?dist}
Summary:        compression/decompression tool based on snappy

License:        BSD
URL:            https://github.com/kubo/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf, automake, libtool, gcc, gcc-c++, snappy-devel

%description
Snzip is one of command line tools using snappy.
This supports several file formats; framing-format, old framing-format, hadoop-snappy format,
raw format and obsolete three formats used by snzip, snappy-java 
and snappy-in-java before official framing-format was defined.
The default format is framing-format.

%prep
%autosetup


%build
autoreconf -fvi
%configure
%make_build
echo -e '#! /bin/bash\nsnzip -d "$@"' > snunzip

%install
%make_install
install -Dpm0755 snunzip %{buildroot}%{_bindir}/snunzip
rm %{buildroot}%{_docdir}/snzip/{COPYING,INSTALL,README.md,AUTHORS,ChangeLog,NEWS} || :

%files
%license COPYING
%doc README.md AUTHORS ChangeLog NEWS
%{_bindir}/snzip
%{_bindir}/snunzip

%changelog
* Thu Aug 25 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.0.3-4
- remove installed docs to make build work on epel

* Thu Aug 25 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.0.3-3
- Add snunzip

* Tue Aug 23 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.0.3-2
- Add missing BuildRequire snappy-devel

* Tue Aug 23 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.0.3-1
- initial package

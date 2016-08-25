Name:           snzip
Version:        1.0.3
Release:        1%{?dist}
Summary:        compression/decompression tool based on snappy

License:        BSD
URL:            https://github.com/kubo/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf, automake, libtool, gcc, gcc-c++

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

%install
%make_install
rm %{buildroot}%{_docdir}/snzip/{COPYING,INSTALL} || :

%files
%license COPYING
%doc README.md AUTHORS ChangeLog NEWS
%{_bindir}/snzip

%changelog
* Tue Aug 23 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.0.3-1
- initial package

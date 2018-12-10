Name:           Bear
Version:        2.3.13
Release:        1%{?dist}
Summary:        A tool to generate compilation database for clang tooling.

License:        GPLv3
URL:            https://github.com/rizsotto/Bear
Source0:        https://github.com/rizsotto/Bear/archive/%{version}.tar.gz

%description
Bear is a tool that generates a compilation database for clang tooling.

%prep
%setup -q

%define generate_debuginfo() ( \
cp %1{,.debug}; \
objcopy --only-keep-debug "%1.debug"; \
strip --strip-debug --strip-unneeded "%1"; \
objcopy "--add-gnu-debuglink=%1.debug" "%1")

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_FLAGS=-g
%{__make} %{?jobs:-j%jobs}


%install
%{__make} DESTDIR=%{buildroot} install


%files
%{_bindir}/bear
%{_libdir}/bear/libear.so
%{_docdir}/bear/COPYING
%{_docdir}/bear/ChangeLog.md
%{_docdir}/bear/README.md
%{_mandir}/man1/bear.1.gz


%changelog
* Sun Dec 09 2018 Saggi Mizrahi <saggi@mizrahi.cc>
* Fri May 26 2017 Dhruv Paranjape <lord.dhruv@gmail.com>

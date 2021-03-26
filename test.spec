Name: test
Version: 1
Release: 1%{?dist}
Summary: Test
License: Public Domain
URL: https://github.com/junaruga/report-clang-12-with-flags-arm32-error
BuildRequires: clang

%description

%prep
cat > test.c <<EOF
int main(void) {
    return 0;
}
EOF

%build
clang --version
clang++ --version

%global toolchain clang
clang test.c -o test %{build_cflags}

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 test %{buildroot}/%{_bindir}/test

%files
%{_bindir}/test

%changelog
* Fri Mar 26 2021 Jun Aruga <jaruga@redhat.com>
- Init.

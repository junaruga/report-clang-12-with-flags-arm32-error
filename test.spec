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
    int class=0;
    return class;
}
EOF

%build
clang --version
clang++ --version
clang test.c -o test -flto -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS --config /usr/lib/rpm/redhat/redhat-hardened-clang.cfg -fstack-protector-strong -march=armv7-a -mfpu=vfpv3-d16 -mtune=generic-armv7-a -mabi=aapcs-linux -mfloat-abi=hard -pipe -D_FILE_OFFSET_BITS=64

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 test %{buildroot}/%{_bindir}/test

%files
%{_bindir}/test

%changelog
* Fri Mar 26 2021 Jun Aruga <jaruga@redhat.com>
- Init.

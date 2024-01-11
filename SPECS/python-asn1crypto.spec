# Created by pyp2rpm-3.2.2
%global pypi_name asn1crypto

%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

%{!?python3_pkgversion:%global python3_pkgversion 3}

Name:           python-%{pypi_name}
Version:        0.24.0
Release:        3%{?dist}
Summary:        Fast Python ASN.1 parser and serializer

License:        MIT
URL:            https://github.com/wbond/asn1crypto
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif
%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%description
Fast ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8,
PKCS#12, PKCS#5, X.509 and TSP.

%if 0%{?with_python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Fast ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8,
PKCS#12, PKCS#5, X.509 and TSP.
%endif

%if 0%{?with_python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Fast ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8,
PKCS#12, PKCS#5, X.509 and TSP.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif


%check
# asn1crypto source distribution doesn't come with tests
# {__python2} setup.py test
%if 0%{?with_python3}
# {__python3} setup.py test
%endif

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%doc
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Tue Jun 19 2018 Christian Heimes <cheimes@redhat.com> - 0.24.0-3
- Drop Python 2 subpackages from RHEL 8, fixes RHBZ#1589755

* Wed May 09 2018 Troy Dawson <tdawson@redhat.com> - 0.24.0-2
- Cleanup spec file conditionals

* Wed Mar 21 2018 Christian Heimes <cheimes@redhat.com> - 0.24.0-1
- New upstream release 0.24.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Christian Heimes <cheimes@redhat.com> - 0.23-1
- New upstream release 0.23.0

* Fri Aug 04 2017 Christian Heimes <cheimes@redhat.com> - 0.22.0-5
- Use python2-setuptools, add with_python3

* Thu Aug 03 2017 Christian Heimes <cheimes@redhat.com> - 0.22.0-4
- Modernize spec

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Christian Heimes <cheimes@redhat.com> - 0.22.0-2
- Address rpmlint issues

* Tue Jun 27 2017 Christian Heimes <cheimes@redhat.com> - 0.22.0-1
- Initial package.

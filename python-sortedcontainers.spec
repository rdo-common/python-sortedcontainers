%global srcname sortedcontainers

Name:           python-%{srcname}
Version:        2.0.1
Release:        2%{?dist}
Summary:        Pure Python sorted container types

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
# https://github.com/grantjenks/python-sortedcontainers/issues/91
Source1:        https://github.com/grantjenks/python-sortedcontainers/raw/master/docs/_templates/gumroad.html

BuildArch:      noarch

%global _description \
SortedContainers is an Apache2 licensed sorted collections library, written in \
pure-Python, and fast as C-extensions.

%description %{_description}

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python2-pytest
BuildRequires:  python2-matplotlib
BuildRequires:  python2-numpy
BuildRequires:  python2-scipy

%description -n python2-%{srcname} %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-matplotlib
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-sphinx
BuildRequires:  dvipng
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(bm.sty)

%description -n python3-%{srcname} %{_description}


%package -n python-%{srcname}-doc
Summary:        %{summary}

%description -n python-%{srcname}-doc
Documentation for %{srcname} package.


%prep
%autosetup -n %{srcname}-%{version}
mkdir docs/_templates
cp -a %SOURCE1 docs/_templates/


%build
%py2_build
%py3_build

pushd docs
make SPHINXBUILD=sphinx-build-%{python3_version} html
rm _build/html/.buildinfo
popd


%install
%py2_install
%py3_install


%check
pushd tests
PYTHONPATH="%{buildroot}%{python2_sitelib}" \
    pytest-2
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    pytest-%{python3_version}
popd


%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py?.?.egg-info


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info


%files -n python-%{srcname}-doc
%license LICENSE
%doc README.rst docs/_build/html


%changelog
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.7

* Sat May 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Update to latest version.

* Sun Apr 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.10-1
- Update to latest version.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.9-1
- Update to latest version.

* Sun Sep 03 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.7-3
- Split out documentation subpackage.

* Sat Sep 02 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.7-2
- Shorten summary and description.
- Standardize spec a bit more.

* Mon Feb 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.7-1
- Initial package release.

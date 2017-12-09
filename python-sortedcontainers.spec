%global srcname sortedcontainers

Name:           python-%{srcname}
Version:        1.5.9
Release:        1%{?dist}
Summary:        Pure Python sorted container types

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
SortedContainers is an Apache2 licensed sorted collections library, written in \
pure-Python, and fast as C-extensions.

%description %{_description}

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python2-nose

%description -n python2-%{srcname} %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-nose
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
    nosetests
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    nosetests-%{python3_version}
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
* Fri Dec 08 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5.9-1
- Update to latest version.

* Sun Sep 03 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5.7-3
- Split out documentation subpackage.

* Sat Sep 02 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5.7-2
- Shorten summary and description.
- Standardize spec a bit more.

* Mon Feb 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5.7-1
- Initial package release.

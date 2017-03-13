%{?scl:%scl_package nodejs-dezalgo}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-dezalgo

%global npm_name dezalgo
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-dezalgo
Version:    1.0.3
Release:    1%{?dist}
Summary:	Contain async insanity so that the dark pony lord doesn't eat souls
Url:		https://github.com/npm/dezalgo
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}npm(tap)
%endif

Requires: %{?scl_prefix}npm(asap)
Requires: %{?scl_prefix}npm(wrappy)

%description
Contain async insanity so that the dark pony lord doesn't eat souls

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json dezalgo.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/dezalgo

%doc README.md
%doc LICENSE

%changelog
* Tue Sep 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-1
- Updated with script

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-4
- rebuilt

* Thu Nov 26 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-3
- Enable scl macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- New upstream release
- added %%license

* Wed May 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- Initial build

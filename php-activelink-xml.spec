Summary:	ActiveLink PHP XML Package
Name:		php-activelink-xml
Version:	0.4.0
Release:	0.1
License:	LGPL 2.1
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/project/php-xml/php-xml/PHP-XML-Package-%{version}/ActiveLink-PHP-XML-Package-%{version}.tar.gz
# Source0-md5:	e95e190b4555ce493edafa7dd09f994e
URL:		http://php-xml.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}/active-link.xml
%define		_phpdocdir		%{_docdir}/phpdoc

%description
ActiveLink PHP XML Package provides an easy interface to parse, read,
modify, and output XML and XML documents. ActiveLink PHP XML Package
is purely implemented in PHP and does not require any PHP XML
extensions (including xml or domXML).

Provided classes are: XML, XMLDocument, XMLBranch, XMLLeaf, RSS, Tag,
Tree, Branch, Leaf, File.

%package phpdoc
Summary:	Online manual for ActiveLink PHP XML Package
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for %{name}.

%description phpdoc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a classes/* $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{name}
cp -a doc/* $RPM_BUILD_ROOT%{_phpdocdir}/%{name}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{_appdir}
%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{name}

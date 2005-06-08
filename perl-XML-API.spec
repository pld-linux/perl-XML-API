#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	API
Summary:	XML::API - Perl extension for creating XML documents
Name:		perl-XML-API
Version:	0.05
Release:	0.1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aae812e5f4a9b915d734d20c8c80ae71
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::API is a class for creating XML documents using object method
calls. This class is meant for generating XML programatically and not
for reading or parsing it.

The methods of a XML::API object are derived directly from the XML
Schema Definition document for the desired document type. A document
author calls the desired methods (representing elements) to create an
XML tree in memory which can then be rendered or saved as desired. The
advantage of having the in-memory tree is that you can be very
flexible about when different parts of the document are created and
the final output is always nicely rendered.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/API
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

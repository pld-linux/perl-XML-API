#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	XML
%define	pnam	API
%include	/usr/lib/rpm/macros.perl
Summary:	XML::API - Perl extension for creating XML documents
Summary(pl.UTF-8):	XML::API - rozszerzenie Perla do tworzenia dokumentów XML
Name:		perl-XML-API
Version:	0.25
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9558636dba8f8d415e9bf7f61b1dbde3
URL:		http://search.cpan.org/dist/XML-API/
BuildRequires:	perl(XML::LibXML::SAX)
BuildRequires:	perl-XML-Parser
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

%description -l pl.UTF-8
XML::API to klasa do tworzenia dokumentów XML przy użyciu wywołań
metod obiektów. Ta klasa służy do programowego generowania XML-a, ale
nie czytania czy przetwarzania go.

Metody obiektu XML::API wywodzą się bezpośrednio z dokumentu XML
Schema Definition dla żądanego typu dokumentu. Autor dokumentu
wywołuje odpowiednie metody (reprezentujące elementy), aby stworzyć w
pamięci drzewo XML, które może być wyrenderowane albo zapisane. Zaletą
posiadania drzewa w pamięci jest duża elastyczność przy tworzeniu
różnych części dokumentu i ładny rendering ostatecznego wyjścia.

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

%define buildall 0

Name:    kde-l10n
Summary: Internationalization support for KDE
Version: 4.10.5
Release: 2%{?dist}

Url:     http://www.kde.org
License: LGPLv2
BuildArch: noarch
# optimize simple noarch pkg, no debuginfo
%define debug_package   %{nil}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source1: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-ar-%{version}.tar.xz
Source2: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-bg-%{version}.tar.xz
Source3: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-bs-%{version}.tar.xz
Source4: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-ca-%{version}.tar.xz
Source5: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-ca@valencia-%{version}.tar.xz
Source6: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-cs-%{version}.tar.xz
#Source7: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-csb-%{version}.tar.xz
Source10: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-da-%{version}.tar.xz
Source11: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-de-%{version}.tar.xz
Source12: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-el-%{version}.tar.xz
Source13: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-en_GB-%{version}.tar.xz
#Source14: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-eo-%{version}.tar.xz
Source15: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-es-%{version}.tar.xz
Source16: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-et-%{version}.tar.xz
Source17: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-eu-%{version}.tar.xz
Source19: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-fa-%{version}.tar.xz
Source20: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-fi-%{version}.tar.xz
Source21: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-fr-%{version}.tar.xz
#Source22: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-fy-%{version}.tar.xz
Source23: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-ga-%{version}.tar.xz
Source24: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-gl-%{version}.tar.xz
#Source25: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-gu-%{version}.tar.xz
Source30: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-he-%{version}.tar.xz
Source31: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-hi-%{version}.tar.xz
Source32: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-hr-%{version}.tar.xz
Source33: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-hu-%{version}.tar.xz
Source34: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-ia-%{version}.tar.xz
#Source35: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-id-%{version}.tar.xz
Source36: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-is-%{version}.tar.xz
Source37: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-it-%{version}.tar.xz
Source40: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-ja-%{version}.tar.xz
Source41: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-kk-%{version}.tar.xz
Source42: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-km-%{version}.tar.xz
#Source43: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-kn-%{version}.tar.xz
Source44: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-ko-%{version}.tar.xz
Source45: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-lt-%{version}.tar.xz
Source46: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-lv-%{version}.tar.xz
#Source50: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-mai-%{version}.tar.xz
#Source51: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-mk-%{version}.tar.xz
Source52: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-mr-%{version}.tar.xz
Source53: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-nb-%{version}.tar.xz
Source54: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-nds-%{version}.tar.xz
Source55: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-nl-%{version}.tar.xz
Source56: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-nn-%{version}.tar.xz
Source60: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-pa-%{version}.tar.xz
Source61: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-pl-%{version}.tar.xz
Source62: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-pt-%{version}.tar.xz
Source63: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-pt_BR-%{version}.tar.xz
Source64: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-ro-%{version}.tar.xz
Source65: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-ru-%{version}.tar.xz
Source70: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-sk-%{version}.tar.xz
Source71: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-si-%{version}.tar.xz
Source72: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-sl-%{version}.tar.xz
Source73: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-sr-%{version}.tar.xz
Source74: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-sv-%{version}.tar.xz
Source75: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-tg-%{version}.tar.xz
Source76: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-th-%{version}.tar.xz
Source77: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-tr-%{version}.tar.xz
Source78: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-ug-%{version}.tar.xz
Source80: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-uk-%{version}.tar.xz
Source81: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-vi-%{version}.tar.xz
Source82: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-wa-%{version}.tar.xz
Source83: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-zh_CN-%{version}.tar.xz
Source84: http://download.kde.org/%{stable}/%{version}/src/kde-l10n/%{name}-zh_TW-%{version}.tar.xz
Source1000: subdirs-kde-l10n

BuildRequires: cmake
BuildRequires: findutils
BuildRequires: gettext
BuildRequires: kdelibs4-devel >= %{version} 

Requires: kde-filesystem

# klickety moved kde-i18n -> kde-l10n (#656523)
Conflicts: kde-i18n < 1:3.5.10-13

# Unfortunately, these are currently not available
Obsoletes: kde-l10n-Kurdish < 4.3.98
Obsoletes: kde-l10n-Bengali-India < 4.4.0
Obsoletes: kde-l10n-Chhattisgarhi < 4.4.0
Obsoletes: kde-l10n-Marathi < 4.4.0
Obsoletes: kde-l10n-Kashubian < 4.5.0
Obsoletes: kde-l10n-Macedonian < 4.5.0
Obsoletes: kde-l10n-Esperanto < 4.6.0
Obsoletes: kde-l10n-Frisian < 4.6.0
Obsoletes: kde-l10n-Malayalam < 4.6.0
Obsoletes: kde-l10n-Gujarati < 4.7.0
Obsoletes: kde-l10n-Maithili < 4.7.0
Obsoletes: kde-l10n-Kannada < 4.8.0
Obsoletes: kde-l10n-Indonesian < 4.9.0

%description
Internationalization support for KDE.

%package Afrikaans
Summary: Afrikaans language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-af = %{version}-%{release}
%description Afrikaans
%{summary}.

%package Arabic 
Summary: Arabic language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ar = %{version}-%{release}
%description Arabic
%{summary}.

%package Azerbaijani
Summary: Azerbaijani language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-af = %{version}-%{release}
%description Azerbaijani
%{summary}.

%package Basque
Summary: Basque language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-eu = %{version}-%{release}
%description Basque
%{summary}.

%package Belarusian
Summary: Belarusian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-be = %{version}-%{release}
%description Belarusian
%{summary}.

%package Bengali-India
Summary: Bengali India language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-bn_IN = %{version}-%{release}
Obsoletes: %{name}-Bengali
%description Bengali-India
%{summary}.

%package Bulgarian
Summary: Bulgarian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-bg = %{version}-%{release}
%description Bulgarian
%{summary}.

%package Tibetan
Summary: Tibetan language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-bo = %{version}-%{release}
%description Tibetan
%{summary}.

%package Breton
Summary: Breton language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-br = %{version}-%{release}
%description Breton
%{summary}.

%package Bosnian
Summary: Bosnian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-bs = %{version}-%{release}
%description Bosnian
%{summary}.

%package Catalan
Summary: Catalan language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ca = %{version}-%{release}
%description Catalan
%{summary}.

%package Catalan-Valencian
Summary: Catalan (Valencian) language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ca-valencia = %{version}-%{release}
%description Catalan-Valencian
%{summary}.

%package Czech
Summary: Czech language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-cs = %{version}-%{release}
%description Czech
%{summary}.

%package Welsh
Summary: Welsh language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-cy = %{version}-%{release}
%description Welsh
%{summary}.

%package Danish
Summary: Danish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-da = %{version}-%{release}
%description Danish
%{summary}.

%package German
Summary: German language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-de = %{version}-%{release}
%description German
%{summary}.

%package Greek
Summary: Greek language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-el = %{version}-%{release}
%description Greek
%{summary}.

%package Gujarati
Summary: Gujarati language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gu = %{version}-%{release}
%description Gujarati
%{summary}.

%package British
Summary: British English support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-en_GB = %{version}-%{release}
%description British
%{summary}.

%package Esperanto
Summary: Esperanto support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-eo = %{version}-%{release}
%description Esperanto
%{summary}.

%package Spanish
Summary: Spanish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-es = %{version}-%{release}
%description Spanish
%{summary}.

%package Estonian
Summary: Estonian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-et = %{version}-%{release}
%description Estonian
%{summary}.

%package Farsi
Summary: Farsi language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-fa = %{version}-%{release}
%description Farsi
%{summary}.

%package Finnish
Summary: Finnish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-fi = %{version}-%{release}
%description Finnish
%{summary}.

%package Faroese
Summary: Faroese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-fo = %{version}-%{release}
%description Faroese
%{summary}.

%package French
Summary: French language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-fr = %{version}-%{release}
%description French
%{summary}.

%package Frisian
Summary: Frisian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-fy = %{version}-%{release}
%description Frisian
%{summary}.

%package Irish
Summary: Irish language support for KDE
Group: User Interface/Desktops
Obsoletes: kde-i18n-Gaeilge
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ga = %{version}-%{release}
%description Irish
%{summary}.

%package Galician
Summary: Galician language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gl = %{version}-%{release}
%description Galician
%{summary}.

%package Hebrew
Summary: Hebrew language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-he = %{version}-%{release}
%description Hebrew
%{summary}.

%package Hindi
Summary: Hindi language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-hi = %{version}-%{release}
%description Hindi
%{summary}.

%package Chhattisgarhi 
Summary: Chhattisgarhi language support for KDE 
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-hne = %{version}-%{release}
%description Chhattisgarhi 
%{summary}.

%package Croatian
Summary: Croatian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-hr = %{version}-%{release}
%description Croatian
%{summary}.

%package Hungarian
Summary: Hungarian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-hu = %{version}-%{release}
%description Hungarian
%{summary}.

%package Interlingua
Summary: Interlingua language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ia = %{version}-%{release}
%description Interlingua
%{summary}.

%package Indonesian
Summary: Indonesian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-id = %{version}-%{release}
%description Indonesian
%{summary}.

%package Icelandic
Summary: Icelandic language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-is = %{version}-%{release}
%description Icelandic
%{summary}.

%package Italian
Summary: Italian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-it = %{version}-%{release}
%description Italian
%{summary}.

%package Japanese
Summary: Japanese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ja = %{version}-%{release}
%description Japanese
%{summary}.

%package Kannada
Summary: Kannada language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-kn = %{version}-%{release}
%description Kannada
%{summary}.

%package Kashubian
Summary: Kashubian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-csb = %{version}-%{release}
%description Kashubian
%{summary}.

%package Kazakh
Summary: Kazakh language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-kk = %{version}-%{release}
%description Kazakh
%{summary}.

%package Khmer
Summary: Khmer language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-km = %{version}-%{release}
%description Khmer
%{summary}.

%package Korean
Summary: Korean language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ko = %{version}-%{release}
%description Korean
%{summary}.

%package Kurdish
Summary: Kurdish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ku = %{version}-%{release}
%description Kurdish
%{summary}.

%package Lao
Summary: Lao language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-lo = %{version}-%{release}
%description Lao
%{summary}.

%package Lithuanian
Summary: Lithuanian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-lt = %{version}-%{release}
%description Lithuanian
%{summary}.

%package Latvian
Summary: Latvian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-lv = %{version}-%{release}
%description Latvian
%{summary}.

%package LowSaxon
Summary: Low Saxon language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-nds = %{version}-%{release}
%description LowSaxon
%{summary}.

%package Maori
Summary: Maori language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-mi = %{version}-%{release}
%description Maori
%{summary}.

%package Macedonian
Summary: Macedonian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-mk = %{version}-%{release}
%description Macedonian
%{summary}.

%package Maithili
Summary: Maithili language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-mai = %{version}-%{release}
%description Maithili
%{summary}.

%package Malayalam
Summary: Malayalam language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ml = %{version}-%{release}
%description Malayalam
%{summary}.

%package Maltese
Summary: Maltese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-mt = %{version}-%{release}
%description Maltese
%{summary}.

%package Marathi
Summary: Marathi language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-mr = %{version}-%{release}
%description Marathi
%{summary}.

%package Nepali
Summary: Nepali language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ne = %{version}-%{release}
%description Nepali
%{summary}.

%package Dutch
Summary: Dutch language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-nl = %{version}-%{release}
%description Dutch
%{summary}.

%package NorthernSami
Summary: Northern Sami language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-se = %{version}-%{release}
%description NorthernSami
%{summary}.

%package Norwegian
Summary: Norwegian (Bokmaal) language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-no = %{version}-%{release}
%description Norwegian
%{summary}.

%package Norwegian-Nynorsk
Summary: Norwegian (Nynorsk) language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-nn = %{version}-%{release}
%description Norwegian-Nynorsk
%{summary}.

%package Occitan
Summary: Occitan language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-oc = %{version}-%{release}
%description Occitan
%{summary}.

%package Polish
Summary: Polish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-pl = %{version}-%{release}
%description Polish
%{summary}.

%package Portuguese
Summary: Portuguese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-pt = %{version}-%{release}
%description Portuguese
%{summary}.

%package Punjabi
Summary: Punjabi language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-pa = %{version}-%{release}
%description Punjabi
%{summary}.

%package Brazil
Summary: Brazil Portuguese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-pt_BR = %{version}-%{release}
%description Brazil
%{summary}.

%package Romanian
Summary: Romanian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ro = %{version}-%{release}
%description Romanian
%{summary}.

%package Russian
Summary: Russian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ru = %{version}-%{release}
%description Russian
%{summary}.

%package Sinhala
Summary: Sinhala language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-si = %{version}-%{release}
%description Sinhala
%{summary}.

%package Slovak
Summary: Slovak language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-sk = %{version}-%{release}
%description Slovak
%{summary}.

%package Slovenian
Summary: Slovenian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-sl = %{version}-%{release}
%description Slovenian
%{summary}.

%package Serbian
Summary: Serbian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-sr = %{version}-%{release}
%description Serbian
%{summary}.

%package Swedish
Summary: Swedish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-sv = %{version}-%{release}
%description Swedish
%{summary}.

%package Tamil
Summary: Tamil language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ta = %{version}-%{release}
%description Tamil
%{summary}.

%package Tajik
Summary: Tajik language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-tg = %{version}-%{release}
%description Tajik
%{summary}.

%package Thai
Summary: Thai language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-th = %{version}-%{release}
%description Thai
%{summary}.

%package Turkish
Summary: Turkish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-tr = %{version}-%{release}
%description Turkish
%{summary}.

%package Uyghur
Summary: Uyghur language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ug = %{version}-%{release}
%description Uyghur 
%{summary}.

%package Ukrainian
Summary: Ukrainian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-uk = %{version}-%{release}
%description Ukrainian
%{summary}.

%package Venda
Summary: Venda language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ven = %{version}-%{release}
%description Venda
%{summary}.

%package Vietnamese
Summary: Vietnamese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-vi = %{version}-%{release}
%description Vietnamese
%{summary}.

%package Walloon
Summary: Walloon language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-wa = %{version}-%{release}
%description Walloon
%{summary}.

%package Xhosa
Summary: Xhosa (a Bantu language) support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-xh = %{version}-%{release}
%description Xhosa
%{summary}.

%package Chinese
Summary: Chinese (Simplified Chinese) language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-zh_CN = %{version}-%{release}
%description Chinese
%{summary}.

%package Chinese-Traditional
Summary: Chinese (Traditional) language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-zh_TW = %{version}-%{release}
%description Chinese-Traditional
%{summary}.


%prep
%setup -T -q -n %{name}-%{version} -c

for i in $(cat %{SOURCE1000}) ; do
  echo $i | grep -v '^#' && \
  %{__xz} --decompress --stdout %{_sourcedir}/%{name}-$i-%{version}.tar.xz | %{__tar} -xf -
done


%build
for i in $(cat %{SOURCE1000}) ; do
  if [ -d "%{name}-$i-%{version}" ]; then
  pushd %{name}-$i-%{version}
  for j in . *@* ; do
    if [ -d $j ] ; then
      # skip kdewebdev for now, because we're still shipping kdewebdev 3 due to Quanta
      sed -i -e 's/add_subdirectory( *kdewebdev *)/#add_subdirectory(kdewebdev)/g' $j/messages/CMakeLists.txt
      if [ -e $j/docs/CMakeLists.txt ] ; then
        sed -i -e 's/add_subdirectory( *kdewebdev *)/#add_subdirectory(kdewebdev)/g' $j/docs/CMakeLists.txt
      fi
      # remove lilo-config, conflicts with 3.5.10
      rm -f $j/messages/kdeadmin/kcmlilo.po
      if [ -e $j/docs/kdeadmin/CMakeLists.txt ] ; then
        sed -i -e 's/add_subdirectory( *lilo-config *)/#add_subdirectory(lilo-config)/g' $j/docs/kdeadmin/CMakeLists.txt
      fi
      # remove bogus duplicated kdepim stuff from kdenetwork
      if [ -e $j/docs/kdenetwork/CMakeLists.txt ] ; then
        sed -i -e 's/add_subdirectory( *korn *)/#add_subdirectory(korn)/g' -e 's/add_subdirectory( *kmail *)/#add_subdirectory(kmail)/g' -e 's/add_subdirectory( *knode *)/#add_subdirectory(knode)/g' $j/docs/kdenetwork/CMakeLists.txt
      fi
      # some languages still ship the kpilot stuff
      # zap it so the kpilot package can ship all translations itself
      rm -f $j/messages/kdepim/kpilot.po
      if [ -e $j/docs/kdepim/CMakeLists.txt ] ; then
        sed -i -e 's/add_subdirectory( *kpilot *)/#add_subdirectory(kpilot)/g' $j/docs/kdepim/CMakeLists.txt
      fi
    fi
  done
  mkdir -p %{_target_platform}
  pushd %{_target_platform}
  %{cmake_kde4} ..
  popd
  make %{?_smp_mflags} -C %{_target_platform}
  popd
  fi
done


%install
for i in $(cat %{SOURCE1000}) ; do
  if [ -d %{name}-$i-%{version}/%{_target_platform} ]; then
  make install/fast DESTDIR=%{buildroot} -C %{name}-$i-%{version}/%{_target_platform}
  fi
done

# get rid of flags (which should be included in kde-runtime-flags?), currently:
# kde-l10n-km-4.5.1/messages/flag.png
# kde-l10n-th-4.5.1/messages/flag.png
# kde-l10n-zh_CN-4.5.1/messages/flag.png
# (get this fixed upstream) -- Rex
rm -rfv  %{buildroot}%{_datadir}/locale/*/flag.png


%files
# empty

%if %{buildall}
%files Afrikaans
%lang(af) %{_datadir}/locale/af/LC_MESSAGES/*
%lang(af) %{_datadir}/locale/af/entry.desktop
%endif

%files Arabic
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/*
%lang(ar) %{_datadir}/locale/ar/entry.desktop
%lang(ar) %{_datadir}/locale/ar/LC_SCRIPTS/
%lang(ar) %{_datadir}/kde4/apps/klettres/ar/

%if %{buildall}
%files Azerbaijani
%lang(az) %{_datadir}/locale/az/LC_MESSAGES/*
%lang(az) %{_datadir}/locale/az/entry.desktop
%endif

%if %{buildall}
%files Belarusian
%lang(be) %{_datadir}/locale/be/LC_MESSAGES/*
%lang(be) %{_datadir}/locale/be/entry.desktop
%endif

%files Bulgarian
%lang(bg) %{_datadir}/locale/bg/LC_MESSAGES/*
%lang(bg) %{_datadir}/locale/bg/entry.desktop
%lang(bg) %{_kde4_appsdir}/kvtml/bg/

%if %{buildall}
%files Bengali-India
%lang(bn_IN) %{_datadir}/locale/bn_IN/LC_MESSAGES/*
%lang(bn_IN) %{_datadir}/locale/bn_IN/entry.desktop
%endif

%if %{buildall}
%files Tibetan
%lang(bo) %{_datadir}/locale/bo/LC_MESSAGES/*
%lang(bo) %{_datadir}/locale/bo/entry.desktop
%endif

%if %{buildall}
%files Breton
%lang(br) %{_datadir}/locale/br/LC_MESSAGES/*
%lang(br) %{_datadir}/locale/br/entry.desktop
%endif

%files Bosnian
%lang(bs) %{_datadir}/locale/bs/LC_MESSAGES/*
%lang(bs) %{_datadir}/locale/bs/entry.desktop

%files Catalan
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/*
%lang(ca) %{_datadir}/locale/ca/LC_SCRIPTS/
%lang(ca) %{_datadir}/locale/ca/entry.desktop
%lang(ca) %{_kde4_appsdir}/autocorrect/ca.xml
%lang(ca) %{_kde4_appsdir}/khangman/ca.txt
%lang(ca) %{_kde4_appsdir}/ktuberling/sounds/ca*
%lang(ca) %{_kde4_appsdir}/kvtml/ca/
#lang(ca) %{_kde4_appsdir}/kvtml/latinCatalan*/
%lang(ca) %{_kde4_docdir}/HTML/ca/*
%lang(ca) %{_mandir}/ca/*/*

%files Catalan-Valencian
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/LC_MESSAGES/*
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/entry.desktop

%files Czech
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/*
%lang(cs) %{_datadir}/locale/cs/entry.desktop
%lang(cs) %{_kde4_appsdir}/autocorrect/cs.xml
%lang(cs) %{_kde4_appsdir}/khangman/cs.txt
%lang(cs) %{_kde4_appsdir}/klettres/cs/
%lang(cs) %{_kde4_appsdir}/kvtml/cs/
%lang(cs) %{_kde4_docdir}/HTML/cs/*

%if %{buildall}
%files Welsh
%lang(cy) %{_datadir}/locale/cy/LC_MESSAGES/*
%lang(cy) %{_datadir}/locale/cy/entry.desktop
%endif

%files Danish
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/*
%lang(da) %{_datadir}/locale/da/entry.desktop
%lang(da) %{_kde4_appsdir}/ktuberling/sounds/da*
%lang(da) %{_kde4_appsdir}/khangman/da.txt
%lang(da) %{_kde4_appsdir}/klettres/da/
%lang(da) %{_kde4_appsdir}/kvtml/da/
%lang(da) %{_kde4_docdir}/HTML/da/*
%lang(da) %{_mandir}/da/*/*

%files German
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
%lang(de) %{_datadir}/locale/de/LC_SCRIPTS/
%lang(de) %{_datadir}/locale/de/entry.desktop
%lang(de) %{_kde4_appsdir}/autocorrect/de_DE.xml
%lang(de) %{_kde4_appsdir}/kajongg/voices/de/
%lang(de) %{_kde4_appsdir}/klettres/de/
%lang(de) %{_kde4_appsdir}/ktuberling/sounds/de*
%lang(de) %{_kde4_appsdir}/khangman/de.txt
%lang(de) %{_kde4_appsdir}/kvtml/de/
%lang(de) %{_kde4_appsdir}/step/objinfo/l10n/de/
%lang(de) %{_kde4_docdir}/HTML/de/*
%lang(de) %{_mandir}/de/*/*

%files Greek
%lang(el) %{_datadir}/locale/el/LC_MESSAGES/*
%lang(el) %{_datadir}/locale/el/entry.desktop
%lang(el) %{_kde4_appsdir}/ktuberling/sounds/el*
%lang(el) %{_kde4_appsdir}/kvtml/el
%lang(el) %{_kde4_docdir}/HTML/el/*
%lang(el) %{_mandir}/el/*/*

%if %{buildall}
%files Gujarati
%lang(gu) %{_datadir}/locale/gu/LC_MESSAGES/*
%lang(gu) %{_datadir}/locale/gu/entry.desktop
%endif

%files British
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/*
%lang(en_GB) %{_datadir}/locale/en_GB/entry.desktop
%lang(en_GB) %{_kde4_appsdir}/klettres/en_GB/
%lang(en_GB) %{_kde4_appsdir}/kvtml/en_GB/
%lang(en_GB) %{_kde4_docdir}/HTML/en_GB/*
%lang(en_GB) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.en_GB.xml
%lang(en_GB) %{_kde4_appsdir}/kturtle/data/logokeywords.en_GB.xml
%lang(en_GB) %{_kde4_appsdir}/kturtle/examples/en_GB/*.logo

%if %{buildall}
%files Esperanto
%lang(eo) %{_datadir}/locale/eo/LC_MESSAGES/*
%lang(eo) %{_datadir}/locale/eo/entry.desktop
%lang(eo) %{_kde4_docdir}/HTML/eo/*
%endif

%files Spanish
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*
%lang(es) %{_datadir}/locale/es/entry.desktop
%lang(es) %{_kde4_appsdir}/autocorrect/es.xml
%lang(es) %{_kde4_appsdir}/ktuberling/sounds/es*
#lang(es) %{_kde4_appsdir}/khangman/data/es
%lang(es) %{_kde4_appsdir}/khangman/es.txt
%lang(es) %{_kde4_appsdir}/klettres/es/
%lang(es) %{_kde4_appsdir}/kvtml/es/
%lang(es) %{_kde4_docdir}/HTML/es/*
%lang(es) %{_mandir}/es/*/*

%files Estonian
%lang(et) %{_datadir}/locale/et/LC_MESSAGES/*
%lang(et) %{_datadir}/locale/et/entry.desktop
%lang(et) %{_kde4_appsdir}/khangman/et.txt
%lang(et) %{_kde4_appsdir}/kvtml/et/
%lang(et) %{_kde4_docdir}/HTML/et/*
%lang(et) %{_mandir}/et/*/*

%files Basque
%lang(eu) %{_datadir}/locale/eu/LC_MESSAGES/*
%lang(eu) %{_datadir}/locale/eu/entry.desktop
%lang(eu) %{_kde4_docdir}/HTML/eu/*

%files Farsi
%lang(fa) %{_datadir}/locale/fa/LC_MESSAGES/*
%lang(fa) %{_datadir}/locale/fa/entry.desktop

%files Finnish
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/*
%lang(fi) %{_datadir}/locale/fi/entry.desktop
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/
%lang(fi) %{_kde4_appsdir}/khangman/fi.txt
%lang(fi) %{_kde4_appsdir}/ktuberling/sounds/fi*
%lang(fi) %{_kde4_appsdir}/kvtml/fi/

%if %{buildall}
%files Faroese
%lang(fo) %{_datadir}/locale/fo/LC_MESSAGES/*
%lang(fo) %{_datadir}/locale/fo/entry.desktop
%endif

%files French
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*
%lang(fr) %{_datadir}/locale/fr/LC_SCRIPTS/
%lang(fr) %{_datadir}/locale/fr/entry.desktop
%lang(fr) %{_kde4_appsdir}/autocorrect/fr.xml
%lang(fr) %{_kde4_appsdir}/khangman/fr.txt
%lang(fr) %{_kde4_appsdir}/ktuberling/sounds/fr*
%lang(fr) %{_kde4_appsdir}/kvtml/fr/
%lang(fr) %{_kde4_docdir}/HTML/fr/*
%lang(fr) %{_mandir}/fr/*/*

%if %{buildall}
%files Frisian
%lang(fy) %{_datadir}/locale/fy/LC_MESSAGES/*
%lang(fy) %{_datadir}/locale/fy/entry.desktop
%endif

%files Irish
%lang(ga) %{_datadir}/locale/ga/LC_MESSAGES/*
%lang(ga) %{_datadir}/locale/ga/LC_SCRIPTS/
%lang(ga) %{_datadir}/locale/ga/entry.desktop
%lang(ga) %{_kde4_appsdir}/khangman/ga.txt
%lang(ga) %{_kde4_appsdir}/ktuberling/sounds/ga*
%lang(ga) %{_kde4_appsdir}/kvtml/ga/

%files Galician
%lang(gl) %{_datadir}/locale/gl/LC_MESSAGES/*
%lang(gl) %{_datadir}/locale/gl/entry.desktop
%lang(gl) %{_kde4_appsdir}/khangman/gl.txt
%lang(gl) %{_kde4_appsdir}/kvtml/gl/
%lang(gl) %{_kde4_appsdir}/ktuberling/sounds/gl.soundtheme
%lang(gl) %{_kde4_appsdir}/ktuberling/sounds/gl/
%lang(gl) %{_kde4_docdir}/HTML/gl/*
%lang(gl) %{_mandir}/gl/*/*

%files Hebrew
%lang(he) %{_datadir}/locale/he/LC_MESSAGES/*
%lang(he) %{_datadir}/locale/he/entry.desktop
%lang(he) %{_kde4_appsdir}/klettres/he/
%lang(he) %{_kde4_docdir}/HTML/he/*

%files Hindi
%lang(hi) %{_datadir}/locale/hi/LC_MESSAGES/*
%lang(hi) %{_datadir}/locale/hi/entry.desktop

%if %{buildall}
%files Chhattisgarhi
%lang(hne) %{_datadir}/locale/hne/LC_MESSAGES/*
%lang(hne) %{_datadir}/locale/hne/entry.desktop
%endif

%files Croatian
%lang(hr) %{_datadir}/locale/hr/LC_MESSAGES/*
%lang(hr) %{_datadir}/locale/hr/entry.desktop
%lang(hr) %{_datadir}/locale/hr/LC_SCRIPTS

%files Hungarian
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/*
%lang(hu) %{_datadir}/locale/hu/entry.desktop
%lang(hu) %{_kde4_appsdir}/autocorrect/hu.xml
%lang(hu) %{_kde4_appsdir}/kanagram/hu.txt
%lang(hu) %{_kde4_appsdir}/khangman/hu.txt
%lang(hu) %{_kde4_appsdir}/kvtml/hu/
%lang(hu) %{_kde4_appsdir}/klettres/hu/
%lang(hu) %{_kde4_docdir}/HTML/hu/*

%files Interlingua 
%lang(ia) %{_datadir}/locale/ia/LC_MESSAGES/*
%lang(ia) %{_datadir}/locale/ia/entry.desktop

%if %{buildall}
%files Indonesian
%lang(id) %{_datadir}/locale/id/LC_MESSAGES/*
%lang(id) %{_datadir}/locale/id/entry.desktop
%endif

%files Icelandic
%lang(is) %{_datadir}/locale/is/LC_MESSAGES/*
%lang(is) %{_datadir}/locale/is/entry.desktop

%files Italian
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/*
%lang(it) %{_datadir}/locale/it/entry.desktop
%lang(it) %{_kde4_appsdir}/autocorrect/it_IT.xml
%lang(it) %{_kde4_appsdir}/ktuberling/sounds/it*
%lang(it) %{_kde4_appsdir}/klettres/it/
%lang(it) %{_kde4_appsdir}/kvtml/it/
%lang(it) %{_kde4_docdir}/HTML/it/*
%lang(it) %{_kde4_appsdir}/step/objinfo/l10n/it/
%lang(it) %{_mandir}/it/*/*

%files Japanese
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/*
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/
%lang(ja) %{_datadir}/locale/ja/entry.desktop
%lang(ja) %{_kde4_docdir}/HTML/ja/*

%if %{buildall}
%files Kannada
%lang(kn) %{_datadir}/locale/kn/LC_MESSAGES/*
%lang(kn) %{_datadir}/locale/kn/entry.desktop
%endif

%if %{buildall}
%files Kashubian
%lang(csb) %{_datadir}/locale/csb/LC_MESSAGES/*
%lang(csb) %{_datadir}/locale/csb/entry.desktop
%endif

%files Kazakh
%lang(kk) %{_datadir}/locale/kk/LC_MESSAGES/*
%lang(kk) %{_datadir}/locale/kk/entry.desktop

%files Khmer
%lang(km) %{_datadir}/locale/km/LC_MESSAGES/*
%lang(km) %{_datadir}/locale/km/entry.desktop

%files Korean
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/*
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/
%lang(ko) %{_datadir}/locale/ko/entry.desktop
%lang(ko) %{_kde4_docdir}/HTML/ko/*

%if %{buildall}
%files Kurdish
%lang(ku) %{_datadir}/locale/ku/LC_MESSAGES/*
%lang(ku) %{_datadir}/locale/ku/entry.desktop
%endif

%if %{buildall}
%files Lao
%lang(lo) %{_datadir}/locale/lo/LC_MESSAGES/*
%lang(lo) %{_datadir}/locale/lo/entry.desktop
%endif

%files Lithuanian
%lang(lt) %{_datadir}/locale/lt/LC_MESSAGES/*
%lang(lt) %{_datadir}/locale/lt/LC_SCRIPTS/
%lang(lt) %{_datadir}/locale/lt/entry.desktop
%lang(lt) %{_kde4_appsdir}/klettres/lt*
%lang(lt) %{_kde4_appsdir}/ktuberling/sounds/lt*
%lang(lt) %{_kde4_docdir}/HTML/lt/*
%lang(lt) %{_mandir}/lt/*/*

%files LowSaxon
%lang(nds) %{_datadir}/locale/nds/LC_MESSAGES/*
%lang(nds) %{_datadir}/locale/nds/entry.desktop
%lang(nds) %{_kde4_appsdir}/autocorrect/nds.xml
%lang(nds) %{_kde4_appsdir}/klettres/nds/
%lang(nds) %{_kde4_appsdir}/khangman/nds.txt
%lang(nds) %{_kde4_appsdir}/kvtml/nds/
%lang(nds) %{_kde4_appsdir}/ktuberling/sounds/nds*
%lang(nds) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.nds.xml
%lang(nds) %{_kde4_appsdir}/kturtle/examples/nds
%lang(nds) %{_kde4_docdir}/HTML/nds/*

%files Latvian
%lang(lv) %{_datadir}/locale/lv/LC_MESSAGES/*
%lang(lv) %{_datadir}/locale/lv/entry.desktop
%lang(lv) %{_datadir}/locale/lv/LC_SCRIPTS

%if %{buildall}
%files Maori
%lang(mi) %{_datadir}/locale/mi/LC_MESSAGES/*
%lang(mi) %{_datadir}/locale/mi/entry.desktop
%endif

%if %{buildall}
%files Macedonian
%lang(mk) %{_datadir}/locale/mk/LC_MESSAGES/*
%lang(mk) %{_datadir}/locale/mk/entry.desktop
%endif

%if %{buildall}
%files Maithili
%lang(mai) %{_datadir}/locale/mai/LC_MESSAGES/*
%lang(mai) %{_datadir}/locale/mai/entry.desktop
%endif

%files Marathi
%lang(mr) %{_datadir}/locale/mr/LC_MESSAGES/*
%lang(mr) %{_datadir}/locale/mr/entry.desktop

%if %{buildall}
%files Malayalam
%lang(ml) %{_datadir}/locale/ml/LC_MESSAGES/*
%lang(ml) %{_datadir}/locale/ml/LC_SCRIPTS/
%lang(ml) %{_datadir}/locale/ml/entry.desktop
%lang(ml) %{_kde4_appsdir}/klettres/ml/
%endif

%if %{buildall}
%files Maltese
%lang(mt) %{_datadir}/locale/mt/LC_MESSAGES/*
%lang(mt) %{_datadir}/locale/mt/entry.desktop
%endif

%if %{buildall}
%files Nepali
%lang(ne) %{_datadir}/locale/ne/LC_MESSAGES/*
%lang(ne) %{_datadir}/locale/ne/entry.desktop
%endif

%files Dutch
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*
%lang(nl) %{_datadir}/locale/nl/LC_SCRIPTS/
%lang(nl) %{_datadir}/locale/nl/entry.desktop
%lang(nl) %{_kde4_appsdir}/ktuberling/sounds/nl*
%lang(nl) %{_kde4_appsdir}/klettres/nl/
%lang(nl) %{_kde4_appsdir}/kvtml/nl/
%lang(nl) %{_kde4_docdir}/HTML/nl/*
%lang(nl) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.nl.xml
%lang(nl) %{_kde4_appsdir}/kturtle/data/logokeywords.nl.xml
%lang(nl) %{_kde4_appsdir}/kturtle/examples/nl/*.logo
%lang(nl) %{_mandir}/nl/*/*

%if %{buildall}
%files NorthernSami
%lang(se) %{_datadir}/locale/se/LC_MESSAGES/*
%lang(se) %{_datadir}/locale/se/entry.desktop
%endif

%files Sinhala
%lang(si) %{_datadir}/locale/si/LC_MESSAGES/*
%lang(si) %{_datadir}/locale/si/entry.desktop

%files Norwegian
%lang(nb) %{_datadir}/locale/nb/LC_MESSAGES/*
%lang(nb) %{_datadir}/locale/nb/LC_SCRIPTS/
%lang(nb) %{_datadir}/locale/nb/entry.desktop
%lang(nb) %{_kde4_appsdir}/khangman/nb.txt
%lang(nb) %{_kde4_appsdir}/kvtml/nb/
%lang(nb) %{_kde4_docdir}/HTML/nb/*
%lang(nb) %{_kde4_appsdir}/klettres/nb/
%lang(nb) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.nb.xml
%lang(nb) %{_kde4_appsdir}/kturtle/data/logokeywords.nb.xml
%lang(nb) %{_kde4_appsdir}/kturtle/examples/nb/*.logo
%lang(nb) %{_mandir}/nb/*/*

%files Norwegian-Nynorsk
%lang(nn) %{_datadir}/locale/nn/LC_MESSAGES/*
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/
%lang(nn) %{_datadir}/locale/nn/entry.desktop
%lang(nn) %{_kde4_appsdir}/khangman/nn.txt
%lang(nn) %{_kde4_appsdir}/kvtml/nn/
%lang(nn) %{_kde4_docdir}/HTML/nn/*

%if %{buildall}
%files Occitan
%lang(oc) %{_datadir}/locale/oc/LC_MESSAGES/*
%lang(oc) %{_datadir}/locale/oc/entry.desktop
%endif

%files Punjabi
%lang(pa) %{_datadir}/locale/pa/LC_MESSAGES/*
%lang(pa) %{_datadir}/locale/pa/entry.desktop
%lang(pa) %{_kde4_appsdir}/kvtml/pa/

%files Polish
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*
%lang(pl) %{_datadir}/locale/pl/LC_SCRIPTS/
%lang(pl) %{_datadir}/locale/pl/entry.desktop
%lang(pl) %{_kde4_appsdir}/khangman/pl.txt
%lang(pl) %{_kde4_appsdir}/kvtml/pl/
%lang(pl) %{_kde4_docdir}/HTML/pl/*
%lang(pl) %{_mandir}/pl/*/*

%files Portuguese
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/*
%lang(pt) %{_datadir}/locale/pt/entry.desktop
%lang(pt) %{_kde4_appsdir}/khangman/pt.txt
%lang(pt) %{_kde4_appsdir}/ktuberling/sounds/pt*
%lang(pt) %{_kde4_appsdir}/kvtml/pt/
%lang(pt) %{_kde4_docdir}/HTML/pt/*
%lang(pt) %{_mandir}/pt/*/*

%files Brazil
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*
%lang(pt_BR) %{_datadir}/locale/pt_BR/entry.desktop
%lang(pt_BR) %{_kde4_appsdir}/khangman/pt_BR.txt
%lang(pt_BR) %{_kde4_appsdir}/klettres/pt_BR/*
%lang(pt_BR) %{_kde4_appsdir}/kvtml/pt_BR/
%lang(pt_BR) %{_kde4_docdir}/HTML/pt_BR/*
%lang(pt_BR) %{_mandir}/pt_BR/*/*

%files Romanian
%lang(ro) %{_datadir}/locale/ro/LC_MESSAGES/*
%lang(ro) %{_datadir}/locale/ro/entry.desktop
%lang(ro) %{_kde4_appsdir}/kvtml/ro/
%lang(ro) %{_kde4_appsdir}/ktuberling/sounds/ro*
%lang(ro) %{_kde4_docdir}/HTML/ro/*

%files Russian
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*
%lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS/
%lang(ru) %{_datadir}/locale/ru/entry.desktop
%lang(ru) %{_kde4_appsdir}/autocorrect/ru_RU.xml
%lang(ru) %{_kde4_appsdir}/kvtml/ru/
%lang(ru) %{_kde4_appsdir}/klettres/ru/
%lang(ru) %{_kde4_appsdir}/ktuberling/sounds/ru*
%lang(ru) %{_kde4_docdir}/HTML/ru/*
%lang(ru) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.ru.xml
#lang(ru) %{_kde4_appsdir}/kturtle/data/logokeywords.ru.xml
#lang(ru) %{_kde4_appsdir}/kturtle/examples/ru/*.logo
%lang(ru) %{_mandir}/ru/*/*

%files Slovak
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/*
%lang(sk) %{_datadir}/locale/sk/entry.desktop
#lang(sk) %{_kde4_docdir}/HTML/sk/*
#%lang(sk) %{_kde4_appsdir}/ktuberling/sounds/sk*
#%lang(sk) %{_kde4_appsdir}/klettres/sk/

%files Slovenian
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/*
%lang(sl) %{_datadir}/locale/sl/entry.desktop
#lang(sl) %{_kde4_appsdir}/ktuberling/sounds/sl*
#lang(sl) %{_kde4_appsdir}/khangman/sl.txt
#lang(sl) %{_kde4_appsdir}/kvtml/sl/
%lang(sl) %{_kde4_docdir}/HTML/sl/*

%files Serbian
%lang(sr) %{_datadir}/locale/sr*/LC_MESSAGES/*
%lang(sr) %{_datadir}/locale/sr*/LC_SCRIPTS/*
%lang(sr) %{_datadir}/locale/sr*/entry.desktop
%lang(sr) %{_kde4_appsdir}/ktuberling/sounds/sr*
%lang(sr) %{_kde4_docdir}/HTML/sr*/*
%lang(sr) %{_kde4_iconsdir}/*/*/*/*/sr/
%lang(sr) %{_kde4_iconsdir}/*/*/*/*/sr@latin/
%lang(sr) %{_kde4_iconsdir}/*/*/*/*/sr@ijekavian/
%lang(sr) %{_kde4_iconsdir}/*/*/*/*/sr@ijekavianlatin/
%lang(sr) %{_kde4_appsdir}/desktoptheme/*/widgets/l10n/sr
%lang(sr) %{_kde4_appsdir}/desktoptheme/*/widgets/l10n/sr@latin
%lang(sr) %{_kde4_appsdir}/desktoptheme/*/widgets/l10n/sr@ijekavian
%lang(sr) %{_kde4_appsdir}/desktoptheme/*/widgets/l10n/sr@ijekavianlatin
%lang(sr) %{_kde4_appsdir}/desktoptheme/default/icons/l10n/sr*
%lang(sr) %{_kde4_appsdir}/khangman/sr@latin.txt
%lang(sr) %{_kde4_appsdir}/kvtml/sr*/
%lang(sr) %{_mandir}/sr*/*/*

%files Swedish
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/*
%lang(sv) %{_datadir}/locale/sv/entry.desktop
%lang(sv) %{_datadir}/locale/sv/LC_SCRIPTS/
%lang(sv) %{_kde4_appsdir}/ktuberling/sounds/sv*
%lang(sv) %{_kde4_appsdir}/khangman/sv.txt
%lang(sv) %{_kde4_appsdir}/kvtml/sv/
%lang(sv) %{_kde4_docdir}/HTML/sv/*
%lang(sv) %{_mandir}/sv/*/*

%if %{buildall}
%files Tamil
%lang(ta) %{_datadir}/locale/ta/LC_MESSAGES/*
%lang(ta) %{_datadir}/locale/ta/entry.desktop
%endif

%files Tajik
%lang(tg) %{_datadir}/locale/tg/LC_MESSAGES/*
%lang(tg) %{_datadir}/locale/tg/entry.desktop
%lang(tg) %{_kde4_appsdir}/kvtml/tg/
%lang(tg) %{_kde4_appsdir}/khangman/tg.txt

%files Thai
%lang(th) %{_datadir}/locale/th/LC_MESSAGES/*
%lang(th) %{_datadir}/locale/th/charset
%lang(th) %{_datadir}/locale/th/entry.desktop

%files Turkish
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/*
%lang(tr) %{_datadir}/locale/tr/entry.desktop
%lang(tr) %{_kde4_appsdir}/khangman/tr.txt
%lang(tr) %{_kde4_appsdir}/kvtml/tr/
%lang(tr) %{_kde4_docdir}/HTML/tr/*
%lang(tr) %{_mandir}/tr/*/*

%files Uyghur
%lang(ug) %{_datadir}/locale/ug/LC_MESSAGES/*
%lang(ug) %{_datadir}/locale/ug/entry.desktop

%files Ukrainian
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/*
%lang(uk) %{_datadir}/locale/uk/LC_SCRIPTS/
%lang(uk) %{_datadir}/locale/uk/entry.desktop
%lang(uk) %{_kde4_appsdir}/autocorrect/uk*.xml
%lang(uk) %{_kde4_appsdir}/ktuberling/sounds/uk*
%lang(uk) %{_kde4_appsdir}/step/objinfo/l10n/uk/
%lang(uk) %{_kde4_appsdir}/kvtml/uk/
%lang(uk) %{_kde4_appsdir}/klettres/uk/
%lang(uk) %{_kde4_docdir}/HTML/uk/*
%lang(uk) %{_mandir}/uk/*/*

%if %{buildall}
%files Venda
%lang(ven) %{_datadir}/locale/ven/LC_MESSAGES/*
%lang(ven) %{_datadir}/locale/ven/entry.desktop
%endif

%files Vietnamese
%lang(vi) %{_datadir}/locale/vi/LC_MESSAGES/*
%lang(vi) %{_datadir}/locale/vi/entry.desktop

%files Walloon
%lang(wa) %{_datadir}/locale/wa/LC_MESSAGES/*
%lang(wa) %{_datadir}/locale/wa/entry.desktop
%lang(wa) %{_kde4_appsdir}/ktuberling/sounds/wa*
%lang(wa) %{_kde4_docdir}/HTML/wa/*

%if %{buildall}
%files Xhosa
%lang(xh) %{_datadir}/locale/xh/LC_MESSAGES/*
%lang(xh) %{_datadir}/locale/xh/entry.desktop
%endif

%files Chinese
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/*
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_SCRIPTS/
%lang(zh_CN) %{_datadir}/locale/zh_CN/charset
%lang(zh_CN) %{_datadir}/locale/zh_CN/entry.desktop
%lang(zh_CN) %{_kde4_appsdir}/kvtml/zh_CN/
%lang(zh_CN) %{_kde4_appsdir}/step/objinfo/l10n/zh_CN/
%lang(zh_CN) %{_kde4_docdir}/HTML/zh_CN/*

%files Chinese-Traditional
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/*
%lang(zh_TW) %{_datadir}/locale/zh_TW/entry.desktop
%lang(zh_TW) %{_kde4_docdir}/HTML/zh_TW/*


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.10.5-2
- Mass rebuild 2013-12-27

* Sun Jun 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4
- +%%lang(mr)
- fix/trim %%changelog

* Fri May 17 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.10.3-3
- completely blacklist extragear-* for kde-l10n-sr (#963547)

* Thu May 16 2013 Than Ngo <than@redhat.com> - 4.10.3-2
- bz#963547, fix file conflicts

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Tue Apr 02 2013 Than Ngo <than@redhat.com> - 4.10.2-1
- 4.10.2

* Mon Mar 04 2013 Than Ngo <than@redhat.com> - 4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Than Ngo <than@redhat.com> - 4.10.0-1
- 4.10.0

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-1
- 4.9.97

* Sat Dec 29 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.95-1
- 4.9.95

* Sat Dec 29 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.5-1
- 4.9.5

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Tue Nov 06 2012 Than Ngo <than@redhat.com> - 4.9.3-1
- 4.9.3

* Mon Oct 08 2012 Than Ngo <than@redhat.com> - 4.9.2-2
- fix url

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-1
- 4.9.2

* Tue Sep 04 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Sat Jul 28 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.9.0-2
- don't Obsolete readded Hindi

* Fri Jul 27 2012 Lukáš Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Tue Jul 17 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- kde-l10n-4.8.97
- .spec cleanup

* Wed Jun 27 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.95-1
- 4.8.95

* Tue Jun 26 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-1
- 4.8.90

* Mon Jun 04 2012 Than Ngo <than@redhat.com> - 4.8.4-1
- 4.8.4

* Tue May 1 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.2-1
- 4.8.2

* Thu Mar 08 2012 Radek Novacek <rnovacek@redhat.com> 4.8.1-2
- Respin kde-l10n-sr (subvariants was missing)
- Add sr* subvariants to sr subpackage

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> 4.8.1-1
- 4.8.1
- readd id, he and ug languages

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-1
- 4.8.0

* Thu Jan 05 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.97-1
- 4.7.97

* Sat Dec 24 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.7.95-2
- Obsolete Serbian (not part of 4.7.95)
- upstream patch to fix sv build (regenerate kwrite docbooks)
- upstream patch to fix es install (install only the files that exist)

* Wed Dec 21 2011 Than Ngo <than@redhat.com> - 4.7.95-1
- 4.8rc1

* Mon Oct 31 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Wed Oct 05 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Fri Sep 02 2011 Than Ngo <than@redhat.com> - 4.7.1-1
- 4.7.1

* Wed Jul 27 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.7.0-2
- Obsolete Gujarati, Hindi and Maithili (not part of 4.7.0)

* Tue Jul 26 2011 Than Ngo <than@redhat.com> - 4.7.0-1
- 4.7.0

* Mon Jul 11 2011 Jaroslav Reznik <jreznik@redhat.com> - 4.6.95-1
- 4.6.95 (rc2)
- build Bosnian

* Mon Jun 27 2011 Than Ngo <than@redhat.com> - 4.6.90-1
- 4.6.90 (rc1)

* Mon Jun 06 2011 Than Ngo <than@redhat.com> - 4.6.4-1
- 4.6.4

* Wed May 18 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.6.3-2
- blacklist kdepim-runtime translations when building for kdepim 4.6

* Thu Apr 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.6.3-1
- 4.6.3

* Mon Apr 11 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.6.2-2
- fixup Release tag

* Wed Apr 06 2011 Than Ngo <than@redhat.com> - 4.6.2-1.1
- 4.6.2

* Tue Mar 22 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1.1
- Conflicts: kde-i18n < 1:3.5.10-14

* Mon Feb 28 2011 Than Ngo <than@redhat.com> - 4.6.1-1
- 4.6.1

* Thu Feb 24 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-3.2
- fix kdepim Conflicts

* Thu Feb 10 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-3.1
- (re)include kdepim-4.4 translations (f15)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-2
- Conflicts: kde-i18n < 1:3.5.10-13 (when klickety moved, #657225)

* Fri Jan 21 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.0-1
- 4.6.0
- obsolete Esperanto, Frisian and Malayalam (not a part of 4.6.0)
- Maithili is available again

* Fri Jan 07 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-1
- 4.5.95 (4.6rc2)

* Sun Dec 26 2010 Rex Dieter <rdieter@fedoraproject.org> 4.5.90-1
- 4.5.90

* Tue Nov 23 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.80-2
- respun et and sr tarballs
- update file lists

* Mon Nov 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.80-1
- update to 4.5.80 (4.6 beta 1)

* Sun Oct 31 2010 Than Ngo <than@redhat.com> - 4.5.3-1
- 4.5.3

* Tue Oct 05 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-1
- 4.5.2
- fix Source urls
- include kdepim-4.4 translations only for < f15

* Fri Sep 03 2010 Than Ngo <than@redhat.com> - 4.5.1-5
- respin kdepim 4.4.5 translations

* Wed Sep 01 2010 Than Ngo <than@redhat.com> - 4.5.1-4
- bz#627898, add missing kdepim 4.4.5 translations

* Tue Aug 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-3
- respun -es,-ru tarballs

* Mon Aug 30 2010 Than Ngo <than@redhat.com> - 4.5.1-2
- workaround for breakage in l10n, ru/es

* Mon Aug 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-1
- 4.5.1

* Wed Aug 11 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.0-2
- Obsolete Kashubian, Macedonian, Maithili, Sinhala, Tajik (not part of 4.5.0)

* Fri Aug 06 2010 Than Ngo <than@redhat.com> - 4.5.0-1
- 4.5.0
- add translations for kdepim-4.4

* Sun Jul 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.95-1
- 4.5 RC3 (4.4.95)

* Wed Jul 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.92-1
- 4.5 RC2 (4.4.92)

* Fri May 28 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.80-1
- KDE SC 4.5 Beta 1 (4.4.80)

* Fri Apr 30 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.3-1
- 4.4.3

* Mon Mar 29 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.2-1
- 4.4.2
- add Indonesian

* Tue Mar 02 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.1-2
- do not own Serbian LC_MESSAGES

* Mon Mar 01 2010 Than Ngo <than@redhat.com> - 4.4.1-1
- 4.4.1

* Wed Feb 10 2010 Than Ngo <than@redhat.com> - 4.4.0-1
- 4.4.0
- Obsoletes: kde-l10n-Bengali-India (not part of 4.4.0)
- Obsoletes: kde-l10n-Chhattisgarhi (not part of 4.4.0)
- Obsoletes: kde-l10n-Marathi (not part of 4.4.0)
- Obsoletes: kde-l10n-Thai (not part of 4.4.0)

* Fri Feb 05 2010 Rex Dieter <rdieter@fedoraproject.org> 4.3.98-2
- Obsoletes: kde-l10n-Kurdish (#555881)

* Wed Feb 03 2010 Than Ngo <than@redhat.com> - 4.3.98-1
- 4.3.98 (KDE-4.4 rc3)
- add Catalan-Valencian and Sinhala

* Tue Jan 26 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.95-1
- 4.3.95 (4.4rc2)

* Fri Jan 15 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.90-3
- don't ship remaining kpilot translations

* Thu Jan 14 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.90-2
- skip translations of kcm_proxy docs, several don't build (at least ca, da, es)
- skip Danish translation of gwenview docs which doesn't build (rev 1065269)
- skip Estonian translation of kturtle docs which doesn't build (rev 1065298)
- make the skipping magic also work for sr@latin

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-1
- 4.3.90 (4.4rc1)

* Fri Nov 13 2009 Than Ngo <than@redhat.com> - 4.3.3-2
- rhel cleanup, remove Fedora<=9 conditionals

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Oct 05 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Sat Oct 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.1-3
- main virtual subpkg

* Sat Sep 05 2009 Than Ngo <than@redhat.com> - 4.3.1-2
- add missing Croatian localization

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Tue Jul 14 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Tue Jul  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.2.95-2
- fix duplicate directory ownership (/usr/share/locale/*/LC_MESSAGES)

* Tue Jun 30 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Tue May 19 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.85-1
- KDE 4.3 beta 1

* Tue Mar 31 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-1
- KDE 4.2.2

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 4.2.1-1
- 4.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Than Ngo <than@redhat.com> - 4.2.0-2
- enable he

* Thu Jan 22 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Sat Jan 10 2009 Than Ngo <than@redhat.com> - 4.1.96-2
- remove debug

* Wed Jan 07 2009 Than Ngo <than@redhat.com> - 4.1.96-1
- 4.2rc1

* Fri Dec 12 2008 Than Ngo <than@redhat.com> - 4.1.85-1
- 4.2beta2

* Fri Nov 21 2008 Than Ngo <than@redhat.com> 4.1.80-1
- 4.2 beta1

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- 4.1.2
- reenable Kurdish, Lithuanian, Malayalam 

* Wed Sep 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.1-2
- reenable Frisian and Kazakh

* Fri Aug 29 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Tue Jul 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-2
- get rid of kdepim documentation from kdenetwork

* Sun Jul 27 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-1.2
- file conflict between kde-l10n and libkdcraw (#456797)

* Sat Jul 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-1.1
- on F9, remove translations for kdepim apps we don't ship (#456745)

* Wed Jul 23 2008 Than Ngo <than@redhat.com> 4.1.0-1
- 4.1.0

* Tue Jul 22 2008 Than Ngo <than@redhat.com> 4.0.98-1
- 4.0.98 (4.1rc1)

* Sat Jun 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.83-2
- disable Serbian for now, it's broken
- fix file list for Ukranian

* Thu Jun 19 2008 Than Ngo <than@redhat.com> 4.0.83-1
- 4.0.83 (beta2)

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta 1

* Fri Apr 18 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-4
- remove documentation for apps which are not part of KDE 4.0

* Thu Apr 17 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-3
- disable kdewebdev documentation correctly

* Thu Apr 17 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- build documentation (#441537)
- mark Norvegian Bokmal translations with %%lang(nb) rather than %%lang(no)

* Tue Apr 01 2008 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3

* Mon Mar 03 2008 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2

* Thu Feb 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-3
- don't ship kdewebdev translations (we don't ship kdewebdev 4 yet)

* Thu Feb 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-2
- fix Danish not to include the data files for all languages
- include ktuberling sounds in the respective languages
- include kvtml (kanagram) translations in Czech

* Thu Jan 31 2008 Than Ngo <than@redhat.com> 4.0.1-1
- 4.0.1

* Fri Jan 18 2008 Lukas Tinkl <ltinkl@redhat.com> 4.0.0-4
- update languages for to the official KDE 4.0.0 list
- correct BR to kdelibs4-devel

* Fri Jan 18 2008 Lukas Tinkl <ltinkl@redhat.com> 4.0.0-2
- update languages for to the official KDE 4.0.0 list

* Wed Jan 09 2008 Than Ngo <than@redhat.com> 4.0.0-1
- 4.0.0

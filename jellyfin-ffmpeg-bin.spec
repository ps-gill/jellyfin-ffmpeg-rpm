Name:           jellyfin-ffmpeg-bin
Summary:        FFmpeg for Jellyfin
Version:        6.0
Release:        6
License:        GPL3
URL:            https://github.com/jellyfin/jellyfin-ffmpeg
Conflicts:      jellyfin-ffmpeg
Requires:       glibc >= 2.23
Recommends:     intel-media-driver
Recommends:     intel-mediasdk
Recommends:     oneVPL-intel-gpu
Recommends:     intel-compute-runtime
Recommends:     libva-intel-driver
Recommends:     mesa-va-drivers
Recommends:     rocm-opencl
Recommends:     mesa-vulkan-drivers

%ifarch %{ix86} x86_64
Source0: https://repo.jellyfin.org/releases/ffmpeg/%{version}-%{release}/jellyfin-ffmpeg_%{version}-%{release}_portable_linux64-gpl.tar.xz
%endif

%ifarch aarch64
Source0: https://repo.jellyfin.org/releases/ffmpeg/%{version}-%{release}/jellyfin-ffmpeg_%{version}-%{release}_portable_linuxarm64-gpl.tar.xz
%endif

Source1: https://raw.githubusercontent.com/jellyfin/jellyfin-ffmpeg/v%{version}-%{release}/LICENSE.md
Source2: https://raw.githubusercontent.com/jellyfin/jellyfin-ffmpeg/v%{version}-%{release}/Changelog
Source3: https://raw.githubusercontent.com/jellyfin/jellyfin-ffmpeg/v%{version}-%{release}/README.md

%description
%{summary}.

%prep
%setup -c
cp %{SOURCE1} %{_builddir}/%{name}-%{version}/
cp %{SOURCE2} %{_builddir}/%{name}-%{version}/
cp %{SOURCE3} %{_builddir}/%{name}-%{version}/

%install
install -Dm 755 ffmpeg %{buildroot}%{_libdir}/jellyfin-ffmpeg/ffmpeg
install -Dm 755 ffprobe %{buildroot}%{_libdir}/jellyfin-ffmpeg/ffprobe

%files
%{_libdir}/jellyfin-ffmpeg/ffmpeg
%{_libdir}/jellyfin-ffmpeg/ffprobe
%license LICENSE.md
%doc README.md Changelog

%changelog
%autochangelog

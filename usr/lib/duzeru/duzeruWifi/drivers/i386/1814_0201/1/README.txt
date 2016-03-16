Card: A-Link #[WL54H] -- [link here|List#WL54H]

    * Chipset: RaLink? RT2500 (rev 01)
    * pciid: 1814:0201 (rev 01)
    * Driver: Ndiswrapper 0.9 and RT2500 thingies (.inf and .sys for WinXP) from [ftp://ftp.a-link.com/wl54h/WL54driver2.2.6.0.zip]
    * Other: Gentoo 2.6.8 and working well. Easy to get running.
    * Other: pciid: 1814:0302 is rt2561 chip and it wont work with these drivers (lspci & lspci -n) not even if loaded rt61.inf/.sys Check "Card: Linksys #[WMP54G v4.1]" on this page how to compile driver. 

Card: Averatec 3200/6100 Series Laptop

    * Chipset: RaLink? RT2500
    * pciid: 1814:0201 (rev 01)
    * Driver: ftp://ftp.a-link.com/wl54h/WL54driver2.2.6.0.zip
    * Other: Seems to work great so far. No hic-cups at all. I tried the official source RT2500 driver before this, which is horrible. Ndiswrapper is definitely the way to go for this chipset. Note that not all Averatecs have the RT2500, some have the broadcom 54G: [If this is the case see entry for "Acer Aspire 1511" above and get the HP driver. The Win2k version worked for me on Ubuntu 5.10]. Also note that if you try to use the stock RT2500 drivers, or the stock Averatec RT2500 drivers with this card, you will get kernel panics, death and destruction. But if you use the A-Link drivers above (which are really just older, less complicated RT2500 drivers) for Windows 2000, you will have no problems, and much more reliability! NOTE: DO NOT USE WINXP DRIVERS, USE WIN2K FOR MORE STABILITY. ndiswrapper version 1.0rc1 works well with latest driver from ralinktech.com (tested with driver version 09/09/2004, 2.02.08.0000). 

Card: [Asus] A8V Deluxe Wireless Edition (Cardname unknown)

    * Chipset: RaLink RT2500
    * pciid: 1814:0201 (rev 01)
    * Driver: Used the WinXP driver from the CD provided by ASUS. Works out of the box. Haven't tried WEP/WPA yet.
    * Other: ndiswrapper 0.12+1.0rc2-1, ubuntu kernel 2.6.10-5-k7 
    
Card: Atlantis-land PCMCIA A02-PCM-W54, 54mbps

    * Chipset: Ralink RT2500
    * pciid: 1814:0201 (rev 01)
    * Driver: [ftp://ftp.a-link.com/wl54h/WL54driver2.2.6.0.zip]
    * Other: I own Compaq Presario 907 EA Laptop, with installed Suse 9.1 Personal, i must upgrade it on Professional before i can install "ndiswrapper 0.12", and also i must uninstall old version of "ndiswwrapper 0.8" which was installed in 9.1 Personal, i followed relative instruction of distributions installation. 
    
Card: Atlantis-land PCI A02-PCI-W54, 54mbps

    * Chipset: Ralink RT2500 (RT2525)
    * pciid: 1814:0201
    * Driver: [ftp://ftp.a-link.com/wl54h/WL54driver2.2.6.0.zip] (WinXP)
    * Other: I am running Debian unstable, so the first try has been to install the debian packake for ndiswrapper, but it worked not very well: I had problems setting essid when starting the interface, and after starting it stopped randomly losing the association with the access point several times. Moreover I got a lot of Tx excessive retries and Invalid misc. So I tried the last nightly tar ball (as of 12-22-2004) and now everything seems to work. 

Card: Belkin 54g Wireless Network Card F5D7000uk

    * Chipset: Ralink RT2500 802.11 Cardbus Reference Card (rev 01)
    * pciid: 1814:0201
    * Driver: Ndiswrapper 1.1 and Rt2500.INF file from ftp://ftp.a-link.com/wl54h/WL54driver2.2.6.0.zip
    * Other: Debian stable Sarge (2.4.27-2-386) works a treat. I followed the "InstallDebianSarge" instructions which were great. In the end however, I didn't need the "Install latest Ndiswrapper" section as version 1.1 comes already available. Also, needed unzip utility (apt-get install unzip). Cheers! 
    
Card: Belkin F5D7010 Wireless-G Notebook Adapter

    * Chipset: RaLink RT2500
    * pciid: 1814:0201 (rev 01)
    * Driver: ndiswrapper 0.11 and A-Link ftp://ftp.a-link.com/wl54h/WL54driver2.2.6.0.zip
    * Other: Debian sid/i386, kernel 2.6.7/9, Inspiron 2650. Tried the linux driver (v1.4.3.0) from http://www.ralinktech.com/ -- module loaded, interface created, but settings for iwconfig don't get committed. Tried to get NDIS driver off CD but couldn't locate/extract INF file. Finally tried NDIS driver for another card using RT2500 (the A-Link above), and (so far) it has worked wonderfully. 

Card: CNet CWC-854 Wireless-G PCMCIA Adapter

    * Chipset: RaLink RT2500
    * pciid: 1814:0201 (rev 01)
    * Driver: ftp://ftp.a-link.com/wl54h/WL54driver2.2.6.0.zip
    * Other: NdisWrapper 0.10 and Slackware 10.2 with custom 2.6.14 kernel
    * Other: Seems to work better in linux than in windows 

Card: CNet CWP-854 Wireless-G PCI Adapter

    * Chipset: RT2500
    * pciid: 1814:0201 (rev 01)
    * Driver: Windows 2000 drivers from installation CD, driver version 11/27/2003, 2.01.00.0000
    * Other: using NdisWrapper? version 1.0rc2, Debian unstable, Kernel 2.6.10
    * Other: I just tested this device with ndiswrapper and works great 

Card: Conceptronic C54RC Wireless 54Mbps PC Card (PCMCIA)

    * Chipset: RT2500
    * pciid: 1814:0201 (rev 01)
    * Driver: Windows XP drivers from installation CD, driver version 2.02.05.0000.
    * Other: Using NdisWrapper? 0.12rc-1, Debian unstable, Kernel 2.6.8.1.
    * Other: The latest RaLink? Linux driver (version 1.4.3.0), works ok, but quickly the system hangs.
    * Other: ndiswrapper + wpa_supplicant, Ubuntu 5.10. Win XP driver, driver (Conceptronic,12/15/2004, 3.00.01.0000) 

Card: Edimax EW-7128g

    * Chipset: RaLink? RT2500
    * pciid: 1814:0201 (rev 1)
    * Driver: Ndiswrapper 0.11; .inf and .sys for Win2K from ftp://ftp.a-link.com/wl54h/WL54driver2.2.6.0.zip
    * Other: Slackware 10.0. Hint: modify /etc/rc.d/rc.inet1 and replace instances of "eth" with "wlan"; also modify /etc/rc.d/rc.modules to load ndiswrapper. Running flawlessly for one day so far. Using WEP. 

Card: Foxconn-WLL-3350 PCI

    * Chipset: RALink RT2500
    * pciid: Unknown Device 1814:0201
    * Driver: NDISWrapper 1.2 and driver from ftp://ftp.a-link.com/wl54h/WL54driver2.2.6.0.zip
    * Other: New machine locked after modprobe with NDISWrapper 1.4; downgraded to 1.2 and it's happy. Had no luck with the open drivers available. 

Card: ROLINE RWA-54 W-LAN 54 PCI Adapter

    * Chipset: RaLink? RT2500 (rev 01)
    * pciid: 1814:0201 (rev 01)
    * Driver: Ndiswrapper 0.11 and RT2500 thingies (.inf and .sys for WinXP) from ftp://ftp.a-link.com/wl54h/WL54driver2.2.6.0.zip
    * Other: Debian (kernel 2.4.26) running (still working on the config, but card is running!). 


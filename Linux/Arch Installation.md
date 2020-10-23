# Arch Linux Installation Notes

## Connect to the Internet

* Use `ip link` to check the network interface.
* Use `ip link set <netowrk interface> up` to turn on the device.
* Scan the Wi-Fi using `iwlist`, like `iwlist wlan0 scan | grep ESSID`.
* Set the *ESSID* and *password* using `wpa_passphrase <ESSID> <password> > <filename.conf>`.
* Use `wpa_supplicant -c <filename.conf> -i <network interface> &` to connect to the internet at background.
* Use `dhcpcd &` to get a dynamic IP address.
* Use `ping baidu.com` to check the internet connection.

## Update the system clock

* Use `timedatectl set-ntp true` to ensure the system clock is accurate.
  
## Partition the disks

* Use `fdisk -l` to check the disk devices.
* Use `fdisk /dev/<disk name>` to enter *fdisk*.
* Enter `g` to create a new empty GPT partition table and `p` to print the current partition table.

Once the partitions have been created, each must be formatted with an appropriate **file system**.

* Use `mkfs.fat -F32 /dev/<device partition>` to set *EFI* partition format.
* Use `mkfs.ext4 /dev/<device partition>` to set *root* partition format.
* Use `mkswap /dev/<device partition>` and `swapon /dev/<device partition>` to set *swap* partition format.

## Configurate pacman

* Run `vim /etc/pacman.conf`.
* Enable `Color`.
* Run `vim /etc/pacman.d/mirrorlist` to edit the mirrors list.

## Mount the file systems

* Run `mount /dev/<root partition> /mnt`
* Run `mkdir /mnt/boot`
* Run `mount /dev/<EFI partition> /mnt/boot`

## Installation

* Run `pacstrap /mnt base linux linux-firmware`
  
## Configure the system

### Fstab

* Run `genfstab -U /mnt >> /mnt/etc/fstab`.

### Change root into the new system

* Run `arch-chroot /mnt`

### Set Time Zone

* Run `ln -sf /usr/share/zoneinfo/Aisa/Shanghai /etc/localtime`.
* Run `hwclock --systohc`

### Localization

* Edit `/etc/locale.gen` and uncomment `en_US.UTF-8 UTF-8` and other needed locales.
* Generate the locales by running: `locale-gen`.
* Create the locale.conf file, and set the LANG variable accordingly:
```
vim /etc/locale.conf
```
```
LANG=en_US.UTF-8
```

### Network configuration

* Create the hostname file:
```
# vim /etc/hostname
```
```
myhostname
```

* Add matching entries to hosts:
```
# vim /etc/hosts
```
```
127.0.0.1	localhost
::1 		localhost
127.0.1.1	myhostname.localdomain	myhostname
```

### Root password

* Set the root password:
```
# passwd
```

### Boot loader
Choose and install a Linux-capable boot loader. If you have an Intel or AMD CPU, enable microcode updates in addition.

```
pacman -S grub efibootmgr amd-ucode os-prober
```

```
# mkdir /boot/grub
# grub-mkconfig > /boot/grub/grub.cfg
# grub-install --target=x86_64-efi --efi-directory=/boot
```

### Install some tools

```
pacman -S vim git wpa_supplicant dhcpcd
```

### Reboot

```
# exit
# killall wpa_supplicant dhcpcd
# reboot
```

## Enter the system

### Install X Windows Server

```
$ sudo pacman -S xorg-server
$ sudo pacman -S xorg-apps
$ sudo pacman -S xorg-xinit
```

### Install Dispaly Manager

```
$ sudo pacman -S lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings
```

### Install dwm

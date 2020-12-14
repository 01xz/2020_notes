# Arch Linux Installation Notes

## 1. Connect to the Internet

* Use `ip link` to check the network interface.
* Use `ip link set <netowrk interface> up` to turn on the device.
* Scan the Wi-Fi using `iwlist`, like `iwlist wlan0 scan | grep ESSID`.
* Set the *ESSID* and *password* using `wpa_passphrase <ESSID> <password> > <filename.conf>`.
* Use `wpa_supplicant -c <filename.conf> -i <network interface> &` to connect to the internet at background.
* Use `dhcpcd &` to get a dynamic IP address.
* Use `ping baidu.com` to check the internet connection.

## 2. Update the system clock

* Use `timedatectl set-ntp true` to ensure the system clock is accurate.
  
## 3. Partition the disk

* Use `fdisk -l` to check the disk devices.
* Use `fdisk /dev/<disk name>` to enter *fdisk*.
* Enter `g` to create a new empty GPT partition table and `p` to print the current partition table.

Once the partitions have been created, each must be formatted with an appropriate **file system**.

* Use `mkfs.fat -F32 /dev/<efi partition>` to set *EFI* partition format.
* Use `mkfs.ext4 /dev/<root partition>` to set *root* partition format.
* Use `mkswap /dev/<swap partition>` and `swapon /dev/<swap partition>` to set *swap* partition format.

## 4. Configurate pacman

* Run `vim /etc/pacman.conf`.
* Enable `Color`.
* Run `vim /etc/pacman.d/mirrorlist` to edit the mirrors list.

## 5. Mount the file systems

* Run `mount /dev/<root partition> /mnt`
* Run `mkdir /mnt/boot`
* Run `mount /dev/<efi partition> /mnt/boot`

## 6. Installation

* Run `pacstrap /mnt base linux linux-firmware`
  
## 7. Configure the system

### Fstab

* Run `genfstab -U /mnt >> /mnt/etc/fstab`.

### Change root into the new system

* Run `arch-chroot /mnt`

### Install vim

* Run `pacman -S vim`

### Set Time Zone

* Run `ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`.
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
pacman -S git wpa_supplicant dhcpcd
```

## 8. Reboot

```
# exit
# killall wpa_supplicant dhcpcd
# reboot
```

## 9. Enter the system

### Install some necessary softwares

```
# pacman -S man base-devel
```

### Add a new user

* add a new user 
```
# useradd -m -G wheel <username>
# passwd <username>
```

* link nvim to vi or vim
```
# ln -s /usr/bin/nvim /usr/bin/vi
# ln -s /usr/bin/nvim /usr/bin/vim
```

* Run `visudo` and uncomment `%wheel ALL=(ALL) ALL`

* Exit root and login as new user

### Install X Windows Server

```
$ sudo pacman -S xorg-server xorg-xinit xorg-xrandr xorg-xsetroot nitrogen picom
```

### configure in VMWare

If you are using VMWare, try following commands to set right resolution

```
$ cvt 1920 1080 60
$ xrandr --newmode <Modeline>
$ xrandr --addmode Virtual-1 <name>
$ xrandr --output Virtual-1 --mode 1920x1080_60.00
```

### Prepare for install dwm

* install `picom` and `nitrogen`, 
* copy `/etc/X11/xinit/xinitrc` to `~/.xinitrc`
```
$ cp /etc/X11/xinit/xinitrc .xinitrc
```
* edit `.xinitrc`
```
# delete the last 5 lines
# add the following lines

picom -f &
exec dwm

```
* run `startx`

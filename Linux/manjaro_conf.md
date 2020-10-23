# manjaro configuration

## 1. set mirrorlist

```
$ sudo vi /etc/pacman.conf
```

add archlinuxcn repo

check at [mirrorlist-repo](https://github.com/archlinuxcn/mirrorlist-repo)

```
[archlinuxcn]
SigLevel = Never
Server = https://mirrors.aliyun.com/archlinuxcn/$arch
```

uncomment `Color`

update the mirrorlist

```
sudo pacman-mirrors -c China
```

## 2. update the system

```
sudo pacman -Syyu
```

## 3. install necessary apps

```
sudo pacman -S neovim git 
```

install Chinese input tools

```
$ sudo pacman -S fcitx-im fcitx-configtool fcitx-sunpinyin
```

create ~/.xprofile

```
vim ~/.xprofile
```

add

```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```

reboot the system

## 4. configurate zsh

change shell to zsh

```
chsh -s /usr/bin/zsh
```

install oh-my-zsh

```
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
```

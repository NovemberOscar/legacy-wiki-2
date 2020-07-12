# Configuring RPi

## OS

Raspbian Lite

## Headless SSH & WiFi setup

```text
sudo touch /Volumes/boot/ssh
sudo echo "\ncgroup_memory=1 cgroup_enable=memory" >> /Volumes/boot/cmdline.txt
sudo vim /Volumes/boot/wpa_supplicant.conf
```

```text
ctrl_interface=DIR=/var/run/wpa_supplicant
country=US
update_config=1
network={
    ssid="your_ssid"
    psk="your_pw"
    key_mgmt=WPA-PSK
}
```

### Copy ssh key

```text
ssh-copy-id pi@k3s-master.local
```

## sudo raspi-config

* Network Options - hostname
  * k3s-master, k3s-slave-01, k3s-slave-02, k3s-slave-03
* Localisation Options - TimeZone
  * Asia, Seoul
* Advanced Options - GPU Memory split
  * 16mb

## k3sup

[https://github.com/alexellis/k3sup](https://github.com/alexellis/k3sup)


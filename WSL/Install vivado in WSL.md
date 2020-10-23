# Install vivado in WSL

* Download installation file from [xilinx](https://www.xilinx.com/support/download.html).
* Open `VcXsrv` before running WSL in terminal.
* run:
    ```
    $ ./Xilinx_Unified_2020.1_0602_1208_Lin64.bin
    ```
    to install vivado.
* Open `.bashrc`
    ```
    $ sudo vim ~/.bashrc
    ```
* Add
    ```
    source /mnt/c/Users/liaml/Xilinx_wsl/Vivado/2020.1/settings64.sh
    ```
    at the end of `.bashrc`.
* Save the file `.bashrc` and restart the WSL.
* Now you can type `vivado` in terminal to open the software.

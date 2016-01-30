vim plugin install

curl -sS https://raw.githubusercontent.com/mkropat/vim-dwiw2015/master/bootstrap.sh | sh

# remember when you are on editing

1. green status bar means that you are on normal mode.
2. gray status bar means that you can edit feely. try INSERT key
3. in ex mode, try 'echo "hello world"'
4. ex mode, try 'help echo'
   if new window appears, try "Control+w h/j/k/l"
   to change widow size, try "Control+w +/-/=/</>"
   to (min/max)imize window, try "Control+w _/|"
   remember again, normal mode is green. edit mode is gray.
5. do you know global mark? 
   to set global mark, mA on normal mode
   to recall `A
   try close help window, split current window, mAZZ[C-w]S`A
6. how about tab?
   try 'tabe %'
   to open new tab and show file in current directory? 'Te'
   opened may tabs? try 'gtgtgtgtgtgtgt' when you are on green.
   try 'gTgTgTgTgT' and '1gt2gt3gt' also.
   and there are more commands.
   # Control+PgUp and Control+PgDn are optional. (they are precious shortcuts.)
7. to close Window or Tab? 
   ZZ [Control+w]c :clo :q :tabclo
8. 


## gvim setting.
1. install minimal x11 server
   sudo yum install xorg-x11-server-utils xauth xorg-x11-fonts-*
2. restart sshd and xhost
   #service ssh restart
   /etc/init.d/sshd restart
   xhost +
   you might need reboot
3. install your favorite programming font
   sudo yum install levien-inconsolata-fonts
4. customize your .gvimrc
   :set guifont=Inconsolata\ Medium:h11
   :hi Menu font=




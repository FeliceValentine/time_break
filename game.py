import sys, time, os
from os import system, name
from time import sleep 
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear") 

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.04)
        else:
            time.sleep(0.04)




def title_1():
    print('''
                                       *                               .::::
      *                                                               :::::
                                                                    .:::::                     :.
                  *                                                ::::::                       ::.
                                                                     :::::                       :::.
                             *                                        :::::.                      ::::
                                            *                          ::::::                    ::::
                     *                                               .:::::                   .:::::  
                                    *               *               ::::::                   ::::::
            *   ████████╗██╗███╗   ███╗███████╗        ██████╗ ██████╗:███████╗ █████╗ ██╗  ██╗:::::.
                ╚══██╔══╝██║████╗ ████║██╔════╝        ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝ ::::::
                   ██║   ██║██╔████╔██║█████╗          ██████╔╝██████╔╝█████╗  ███████║█████╔╝   ::::::
    *              ██║   ██║██║╚██╔╝██║██╔══╝   *      ██╔══██╗██╔══██╗██╔══╝  ██╔══██║██╔═██╗  :::::
                   ██║   ██║██║ ╚═╝ ██║███████╗        ██████╔╝██║  ██║███████╗██║  ██║██║  ██╗:::::
                   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝        ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝::::
                                *                                                                
            *                                 *                                                   

''')


def title_2():
  print('''
        *                                                            :::.
                                              *                       ::::.
                           *                                           :::::                   :.
     *                                                                ::::::                   :::.
                                       *                             :::::                      :::.
                *                                                  .:::::                        :::::
                                                   *              ::::::                        :::::
        *                                                          :::::.                    .::::::  
                             *                                      ::::::                  ::::::
  *             ████████╗██╗███╗   ███╗███████╗        ██████╗ ██████╗:███████╗ █████╗ ██╗  ██╗::
                ╚══██╔══╝██║████╗ ████║██╔════╝  *     ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝:
                   ██║   ██║██╔████╔██║█████╗          ██████╔╝██████╔╝█████╗  ███████║█████╔╝:::
    *              ██║   ██║██║╚██╔╝██║██╔══╝          ██╔══██╗██╔══██╗██╔══╝  ██╔══██║██╔═██╗::::
                   ██║   ██║██║ ╚═╝ ██║███████╗    *   ██████╔╝██║  ██║███████╗██║  ██║██║  ██╗::::
           *       ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝        ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝:::
                                            *                                                    
                           *                                                                     

''')


def title_display():
    for i in range(2):
        clear()
        title_1()
        sleep(0.5)
        clear()
        title_2()
        sleep(0.5)
        clear()
        title_1()
        sleep(0.5)
        clear()
        title_2()
        sleep(0.5)


def tardis1():
  print('''                                                                    
              .::,.                      
             ,looooooox0KK0koooooool;.            
           ;dONNNNNNNNNNNNNNNNNNNNNN0x;           
           oKOKKKKKKKKKKK0KXKKXKKKKK0Kl           
           :K0O0OOOkOOOxodO0OOOOOOOk00;           
           :NXKO:;;.;;;odx0d;;.;;;k0XX;           
           :NXKO;,,.,,,odxKo.;.,;,x0XX;           
           :NXKO;,,.;,,oxkKd,;.;:;k0KX;           
           :NXKO,.. ...oxxKo.,.,;.x0XK,           
           cNXKXK00O000kdxKX00O0KKKOXX;           
           cNXKKd;;;::oxxkOo;;;;;dK0XK;           
           :NXK0;     ,dxOk,     ;K0XK;           
           :NXK0;     ,dxOk,     ;00XK;           
           cNXKXxcllllxkxxOxlllllkK0XK,                     
           cNXKKc.....:xddxc.....cKKXK;           
           cNNK0;     ;xddx;     ;00XK,           
           cNXK0:     ;xoox;     :00XK,           
           :NX00OxxxxxOxlcxOdxxxxO0OXK,           
          .lKK00KKKKKKK0kkOK00K00000K0c.          
          .lxdddddddddddxxddddddddddddl.          
                                           
      ''')
def tardis2():
  print ('''
                
                                        
                       .::.       ..;;..          
                       .:;,.      .lloo.          
             .loooooood0KK0koooooookx:.           
           ;dONNNNNNNNNNNNNNNNNNNNNN0x;           
          .o00KKKKKKKKKKKKKKKKKXKXKK0Kl           
           :K0O0OOOkOOOxodO0O0OOOO0k00;           
    .;.    :NXKO:;;.;;;odd0d;:.;;;k0XX;           
 .,.,:,.,. :NXKO;,,.,,,odxKo.;.,,,x0XX;           
 .,:. .:;. :NXKO;,;.;,,oxxKd,;.;:;k0XX;           
  .:;.;c.  :NXKO,.. ,..oxkKo.,.,;.x0XX;           
   .   .   :NXKXK00OK00kxkKX0KOKK0K0XX;                    
           cNXKK;     ,xxkx,     ;00XK,           
           cNXKK;     ;xxxx,     ;00XK,      .    
           cNNKKo.,.,,okdxkl,,,,,oK0XK,     .l.   
           cNNKXKOOOOOKOod0X00000XX0XK, .,;.....;;
           cNXKKc.....:xddxc.....c00XK,  .,,. .,;.
           cNNK0;     ;xddx;     ;00XK,   ,c...c, 
     .;.   cNXKK:     ;xoox;     :00XK;   ..   .. 
   .:c;::. :NX00OxxxxxOxllxOxxxxxO0OXK,           
    .:.:, .oKK00KKKKKKK0kkO00K000000K0c.          
          .lddddddddddddddddddddddddddl.   .,::,. 
                                           .looo. 

  ''')
def last():
    print('''
 ....,;;....           .:;,.      .lloo.          
 .:c;.   ,:c,..loooooood0KK0koooooookx:.           
   .;...,;.;dONNNNNNNNNNNNNNNNNNNNNN0x;         ,.
   ,:...;:.o0OKKKKKKKKKKKKKKKKKXKXKK0Kl           
           :K0O0OOOkOOOxodO0O0OOOO0k00;           
    .;.    :NXKO:;;.;;;odd0d;:.;;;k0XX;           
 .,.   .,. :NXKO;,,.,,,odxKo.;.,,,x0XX;     .;.   
 .,:. .:;. :NXKO;,;.;,,oxxKd,;.;:;k0XX;  ...;  ,...
  .:;.;c.  :NXKO,.. ,..oxkKo.,.,;.x0XX; .,c:. .::..
   .   .   :NXKXK00OK00kxkKX0KOKK0K0XX;   ,l,.,l.        
     .;.   cNXKK;     ,xxkx,     ;00XK,     . .      
 ....;:,...lNNKK;     ;xxxx,     ;00XK,      .    
 .::,. .;c;oNXKKo.,.,,okdxkl,,,,,oK0XK,     .l.   
   ;,...;. cNNKXKOOOOOKOod0X00000XX0XK, .,;.....;;
  .c:...c, cNXKKc.....:xddxc.....c00XK,  .,,. .,;.
   .    .. cNNK0;     ;xddx;     ;00XK,   ,c...c, 
     .;.   cNNKK:     ;xoox;     :00XK;   ..   .. 
   .:c;::. :NX00OxxxxxOxllxOxxxxxO0OXK,           
    .:.:, .lKK00KKKKKKK0kkO00K000000K0c.          
       ....lddddddddddddddddddddddddddl.                                                 
                                                                                                                                                                        

    ''')

def tardis4():
  print ('''
  .c.               .::.                 
  .;,.  ;;.  .loooooood0KK0koooooookx:.           
   ,l,.,l. :dONNNNNNNNNNNNNNNNNNNNNN0x;           
   ..   ...o0OKKKKKKKKKKKKKKKKKXKXKK0Kl           
           :K0O0OOOkOOOxodO0O0OOOO0k00;      ..   
           :NXK0:;;.;;;odd0d;:.;;;k0XX;   ..,l:...
           :NXKO;,,.,,,odxKo.;.,,,x0XX;  .:c,  :c.
           :NXKO;,;.;,,oxxKd,;.;:;k0XX;    ;;  :. 
           :NXKO,.. ,..oxkKo.,.,;.x0XX;   .;;..:. 
           :NXKXK00OK00kxkKX0KOKK0K0XX;           
           :NXKKd;:;;;oxxOOo;;;;;dK0XX;                      
           cNXKK;     ,xxkx,     ;00XK;   .:.     
   ,;      cNXKK;     ,xxxx,     ;00XX:...,,,...  
,..,,,.,.  cNNKKo.,.,,okdxkl,,,,,oK0XXdc;.. .,::. 
,c,   :;.  cNNKXKOOOOOKOod0X00000XX0XK;.;.   ,,   
 :c..:c.   cNXKKc.....:xddxc.....c00XK;.c:...c;   
 ..  ...   cNXK0;     ;xddx;     ;00XX;.,.   ..   
     .;.   cNNKK:     ;xoox;     :00XK;           
   .:   ::. :NX00OxxxxxOxllxOxxxxdO0OXK,           
    .:.:, .oKK00KKKKKKK0kkO00K000000K0c.          
          .lddddddddddddddddddddddddddl.   
''')
def transition():
  for i in range(2):
    clear()
    tardis1()
    sleep(0.3)
    clear()
    tardis2()
    sleep(0.3)
    clear()
    last()
    sleep(0.3)
    clear()
    tardis4()
    sleep(0.3)
    clear()


def peace_love():
    sleep(1)
    print('''
MMMMMMMMMMMMMMMMMMMMMMMNXK0Okkxxkk0KXWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWWWXkoc;,...........,:lx0NWWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWXkl,..;:coxd;....colc,...:d0NMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWKd,..:d0NNWMMNl...:KMMWKx:...,dNMMMMMMMMMMMMMM
MMMMMMMMMMMMXd,.,l0NWMMMMMMWo...,0MMMMMN0d:..cONMMMMMMMMMMMM
MMMMMMMMMMW0:.,xXWWWMMMMMMMMx....kMMMMMMMWNk:.,kNMMMMMMMMMMM
MMMMMMMMMNx,.,kWMMMMMMMMMMMMk....xMMMMMMMMMWXo..xWMMMMMMMMMM
MMMMMMMMNo..:OWMMMMMMMMMMMWWO,...xWMMMMMMMMMMNo..xNMMMMMMMMM
MMMMMMMWx..lXWMMMMMMMMMMMMMWk....xMMMMMMMMMMMMXl..xWMMMMMMMM
MMMMMMMNl..kWMMMMMMMMMMMMMMWx...,OMMMMMMMMMMMMM0;.cKWMMMMMMM
MMMMMMMNd.,OMMMMMMMMMMMMMWXk;....xNMWWMMMMMMMMMWd..kWMMMMMMM
MMMMMMMXl..kMMMMMMMMMMMMNk:.......lKWMMMMMMMMMMMO,.dWMMMMMMM
MMMMMMMXl.;0MMMMMMMMMWNk:..;,....;.,o0WMMMMMMMMM0;.lNMMMMMMM
MMMMMMMWd.,OMMMMWWMMNOc..:kKd...cKO:.,dKWMMMMMMMk..oNMMMMMMM
MMMMMMMMK:.lXWWMWWWKo,,cONWWx,..cXWNOl;;oKWMWWMWx..kMMMMMMMM
MMMMMMMMWk,.oXWMWKo,.:ONMWMWk,..oNWMMW0l,:kXWMMKl.oNMMMMMMMM
MMMMMMMMMNd..l0Kd,..oXMMMMMM0,..lXMMMMMNO:.,ldxxc:0MMMMMMMMM
MMMMMMMMMWWk;.,,..:ONWMMMMMM0;..:KMMMMMMMNOo;...;xWMMMMMMMMM
MMMMMMMMMMMMXd,...l0XWMMMMMMk...,OMMMMMMMMMXl...xWMMMMMMMMMM
MMMMMMMMMMMMMWXkc,..;ldOXNWM0,...dWMMMMWXOx:.:d0WMMMMMMMMMMM
MMMMMMMMMMMMMMMMWXOdl:,,;:cod:...d0K0Oxl:,;oOXWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNXKkdollc:cdOOkxdodO0XWMMMMMMMMMMMMMMMM
██████ ███████ █████  █████████████        ██        ██      ██████ ██    █████████ 
██   ████     ██   ████     ██             ██        ██     ██    ████    ████      
██████ █████  █████████     █████       ████████     ██     ██    ████    ███████   
██     ██     ██   ████     ██          ██  ██       ██     ██    ██ ██  ██ ██      
██     █████████   ██ █████████████     ██████       ███████ ██████   ████  ███████ 
                                                                                    
''')
    sleep(2)


def church():
    print ('''                    
                                                             .:.                            
                                                             ;Oc                            
                                                             lNd                            
                                                            .o0d.                           
                                                            .loo;                           
                                                            ,c:oo.                          
                                                            ,;;:l,                          
                                                           .;,,.;;                          
                                                           .,.,..:.                         
                                                           ,..,..:.                         
                                                          .;..,. ,;                         
                                                          .; .;. .;.                        
                                                          ,, .;. .,.                        
                                                         .:. .;.  ,,                                              
                                                        ;c...:dc,...:.                             
      ....;oO00XNNN0c:kXWWWWWXk;                        .loco0Ooc:ld;.                      
        .;ld0Xx;...,,:kO000XX0x;                       .ddc;;lo;,.,cl.                      
   .;;;,,;okdc:cc:;:dKXK0Oxc..                          :c.  ;c..::;;.                      
  ,OWWWN0c.   .ONX0KKOxk0d:.                     ......,c:. .lo:o0Oo:.                      
  .okk0XN0,..;loo0WMN0l;cllloc..        ....,.,,,,,,... .....,ll:ckKx.                      
    .c0WMNko0WO. .lkKXxo0WMWNWKl.....,..,,....              .cc.  .dKx.                     
     .;lOKXXOo;,.,d0XNOdOO00Oxl:,....                     .:l,     .cK0c.                   
    .;llllll:..o0000Odc:;...                             .oc.        ,ONO,                  
   ..oXMWNXXK0KNNOc.                                   .co,    .....  .dX0c                 
  .cddxXWMMMMN0o..                                   .;ol;.  ..;lcll;.  ;kKo.               
    ..:0NNKOx;.                                    .;o::oOO;.cdld0Kxc;..;oOKO,              
    c0NWW0o.                                 ....,col. ,clk:.ox,,dkc:l;;x0xlOO,             
   .lKXOc.              .....,,,;:cclooloxkkkkxxdkOd.  .;;o:.lc  ;o..c;.:dd.:k,             
  .,ldl;;;;:ccclodddxollokOxxO0dcclclkd;:lO0:.....;:.  ..;d:.cc  ;l..:,.,ll.,Oo             
 ,oKNXOdco0NXd;,:xKKO,   .do:lx,    .ll.;:dO.    .;c.  .,;dc.;;  ;l..c;.:lo.,KKl..          
  .:OXx. .xK0;   l0Ok,   .dxlox,    .dd;::dk.    .;c.  .;;dc.,,  ;l..c;,cco.,KW0:.          
  .;xK0l..dOk,  .lkOk.   .lc,co.    .od,;;od.    .;:.  ...l;.;,  ;o..l:.;:c.,KMNKd.         
:o0NNKKKxlol;.   ..,.     .....      .::;...     .;l,     ..;ll;,cl;;ll::.  ,KMMMW0o:,........  ...x
,ckOOO0NMWNKkkko;....,.,::.          .oOOddo:.   .;o;     .:lcllll:;;;,,,...;KWWWNNKOl;;;;;..,,.,..x
 .;;cololoxxooool:,:dkO00Okoccccc:;;;okOOddO0x:,.;ldc....;c:;;:cldolllc:::lool;.,....       
                     ....................  ..................................                     .k ''')
    sleep(2)



def berries():
    print('''

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMWXNWMWMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMNodNMMMMMMM0;,xNMWMMMMMXkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMXoxWMMMMMMMMMKc .0MMMMMMMk. .dNMMMMMXc.oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:.dNMMMMMMMXc  .oWMMMMMWd   .0MMMMWd. ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWl .:0WMMMMWx.   .kWMMMMNl   .xMMMWx.  ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx.  .lKWMMX:     .OWMMMK;   .dWMMk.   lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0.    .oKWK;      ,0WWMO.   .xMWk.   .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl      .lk:       ,o0Nc    .0Xo.   .dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:       ..         ,c.    .l,    .dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc.   ....    .,;;:::..   .;,...;OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOoc::;;;::.;l:.....:l;;c:;,;:oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKc.    .;kk,       ;Od.     .cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWo       .xx.       .xl       .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;     .l00:       :Ok;.     ,kKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkl:c:clol:;.,cc;,,,;cc,.cc::;:cc...dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc.   .,kO,     .:kKx,.    .,xx,.     lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk.      :d.      .o0c        co.      cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK,     .dKc       ;kx,       lKx;....cKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0l,..;xNWKo..   .okxoc;...:dko::::oKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkc;:kKd,,::;lkk:.. .,;lKNo.     .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0,   ;o.     .kd.      .dO.      ,0MMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;   .o,      ok.       o0c.   .:OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl...cx:.  .:xxlc;.  .cl:;::cd0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0ko:::;;dk; .,;:;;dd.    ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:     ;o.       :o.    cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0:.   .xo.     .xx,..:xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0o:;::::;;:lc:,,;xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKl.    ..lx.   ,OWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkl::lxOKx::cxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

''')
    sleep(2)


def future_display():
    print('''
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWNk:,:dKWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWKl.    .c0WWWWWW
WWWWWWWWWWWWWWWWWWWWWWNk:   .,.  .dXWWWW
WWWWWWWWWWWWWWWWWWWNKk;  ;l..ok:.  ,kNWW
WWWWWWWWWNOkKWWWWW0:.,: .kNx:.;oOkl,.;kW
WWWWWWWWXl. :xNWW0,,d0d.cNWWO,..:kNNOoxN
WWWWWWNO,     cK0,.OMO:;KWWWX000KXWWWWWW
WWWWXo:. .,;.  ...dOl;:KWWWWWWWWWWWWWWWW
WWWK:   ,ONWXd.  lx;,oNWWWWWWWWWWWWWWWWW
WWK;.  .OWWWWNc cxckNWWWWWWWWWWWWWWWWWWW
WK;.c;.oWWWWWx.cOokWWWWWWWWWWWWWWWWWWWWW
Nc.oc.;XWWWNd:lXX0NWWWWWWWWWWWWWWWWWWWWW
Nddl.:kWWWXl,xNWWWWWWWWWWWWWWWWWWWWWWWWW
WKc;d0NWNk:c0WWWWWWWWWWWWWWWWWWWWWWWWWWW
WOxKWN0o:ckNWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWW0dc:lONWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WKkxx0NWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW''')
    sleep(2)

def zombies():
    print('''
MMMMMMMNkoccxXMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWd.   .xWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMK;    cNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMXl.  :xKWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWKd,     .,lKMMMMMMMMMMMMMMMMMMMMM
MMMMMXl.          ;kWWMMMMMMMMMMMMMMMMMM
MMMMM0;           .xWWMMMMMMMMMMMMMMMMMM
MMMMMK,           .dWWMMMMMMMMMMMM0lckNM
MMMMMO;         cl..:xNMMMMMMMMMMX:  ,KM
MMMWk;...       oNx; .cXMMMMMMWK00; .dNM
MMKl;;kx.       .kMXOl.:KMMMMXl. .  ,ONM
Wx,:OWMk.        ;XMWNd.:XMMMx.       :K
k.;XMMMx.        .xMWM0,;OMXd;;.      .k
x;oNMMWo    ,;    oMMMNo;xx::kx.    ..:X
NWWMMMMx.  ;0k.  .OMMMWNKdo0WNc    .l;:X
MMMMMMMd   cN0;  .kMMMMMWXNMMx.    .xo,O
MMMMMMWl   lWX;   cNMMMMMMMMX:      dXok
MMMMMM0;  ,0MW0,  .o0XMMMMMMk.      lNod
MMMMMK;  ;0WMMMk,.  .cNMMMMMo  .c;  ;K0K
MMMMNc  ;0MMMMMWK;   .xMMMMN:  ;Kk. ;0MM
MMMMO; .xWMMMMMMMKc.  dMMMM0; .xMX;  cNM
MMMNo  cNMMMMMMMMMNo..cWMMMK,.lKMNdc;;0M
MMMk. ,0MMMMMMMMMMMOc..OMMMN:cNMMWNWO;oW
MMWl  dWMMMMMMMMMNk,   oWMWk;lWMMMMMWd,o
MMNc .dWMMMMMMMMWO:;;,l0WMXc,OMMMMMMMNo:''')
    sleep(2)


def one():
  print( ''' MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l,;:oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMXxod0WMMMMMMMMMMMMMMM0,     :XMMMMMMMMMMMMMMMNOookNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXc   .lXMMMMMMMMMMMMMMx.     .OMMMMMMMMMMMMMW0:   .oWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMN0kOXWMMMMMMMMMMK,     lNMMMMMMMMMMMMMO.     ;KMMMMMMMMMMMMMX:     cNMMMMMMMMMMWKOkKWMMMMMMMM
MMMMMMNo.  .c0WMMMMMMMMNo.    ;XMMMMMMMMMMMMMWx.   .OWMMMMMMMMMMMMMO.    .xWMMMMMMMMWO:.  .xWMMMMMMM
MMMMMMNc     .xWMMMMMMMMNd.   :XMMMMMMMMMMMMMWx.   .OMMMMMMMMMMMMMM0.  .,kWMMMMMMMMNo.     oWMMMMMMM
MMMMMMM0;     ,KMMMMMMMMMWXo. .cKMMMMMMMMMMMWO.     ;KMMMMMMMMMMMWO;  .dNMMMMMMMMMMk.     cXMMMMMMMM
MMMMMMMMXd,.  .xWMMMMMMMMMMk.   .xNMMMMMMMMM0,       :XMMMMMMMMMXo.   .0MMMMMMMMMMNo.  .:kNMMMMMMMMM
MMMMMMMMMMNKk, .:kNMMMMMMMMk.    .cKWMMMMMMK:         lNMMMMMMW0;     .0MMMMMMMWXx,  :OXWMMMMMMMMMMM
MMMMMMMMMMMMWk.   ,xXMMMMMMO.      .kNMMMMXc          .oWMMMMNd.      ;KMMMMMWKo.   .0MMMMMMMMMMMMMM
MMMMMMMMMMMMMNl     .oKWMMM0.       .lNMMMO.           ;KMMMK:        :XMMMW0l.    .dWMMMMMMMMMMMMMM
MMMMMMMMMMMMMM0,      .l0WMNOl,      lNMMMWx.         ,OWMMMX:     .;o0WMNO:.      :XMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWx.       ;KMMMMNl     oWMMMMO.         ;KMMMMNc    .dWMMMMO.       .OMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMXc       .OWMMMWo     .cxOko.           ,dOOx:.    .xWMMMWx.      .oWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM0.       .okkx:.                                   .lxkxc.       ;XMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWd.                                                             .kMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMX:                         ...........                         lNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMO.          ...;:loddxxkxkkkkkkkkkkkkkkkxxdolc:;...          ;KMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWo    ..:ldxxxxdolcc:;,.......;;,.......,;:clodxxkxxol;.    .xWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMKc.cdxxdl;....,;.          .lOOd:.         ..;,...,:ldxxo:.lNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWKxl,.       ;xOo.         ..;,..          ,xOd.       .;lxXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWd.          ..:::cllooooooooooooooooooollc::;..          .OMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWo     ..:loodoollc:;,.................,;:clloodooc;.     .kMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMk. .codol:...                                 ..,:oddo:. .0MMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXxdxl,.        ...,;;:cclllllllllllcc:;,....        .;oxdkNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNo.         .;lxO0KXNWWWWWWWWWWWWWWNNXK0kdc;.         .xWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMM0,     ;c;...........,,,;;;;;;;;;,,...........,:l,     :XMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWk;.   ;d0KKK0kxdoolcc::::::::::::ccllodxkO0KXKOo.   .:0WMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNOo;.  ..;cldxkO00KKXXXXXXXXXXXXKKK00Okxolc;.. ..:d0WMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWXOxoc;,...............................,:cox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXKOOkxddooollllllloooddxkO0KXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 __   __           __        _____  _   _   _ 
 \ \ / /__  _   _  \ \      / / _ \| \ | | | |
  \ V / _ \| | | |  \ \ /\ / / | | |  \| | | |
   | | (_) | |_| |   \ V  V /| |_| | |\  | |_|
   |_|\___/ \__,_|    \_/\_/  \___/|_| \_| (_)
                                              
''')
def two ():
  print( ''' MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l,;:oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMXxod0WMMMMMMMMMMMMMMM0,     :XMMMMMMMMMMMMMMMNOookNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXc   .lXMMMMMMMMMMMMMMx.     .OMMMMMMMMMMMMMW0:   .oWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMN0kOXWMMMMMMMMMMK,     lNMMMMMMMMMMMMMO.     ;KMMMMMMMMMMMMMX:     cNMMMMMMMMMMWKOkKWMMMMMMMM
MMMMMMNo.  .c0WMMMMMMMMNo.    ;XMMMMMMMMMMMMMWx.   .OWMMMMMMMMMMMMMO.    .xWMMMMMMMMWO:.  .xWMMMMMMM
MMMMMMNc     .xWMMMMMMMMNd.   :XMMMMMMMMMMMMMWx.   .OMMMMMMMMMMMMMM0.  .,kWMMMMMMMMNo.     oWMMMMMMM
MMMMMMM0;     ,KMMMMMMMMMWXo. .cKMMMMMMMMMMMWO.     ;KMMMMMMMMMMMWO;  .dNMMMMMMMMMMk.     cXMMMMMMMM
MMMMMMMMXd,.  .xWMMMMMMMMMMk.   .xNMMMMMMMMM0,       :XMMMMMMMMMXo.   .0MMMMMMMMMMNo.  .:kNMMMMMMMMM
MMMMMMMMMMNKk, .:kNMMMMMMMMk.    .cKWMMMMMMK:         lNMMMMMMW0;     .0MMMMMMMWXx,  :OXWMMMMMMMMMMM
MMMMMMMMMMMMWk.   ,xXMMMMMMO.      .kNMMMMXc          .oWMMMMNd.      ;KMMMMMWKo.   .0MMMMMMMMMMMMMM
MMMMMMMMMMMMMNl     .oKWMMM0.       .lNMMMO.           ;KMMMK:        :XMMMW0l.    .dWMMMMMMMMMMMMMM
MMMMMMMMMMMMMM0,      .l0WMNOl,      lNMMMWx.         ,OWMMMX:     .;o0WMNO:.      :XMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWx.       ;KMMMMNl     oWMMMMO.         ;KMMMMNc    .dWMMMMO.       .OMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMXc       .OWMMMWo     .cxOko.           ,dOOx:.    .xWMMMWx.      .oWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM0.       .okkx:.                                   .lxkxc.       ;XMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWd.                                                             .kMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMX:                         ...........                         lNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMO.          ...;:loddxxkxkkkkkkkkkkkkkkkxxdolc:;...          ;KMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWo    ..:ldxxxxdolcc:;,.......;;,.......,;:clodxxkxxol;.    .xWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMKc.cdxxdl;....,;.          .lOOd:.         ..;,...,:ldxxo:.lNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWKxl,.       ;xOo.         ..;,..          ,xOd.       .;lxXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWd.          ..:::cllooooooooooooooooooollc::;..          .OMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWo     ..:loodoollc:;,.................,;:clloodooc;.     .kMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMk. .codol:...                                 ..,:oddo:. .0MMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXxdxl,.        ...,;;:cclllllllllllcc:;,....        .;oxdkNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNo.         .;lxO0KXNWWWWWWWWWWWWWWNNXK0kdc;.         .xWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMM0,     ;c;...........,,,;;;;;;;;;,,...........,:l,     :XMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWk;.   ;d0KKK0kxdoolcc::::::::::::ccllodxkO0KXKOo.   .:0WMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNOo;.  ..;cldxkO00KKXXXXXXXXXXXXKKK00Okxolc;.. ..:d0WMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWXOxoc;,...............................,:cox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXKOOkxddooollllllloooddxkO0KXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 ██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██     ██ 
 ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██     ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██     ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██        
   ██     ██████   ██████       ███ ███   ██████  ██   ████     ██ 
                                                                   
''')
def three():
  print( ''' MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l,;:oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMXxod0WMMMMMMMMMMMMMMM0,     :XMMMMMMMMMMMMMMMNOookNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXc   .lXMMMMMMMMMMMMMMx.     .OMMMMMMMMMMMMMW0:   .oWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMN0kOXWMMMMMMMMMMK,     lNMMMMMMMMMMMMMO.     ;KMMMMMMMMMMMMMX:     cNMMMMMMMMMMWKOkKWMMMMMMMM
MMMMMMNo.  .c0WMMMMMMMMNo.    ;XMMMMMMMMMMMMMWx.   .OWMMMMMMMMMMMMMO.    .xWMMMMMMMMWO:.  .xWMMMMMMM
MMMMMMNc     .xWMMMMMMMMNd.   :XMMMMMMMMMMMMMWx.   .OMMMMMMMMMMMMMM0.  .,kWMMMMMMMMNo.     oWMMMMMMM
MMMMMMM0;     ,KMMMMMMMMMWXo. .cKMMMMMMMMMMMWO.     ;KMMMMMMMMMMMWO;  .dNMMMMMMMMMMk.     cXMMMMMMMM
MMMMMMMMXd,.  .xWMMMMMMMMMMk.   .xNMMMMMMMMM0,       :XMMMMMMMMMXo.   .0MMMMMMMMMMNo.  .:kNMMMMMMMMM
MMMMMMMMMMNKk, .:kNMMMMMMMMk.    .cKWMMMMMMK:         lNMMMMMMW0;     .0MMMMMMMWXx,  :OXWMMMMMMMMMMM
MMMMMMMMMMMMWk.   ,xXMMMMMMO.      .kNMMMMXc          .oWMMMMNd.      ;KMMMMMWKo.   .0MMMMMMMMMMMMMM
MMMMMMMMMMMMMNl     .oKWMMM0.       .lNMMMO.           ;KMMMK:        :XMMMW0l.    .dWMMMMMMMMMMMMMM
MMMMMMMMMMMMMM0,      .l0WMNOl,      lNMMMWx.         ,OWMMMX:     .;o0WMNO:.      :XMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWx.       ;KMMMMNl     oWMMMMO.         ;KMMMMNc    .dWMMMMO.       .OMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMXc       .OWMMMWo     .cxOko.           ,dOOx:.    .xWMMMWx.      .oWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM0.       .okkx:.                                   .lxkxc.       ;XMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWd.                                                             .kMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMX:                         ...........                         lNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMO.          ...;:loddxxkxkkkkkkkkkkkkkkkxxdolc:;...          ;KMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWo    ..:ldxxxxdolcc:;,.......;;,.......,;:clodxxkxxol;.    .xWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMKc.cdxxdl;....,;.          .lOOd:.         ..;,...,:ldxxo:.lNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWKxl,.       ;xOo.         ..;,..          ,xOd.       .;lxXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWd.          ..:::cllooooooooooooooooooollc::;..          .OMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWo     ..:loodoollc:;,.................,;:clloodooc;.     .kMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMk. .codol:...                                 ..,:oddo:. .0MMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXxdxl,.        ...,;;:cclllllllllllcc:;,....        .;oxdkNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNo.         .;lxO0KXNWWWWWWWWWWWWWWNNXK0kdc;.         .xWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMM0,     ;c;...........,,,;;;;;;;;;,,...........,:l,     :XMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWk;.   ;d0KKK0kxdoolcc::::::::::::ccllodxkO0KXKOo.   .:0WMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNOo;.  ..;cldxkO00KKXXXXXXXXXXXXKKK00Okxolc;.. ..:d0WMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWXOxoc;,...............................,:cox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXKOOkxddooollllllloooddxkO0KXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                 ______                                              ______                          
``..     ..''  .~      ~.  |         |        `.               .'  .~      ~.  |..          |        
    ``.''     |          | |         |          `.           .'   |          | |  ``..      |        
      |       |          | |         |            `.   .   .'     |          | |      ``..  |        
      |        `.______.'  `._______.'              `.' `.'        `.______.'  |          ``|      
''')
def four():
  print( ''' MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l,;:oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMXxod0WMMMMMMMMMMMMMMM0,     :XMMMMMMMMMMMMMMMNOookNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXc   .lXMMMMMMMMMMMMMMx.     .OMMMMMMMMMMMMMW0:   .oWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMN0kOXWMMMMMMMMMMK,     lNMMMMMMMMMMMMMO.     ;KMMMMMMMMMMMMMX:     cNMMMMMMMMMMWKOkKWMMMMMMMM
MMMMMMNo.  .c0WMMMMMMMMNo.    ;XMMMMMMMMMMMMMWx.   .OWMMMMMMMMMMMMMO.    .xWMMMMMMMMWO:.  .xWMMMMMMM
MMMMMMNc     .xWMMMMMMMMNd.   :XMMMMMMMMMMMMMWx.   .OMMMMMMMMMMMMMM0.  .,kWMMMMMMMMNo.     oWMMMMMMM
MMMMMMM0;     ,KMMMMMMMMMWXo. .cKMMMMMMMMMMMWO.     ;KMMMMMMMMMMMWO;  .dNMMMMMMMMMMk.     cXMMMMMMMM
MMMMMMMMXd,.  .xWMMMMMMMMMMk.   .xNMMMMMMMMM0,       :XMMMMMMMMMXo.   .0MMMMMMMMMMNo.  .:kNMMMMMMMMM
MMMMMMMMMMNKk, .:kNMMMMMMMMk.    .cKWMMMMMMK:         lNMMMMMMW0;     .0MMMMMMMWXx,  :OXWMMMMMMMMMMM
MMMMMMMMMMMMWk.   ,xXMMMMMMO.      .kNMMMMXc          .oWMMMMNd.      ;KMMMMMWKo.   .0MMMMMMMMMMMMMM
MMMMMMMMMMMMMNl     .oKWMMM0.       .lNMMMO.           ;KMMMK:        :XMMMW0l.    .dWMMMMMMMMMMMMMM
MMMMMMMMMMMMMM0,      .l0WMNOl,      lNMMMWx.         ,OWMMMX:     .;o0WMNO:.      :XMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWx.       ;KMMMMNl     oWMMMMO.         ;KMMMMNc    .dWMMMMO.       .OMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMXc       .OWMMMWo     .cxOko.           ,dOOx:.    .xWMMMWx.      .oWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM0.       .okkx:.                                   .lxkxc.       ;XMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWd.                                                             .kMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMX:                         ...........                         lNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMO.          ...;:loddxxkxkkkkkkkkkkkkkkkxxdolc:;...          ;KMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWo    ..:ldxxxxdolcc:;,.......;;,.......,;:clodxxkxxol;.    .xWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMKc.cdxxdl;....,;.          .lOOd:.         ..;,...,:ldxxo:.lNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWKxl,.       ;xOo.         ..;,..          ,xOd.       .;lxXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWd.          ..:::cllooooooooooooooooooollc::;..          .OMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWo     ..:loodoollc:;,.................,;:clloodooc;.     .kMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMk. .codol:...                                 ..,:oddo:. .0MMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXxdxl,.        ...,;;:cclllllllllllcc:;,....        .;oxdkNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNo.         .;lxO0KXNWWWWWWWWWWWWWWNNXK0kdc;.         .xWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMM0,     ;c;...........,,,;;;;;;;;;,,...........,:l,     :XMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWk;.   ;d0KKK0kxdoolcc::::::::::::ccllodxkO0KXKOo.   .:0WMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNOo;.  ..;cldxkO00KKXXXXXXXXXXXXKKK00Okxolc;.. ..:d0WMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWXOxoc;,...............................,:cox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXKOOkxddooollllllloooddxkO0KXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
  _     _      _     _      _     _       _     _      _     _      _     _    !
  (c).-.(c)    (c).-.(c)    (c).-.(c)     (c).-.(c)    (c).-.(c)    (c).-.(c)    
   / ._. \      / ._. \      / ._. \       / ._. \      / ._. \      / ._. \     
 __\( Y )/__  __\( Y )/__  __\( Y )/__   __\( Y )/__  __\( Y )/__  __\( Y )/__   
(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._) (_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)  
   || Y ||      || O ||      || U ||       || W ||      || O ||      || N ||     
 _.' `-' '._  _.' `-' '._  _.' `-' '._   _.' `-' '._  _.' `-' '._  _.' `-' '._   
(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.) (.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)  
 `-'     `-'  `-'     `-'  `-'     `-'   `-'     `-'  `-'     `-'  `-'     `-'      
''')
# import only system from os 
from os import system, name 
# from random import randint
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
def win():
  for i in range(3):
    clear()
    one()
    sleep(0.4)
    clear()
    two()
    sleep(0.4)
    clear()
    three()
    sleep(0.4)
    clear()
    four()
    sleep(0.4)
    clear()
    one()
    sleep(0.4)
    clear()
    two()
    sleep(0.4)
    clear()
    three()
    sleep(0.4)
    clear()
    four()
    sleep(0.4)
    clear()
    one()
    sleep(0.4)
    clear()
    two()
    sleep(0.4)
    clear()
    three()
    sleep(0.4)
    clear()
    four()
    sleep(0.4)
    clear()

def skulls():
    print('''
                                           
                                          
                                                     .';cccclc:'.
                                                  .:d0NWMMMMMMWN0o,
                                                 :0WMMMMMMMMMMMMMMNk, 
                                                lXMMMMMMMMMMMMMMMMMWXl.
                                               ;kWMMMMMMMMMMMMMMMMMWWNl 
                                              .cdXMMWWMMMMMMMMMMMMMWN0o.
                                              .cl0MWWWWMMMWMMMMMMMWWOoc.
                                              .:okdc::lkNMWWWXkocdOK0d,  
                                               ;;.     .lxxkx;     .,;.  
                                               :c      .cOXWXc       :c. 
                                              .kx.  ..,oKXXNWO:'....:K0' 
                                              .ldc;,';xKd'';okl::::lk0d.
                                                     .xd.    cx'...  . 
                                                     lKd.....lOc     
                                                    .:oooc;,;ldc.  
                                                       .,:,'.    
                                                                          
''')




def dice(name):
    x =(random.randint(0,9))
    if x % 2 == 0:
        typewriter("  So the dice decided... you are going to the forest\n")
        sleep(1)
        forest(name)
    else:
        print("So the dice decided .... you are going to the village\n")
        sleep(1)
        village(name)



def start():
    title_display()
    print("\n\
    What is your name?")
    name = input(">>>   ")
    name = name.lower().capitalize()
    typewriter(f"    Welcome {name} let's play a game.\n")
    typewriter(f"So, let's face it {name} You are a bit of a genius. You just invented a fully working time machine. Time to take it for a ride:\n")
    sleep(2)
    transition()
    trouble_in_70s(name)



def trouble_in_70s(name):
    the_beginning(name)


def the_beginning(name): 
    typewriter(f"    You just wanted to go back a few days to peak at those Lottery numbers!\n\
    But looks like you {name} went too far back!!\n\
    Poking your head out, you can hear 'Dancing Queen' in the distance and see people walking around in weird flowery clothes.\n\n\n\
    YOU ARE IN THE 70'S!")
    peace_love()
    typewriter("You look around and see that your emergency lock is about to go off and shut you inside the machine... \n\n\
         FOREVER!\n\n\
    The only way to stop it is to pass the code which is x for 5x -4 = 6 \n") #answer is 2
    x = input("X = ")
    x = int(x)
    if x == 2:
        typewriter("    Congratulations, you stopped the clock ! You can now take a stroll and see what the 70's were all about\n\
        Or stay in the machine and  try to get home as soon as you can!\n")
        stay_or_go(name)
    else: 
        typewriter("    Oh no, you did not get it right and now you will be stuck in the machine forever")
        sleep(2)
        uh_oh(name)

def stay_or_go(name):
    print(" So do you want to stay or go ?")
    choice = input(">>>   ")
    if choice.lower() == "stay":
        typewriter("    So you decide to stay in a machine and try to come back home asap GOOD CHOICE !\n\
        You dial in the date you want to come back to and pray for the best.")
        sleep(2)
        medieval(name)
    elif choice.lower() == "go":
        typewriter("    So you decided to have a look around, after all you dont get a chance like that everyday.\n\
        But the further you go the more stares you get, your clothes look weird and the fact that you are staring at everything is not helping.\n\
        You soon find yourself surrounded by the police accusing you of being a spy. The only way of proving your indentiy is to answer questions about current affairs\n\
        The question is ...What great band broke up in the 1970s\n\
        (The hits included songs  \"Lucy in the sky with dimonds\" or \"Yellow Submarine\")")
        band(name)
    else:
        typewriter("    Please choose Stay or Go to explore !\n")
        stay_or_go(name) 
     
    
def band(name):
    y = input(">>>   ")
    if y.lower() == "the beatles":
        typewriter("    You did it ! You can safely go back to your time machine now.")
        sleep(2)
        medieval(name)
    elif y.lower() == "beatles":
        typewriter("    You did it ! You can safely go back to your time machine now.")
        sleep(2)
        medieval(name)
    else:
        typewriter("    You failed to indentify yourself and will spend the rest of your life in prison !")
        sleep(2)
        uh_oh(name)



def medieval(name):
    transition()
    typewriter("    \n\
    You can feel a pulling sensation around your stomach as you hit the ground,\n\
    You look around outside but the place looks nothing like your house.\n\
    In fact it looks nothing like 2021, more like\n\n\
     ...Medieval times...\n")
    sleep(1)
    church()
    typewriter(f" Oh crap you are even more back in time than you were originally.\n\
    Hope you stuided history!\n\
    As you hear grumbling of your stomach, you realise the pulling sensation was hunger.\n\n\
    You need to find food, fast.\n\
    You see a small medieval village next to a river, on the right of village- a forest.\n\n\
    You might think You have a choice to make here, but no dear {name}, like most things in life \n\
    the choice will be up to fate. You will throw an imaginary dice and this will lead you to your destiny\n\
        Do you want to throw the dice (Yes or No ?)")
    choice = input(">>>  ")
    if choice.lower() == "yes":
        typewriter("    So let the dice roll")
        sleep(1)
        dice(name)
    elif choice.lower() == "no":
        typewriter("Well you have to say yes if u want to play, let me start u over")
        sleep(2)
        medieval(name)
    else:
        typewriter("    Please choose yes or no !")
        sleep(1)
        medieval(name)


def forest(name):
    typewriter("    As you move towards the Forest you think\n\
    while there's less chance of being found but you aren't quite sure what is edible.")
    typewriter("\n\
    Will you continue on or try your chances at the village? (write continue or village)")
    choice = input(">>>  ")
    if choice.lower() == "continue":
        typewriter("    You carry on into the Forest, dont want to bump into anyone.")
        forest_deicsion(name)
    elif choice.lower() == "village":
        typewriter("    You would rather not poison yourself on second thought\n\
        you head back.")
        sleep(2)
        village(name)
    else:
        typewriter("    Please enter vaild input, continue or village.\n\
        Come on you've done this before! Again!")
        sleep(2)
        forest(name)

def forest_deicsion(name):
    typewriter(f"\n\
    As you move into the forest you keep a path in view, dont want to get lost now.\n\
    After some time you come accross a small bush with bright red berries\n\
    So {name} will you crouch down in the bushes and get some sweet fruit\n\
    Or will you carry on, isn't there something about red berries? Continue or crouch?")
    choice = input(">>>   ")
    if choice.lower() == "continue":
        typewriter("    You shake your head, sure you remember something about red berries.\n\
        You carry on the path, shouting and horns are heard in the distence and you run looking for shelter,\n\n\n\
        You are spotted and killed by a hunting party")
        sleep(2)
        uh_oh(name)
    elif choice.lower() == "crouch":
        typewriter(f"\n\
        They do look delicous, dont they {name}?\n\
        You crouch down to pick the berries and half way through you hear shouting and horns.\n\n\
        A hunting party!!\n\
        You press down to the dirt, lucky you, The bushes cover you completly!\n\
        As you walk back to your time travel machine snacking on berries\n\
            You   start to feel   just a   bit  off\n\
            and\n\
                you\n\
                     f\n\
                       a\n\
                          l\n\
                           l\n\
                            l\n\
                              un\n\
                                con\n\
                                  sci\n\
                                   ous\n\n\n\
        Well, well, well.\n\
        Looks like you should have payed more attention to things outside the lab.\n\
        Doesn't it?")
        sleep(1)
        berries()
        sleep(2)
        uh_oh(name)
    else:
        typewriter("Where instructions not clear? INPUT CROUCH OR CONTINUE! Time to rewind!")
        sleep(2)
        forest(name)





def lucky_number(name):
    typewriter("  \n  So what number from 1 to 10 I am thinking about future man ?\n")  
    choice = input(">>>   ")
    choice = int(choice)
    if choice <= 5:
        typewriter("  How did you know that ! Ok then a deal is a deal get your bread")
        sleep(2)
        going_to_the_future (name)
    elif choice >= 6 and choice < 10:
        typewriter("oh no that was not it, I think it will be best if we just burn you at the stake.\n ")
        sleep(2)
        uh_oh(name)
     
    else: 
       typewriter("    I said number from 1 to 10, I am getting impatient now.")
       sleep(2)
       lucky_number(name)
      
 

def village(name):
    typewriter("\n\
    You slowly move towards the edge of village keeping to the shadows,\n\
    And looking at the houses at the edge of the settelment, seeing if there's unattended food.\n\
    Not too many people, ah look. Merchants at the pier.\n\
    So everyone is at that side of the village, lucky.\n\
    Double luck you manage to find a loaf of bread cooling in an open window.\n\
    Now are you going to politely ask for it or just steal it?\n What are you doing(ask or steal)")
    sleep(1)
    getting_bread(name)

def going_to_the_future (name):
    typewriter("    You grab it and quickly,mumble thanks and make your way back to the time machine eating your prize.\n\
    feeling full you decide to try travelling agian, you check the inputs twice,\n\
    now you are not going back in time anymore,that is for sure")
    sleep(2)
    future(name)

def getting_bread (name):
    choice = input(">>>   ")
    if choice ==  "ask":
        typewriter("Oh what a polite person you are ! Of course the villagers gave you the bread, manners pay off!")
        sleep(1)

        going_to_the_future(name)
    elif choice == "steal":
        typewriter ("You were caught by a Marchant but he finds your funny clothes amusing, if you guess what number he is thinking about he will let you go !\n")

        lucky_number(name)
    else:
        typewriter("you need to say ask or steal, let try it all agian shall we ?")
        getting_bread(name)



def future(name):
    transition()
    typewriter(f"\n\n\n\
    {name} after your last lucky escape from medieval times, the time machine lands again,\n\
    the clock says it's the year 2525.")
    future_display()
    typewriter("With some trepidation, you reach to open the door.\n\
    Then a klaxon alarm sounds. The ship's computer informs you that you are running out of fuel.\n\
    If this happens you will be trapped forever in the future. Time is running out. You open the door.\n\
    In front of you is a barren wasted landscape with mountains in the west and what appears to be a structure in the East.\n\
    All other directions lead to an endless sea of destruction.\n\
    Which way do you go?  Choose East or West")
    choice = input(">>>   ")
    if choice.lower() == "east":
        east(name)
    elif choice.lower() == "west":
        west(name)
    else:
        print("    Invalid choice, you've gotten to the third part and you still struggle? Is this too hard?")
        sleep(2)
        future(name)




def east (name):
    typewriter("    You walk East, after walking for hours on the strange spongy ground  which your feet sink into,\n\
    you find your way to a bunker, the door ajar. The inhabitants must of left years ago or be dead.\n\
    You walk in, your torch illuminates the area and you find ten canisters filled with fuel.\n\
    Not knowing how much you need, how many carnisters are u taking?")
    sleep(2)
    bunker(name)

def bunker(name):
    print("    Pick a number from 1 to 10. CHOOSE WISELY")  
    choice = input(">>>   ")
    choice = int(choice)
    if choice <= 3:
        typewriter("    You decide not to carry too much, you only need enough for one ride, right?\n\
        You walk back to your ship, soon you will be home.But oh no ! The moment you put it into the machine\n\
        You see it is not enough ! It is too late to come back now as the toxic fumes infect your lungs !")
        sleep(2)
        uh_oh(name)
     
    elif choice >=4 and choice <= 6: 
       typewriter("    You take a hefty amount but not too much, just right in the middle. YOU CHOSE WISELY\n\n\
       You are almost home.\n\
       You reach the ship just in time, you could hear inhuman howling sounds following you.\n\
       You refuel, enter the year 2023 (hoping Covid will be over) and press the time warp button.\n\
       The ship rockets through time and space with the Beatles pumping out of the stereo.\n\
       You land, what a ride!")
       sleep(2)
       transition()
       win()
     
    elif choice >=7 and  choice <= 10 :
        typewriter("You take a good amount, better safe than sorry right ?\n\
        Then you stop, unable to move.\n\
        You're sinking into the ground, your boots start to melt, toxic fumes are all around you,\n\
        Your skin is melting, agonizing pain envelopes you. This is the end of your trip through time.")
        sleep(2)
        uh_oh(name)
    else:
         typewriter("   Invalid choice,  pick a number between 1 and 10 !")
         sleep(2)
         bunker(name)


def west (name):
    typewriter(f"    {name} goes West towards the mountains, they hear strange howling in the distance.\n\
    It's getting closer. It's not like any animal you've heard. Your heartbeat fills your ears.\n\
    You know the truth now, its' mutant cannibals but it's too late. Your journey ends here..\n\n\n\n\
    ") #END CREDITS / LOOP to beginning of game. 
    sleep(2)
    zombies()
    sleep(1)
    uh_oh(name)

def uh_oh(name):
    clear()
    skulls()
    time.sleep(2)
    os.system("cls") 
    typewriter(f"\n\n\n\n    Whelp {name} look at that!\n\
    Gone and got yourself lost or killed or trapped in the past or future!\n\
    All the possibilities and you choose this one!\n\
    So tell me....\n\n\
    Want to try again? Yes or No this time please!")
    choice = input(">>>   ")
    if choice.lower() == "yes":
        typewriter("    Good choice my friend!\n\
        Just one second and you'll be at the very start of this mess!!\n\
        You could even change your name! Since you did so bad with this one!")
        sleep(1)
        start()
    elif choice.lower() == "no":
        typewriter("    Aww and I thought we were having fun!\n\
        Right then, lets get you out of here as you dont want to play!\n\n\n\n\n\n\n\n\
        Yes? what are you still doing here! You can go!")
    else:
        typewriter("Oh come on! Yes or No, it's very simple!\n\
        Is this the reason you couldn't make it home?\n\
        Very dumb indeed.\n\n\
        Let's try again shall we!")
        sleep(2)
        uh_oh(name)

start()
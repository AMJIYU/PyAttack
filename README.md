# PyAttack

基于python的批量漏洞检测（抓鸡）脚本......
</br></br>
Usage:</br>
[*]python &nbsp;mass_attack.py -n ewebeditor,webdav,struts2 -t http://www.xxx.com    针对单网站指定漏洞检测

[*]python &nbsp;mass_attack.py -n 1(ewebeditor)  针对批量网站进行单个漏洞检测

[*]python &nbsp;mass_attack.py -n all    针对批量网站进行所有漏洞检测


</br></br>
@支持漏洞列表:</br>

[1]ewebeditor</br>

[2]webdav</br>

[3]struts2</br></br>


Options:</br>

  -h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show this help message and exit</br>

  -n NAME, --name=NAME&nbsp;&nbsp;&nbsp;&nbsp;漏洞名称(*必填*)</br>

  -t TARGET, --target=TARGET&nbsp;&nbsp;&nbsp;目标url,默认为自动抓取(*可选*)</br></br>
  
@版本:1.0&nbsp;&nbsp;2016.04.22&nbsp;&nbsp;--by&nbsp;nmask

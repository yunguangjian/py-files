import pyautogui
ggwz=pyautogui.confirm('是否要更改已保存的学生数、免费数、学生折扣坐标位置？','更改位置',['OK','CANNCEL'])
if ggwz=='OK':
    pyautogui.alert('请把鼠标放到“学生数”位置，并按“空格”确认')
    xsds= str(pyautogui.position()[0:2])
    pyautogui.alert('请把鼠标放到“免费数”位置，并按“空格”确认')
    mfds= str(pyautogui.position()[0:2])
    pyautogui.alert('请把鼠标放到“学生折扣”位置，并按“空格”确认')
    xszk= str(pyautogui.position()[0:2])
    sbcs = open('sbcs.txt', 'w+')
    sbcs.write(f'{xsds}\n{mfds}\n{xszk}')
sbcs.close()